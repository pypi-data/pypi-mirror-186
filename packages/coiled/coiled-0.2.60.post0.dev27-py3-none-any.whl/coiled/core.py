"""
Cloud (and similarly its subclass CloudBeta) is not intended as a user-facing API but rather is a helper
for implementing top-level user-facing functions.

* Cloud contains methods for our "v1" API (e.g. software environments)
* CloudBeta contains methods for our "v2" API (clusters, package sync)

A few methods in Cloud are reused by CloudBeta, but not much. Ideally we would completely separate these classes
so there's no subclass relationship, or implement a tiny base class CloudBase with subclasses CloudV1 and CloudV2.

Some notes on async:

Because the distributed API can be used as either async and sync, Coiled can too. This is implemented with
leading-underscore async-only functions like "Cloud._create_software_environment", and then non-underscored
versions like "Cloud.create_software_environment", where the latter uses a helper method "cloud.sync" to do
the right thing depending on whether we're in a sync or async context.

When it comes to the Cluster class, this complexity is probably forced on us by distributed supporting sync and async.
But for our own stuff (e.g. create_software_environment) we could probably simplify to a simpler sync-only API
if we choose.
"""
from __future__ import annotations, with_statement

import asyncio
import copy
import datetime
import json
import logging
import numbers
import os
import pathlib
import platform
import sys
import threading
import time
import weakref
from contextlib import contextmanager
from dataclasses import dataclass
from json.decoder import JSONDecodeError
from typing import (
    Any,
    Awaitable,
    Callable,
    Coroutine,
    Dict,
    Generator,
    Generic,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
    cast,
    overload,
)

import aiohttp
import backoff
import dask
import dask.distributed
import distributed
import rich
import toolz
import yaml
from distributed.comm import parse_address
from distributed.utils import LoopRunner, sync
from importlib_metadata import PackageNotFoundError, version
from rich.console import Console
from rich.table import Table
from rich.text import Text
from tornado.ioloop import IOLoop
from typing_extensions import Literal, Protocol

from coiled.exceptions import (
    AccountConflictError,
    ApiResponseStatusError,
    AWSCredentialsParameterError,
    GCPCredentialsError,
    GCPCredentialsParameterError,
    NotFound,
    PermissionsError,
    RegistryParameterError,
    UnsupportedBackendError,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from .compatibility import COILED_VERSION, DISTRIBUTED_VERSION, PY_VERSION
from .context import COILED_SESSION_ID, TRACE_CONFIG, track_context
from .types import event_type_list
from .utils import (
    ALLOWED_PROVIDERS,
    COILED_LOGGER_NAME,
    Spinner,
    VmType,
    experimental,
    get_auth_header_value,
    handle_api_exception,
    handle_credentials,
    in_async_call,
    parse_gcp_region_zone,
    parse_identifier,
    parse_requested_memory,
    rich_console,
    validate_account,
    verify_aws_credentials,
)
from .websockets import ConfigureBackendConnector, WebsocketConnector

logger = logging.getLogger(COILED_LOGGER_NAME)
console = Console()
SUPPORTED_BACKENDS = {"aws", "gcp"}


class AWSSessionCredentials(TypedDict):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: Optional[str]
    Expiration: Optional[datetime.datetime]


def delete_docstring(func):
    delete_doc = """ Delete a {kind}

Parameters
---------
name
    Name of {kind} to delete.
"""
    func_name = func.__name__
    kind = " ".join(
        func_name.split("_")[1:]
    )  # delete_software_environments -> software environments
    func.__doc__ = delete_doc.format(kind=kind)
    return func


def list_docstring(func):

    list_doc = """ List {kind}s

Parameters
---------
account
    Name of the Coiled account to list {kind}s.
    If not provided, will use the ``coiled.account`` configuration
    value.

Returns
-------
:
    Dictionary with information about each {kind} in the
    specified account. Keys in the dictionary are names of {kind}s,
    while the values contain information about the corresponding {kind}.
"""
    func_name = func.__name__
    kind = " ".join(func_name.split("_")[1:])
    kind = kind[:-1]  # drop trailing "s"
    func.__doc__ = list_doc.format(kind=kind)
    return func


# This lock helps avoid a race condition between cluster creation in the
# in process backend, which temporarily modify coiled's dask config values,
# and the creation of new Cloud objects, with load those same config values.
# This works, but is not ideal.
_cluster_creation_lock = threading.RLock()


# Generic TypeVar for return value from sync/async function.
_T = TypeVar("_T")


# A generic that can only be True/False, allowing us to type async/sync
# versions of coiled objects.
Async = Literal[True]
Sync = Literal[False]
IsAsynchronous = TypeVar("IsAsynchronous", Async, Sync, bool)


# Short of writing type stubs for distributed or typing the underlying package,
# this is a useful cast.
class _SyncProtocol(Protocol):
    def __call__(
        self,
        loop: IOLoop,
        func: Callable[..., Awaitable[_T]],
        *args: Any,
        callback_timeout: numbers.Number,
        **kwargs: Any,
    ) -> _T:
        ...


sync = cast(_SyncProtocol, sync)


class Cloud(Generic[IsAsynchronous]):
    """Connect to Coiled

    Parameters
    ----------
    user
        Username for Coiled account. If not specified, will check the
        ``coiled.user`` configuration value.
    token
        Token for Coiled account. If not specified, will check the
        ``coiled.token`` configuration value.
    server
        Server to connect to. If not specified, will check the
        ``coiled.server`` configuration value.
    account
        The coiled account to use. If not specified,
        will check the ``coiled.account`` configuration value.
    asynchronous
        Set to True if using this Cloud within ``async``/``await`` functions or
        within Tornado ``gen.coroutines``. Otherwise this should remain
        ``False`` for normal use. Default is ``False``.
    loop
        If given, this event loop will be re-used, otherwise an appropriate one
        will be looked up or created.
    default_cluster_timeout
        Default timeout in seconds to wait for cluster startup before raising ``TimeoutError``.
        Pass ``None`` to wait forever, otherwise the default is 20 minutes.
    """

    _recent_sync: list[weakref.ReferenceType[Cloud[Sync]]] = list()
    _recent_async: list[weakref.ReferenceType[Cloud[Async]]] = list()

    @overload
    def __init__(
        self: Cloud[Sync],
        user: Optional[str] = None,
        token: Optional[str] = None,
        server: Optional[str] = None,
        account: Optional[str] = None,
        asynchronous: Sync = False,
        loop: Optional[IOLoop] = None,
        default_cluster_timeout: int = 20 * 60,
    ):
        ...

    @overload
    def __init__(
        self: Cloud[Async],
        user: Optional[str] = None,
        token: Optional[str] = None,
        server: Optional[str] = None,
        account: Optional[str] = None,
        asynchronous: Async = True,
        loop: Optional[IOLoop] = None,
        default_cluster_timeout: int = 20 * 60,
    ):
        ...

    @overload
    def __init__(
        self,
        user: Optional[str] = None,
        token: Optional[str] = None,
        server: Optional[str] = None,
        account: Optional[str] = None,
        asynchronous: bool = False,
        loop: Optional[IOLoop] = None,
        default_cluster_timeout: int = 20 * 60,
    ):
        ...

    def __init__(
        self,
        user: Optional[str] = None,
        token: Optional[str] = None,
        server: Optional[str] = None,
        account: Optional[str] = None,
        asynchronous: bool = False,
        loop: Optional[IOLoop] = None,
        default_cluster_timeout: int = 20 * 60,
    ):
        with _cluster_creation_lock:
            self.user = user or dask.config.get("coiled.user")
            self.token = token or dask.config.get("coiled.token")
            self.server = server or dask.config.get("coiled.server")
            if "://" not in self.server:
                self.server = "http://" + self.server
            self.server = self.server.rstrip("/")
            self._default_account = account or dask.config.get("coiled.account")
            self._default_backend_options = (
                dask.config.get("coiled.backend-options", None) or {}
            )
        self.session: Optional[aiohttp.ClientSession] = None
        self.status = "init"
        self.cluster_id: Optional[int] = None
        self._asynchronous = asynchronous
        self._loop_runner = LoopRunner(loop=loop, asynchronous=asynchronous)
        self._loop_runner.start()
        self.default_cluster_timeout = default_cluster_timeout

        if asynchronous:
            self._recent_async.append(weakref.ref(cast(Cloud[Async], self)))
        else:
            self._recent_sync.append(weakref.ref(cast(Cloud[Sync], self)))

        if not self.asynchronous:
            self._sync(self._start)

    def __repr__(self):
        return f"<Cloud: {self.user}@{self.server} - {self.status}>"

    def _repr_html_(self):
        text = (
            '<h3 style="text-align: left;">Cloud</h3>\n'
            '<ul style="text-align: left; list-style: none; margin: 0; padding: 0;">\n'
            f"  <li><b>User: </b>{self.user}</li>\n"
            f"  <li><b>Server: </b>{self.server}</li>\n"
            f"  <li><b>Account: </b>{self.default_account}</li>\n"
        )

        return text

    @property
    def loop(self):
        return self._loop_runner.loop

    @overload
    @classmethod
    def current(cls, asynchronous: Sync) -> Cloud[Sync]:
        ...

    @overload
    @classmethod
    def current(cls, asynchronous: Async) -> Cloud[Async]:
        ...

    @overload
    @classmethod
    def current(cls, asynchronous: bool) -> Cloud:
        ...

    @classmethod
    def current(cls, asynchronous: bool) -> Cloud:
        recent: list[weakref.ReferenceType[Cloud]]
        if asynchronous:
            recent = cls._recent_async
        else:
            recent = cls._recent_sync
        try:
            cloud = recent[-1]()
            while cloud is None or cloud.status != "running":
                recent.pop()
                cloud = recent[-1]()
        except IndexError:
            if asynchronous:
                return cls(asynchronous=True)
            else:
                return cls(asynchronous=False)
        else:
            return cloud

    @property
    def closed(self) -> bool:
        if self.session:
            return self.session.closed
        # If we haven't opened, we must be closed?
        return True

    @backoff.on_exception(
        backoff.expo,
        # `aiohttp.client_exceptions.ClientOSError` is the same as `aiohttp.ClientOSError`
        # except that pyright doesn't like the former
        aiohttp.ClientOSError,
        logger=logger,
    )
    async def _do_request_idempotent(
        self, *args, ensure_running: bool = True, **kwargs
    ):
        """
        This method retries more aggressively than _do_request.

        We may retry with no knowledge of the state of the original request so this
        should only ever be used to make idempotent API calls (e.g. non-mutating calls).
        """
        return await self._do_request(*args, ensure_running=ensure_running, **kwargs)

    @backoff.on_predicate(
        backoff.expo,
        lambda resp: resp.status in [502, 503, 504, 429],
        logger=logger,
        max_value=15,
    )
    async def _do_request(self, *args, ensure_running: bool = True, **kwargs):
        """
        This wraps the session.request call and injects a per-call UUID.

        Most of the time we check that this is in a "running" state before making
        requests. However, we can disable that by passing in ensure_running=False
        """
        session = self._ensure_session(ensure_running)
        response = await session.request(*args, **kwargs)
        return response

    def _ensure_session(self, ensure_running=True) -> aiohttp.ClientSession:
        if self.session and (not ensure_running or self.status == "running"):
            return self.session
        else:
            raise RuntimeError("Cloud is not running, did you forget to await it?")

    @track_context
    async def _start(self):
        if self.status != "init":
            return self
        # Check that server and token are valid
        self.user, self.token, self.server = await handle_credentials(
            server=self.server, token=self.token, save=False
        )
        # TODO: revert when we remove versioneer
        if dask.config.get("coiled.no-minimum-version-check", False):
            client_version = "coiled-frontend-js"
        else:
            client_version = COILED_VERSION

        self.session = aiohttp.ClientSession(
            trace_configs=[TRACE_CONFIG],
            headers={
                "Authorization": get_auth_header_value(self.token),
                "Client-Version": client_version,
                "coiled-session-id": COILED_SESSION_ID,
            },
        )
        # do normal queries
        response = await self._do_request(
            "GET", self.server + "/api/v1/users/me/", ensure_running=False
        )
        if response.status == 426:
            # Upgrade required
            await handle_api_exception(response)
        if response.status >= 400:
            await handle_api_exception(response)

        data = await response.json()
        self.accounts = {
            d["account"]["slug"]: toolz.merge(
                d["account"],
                {"admin": d["is_admin"]},
            )
            for d in data["membership_set"]
        }
        if self._default_account:
            self._verify_account(self._default_account)

        self.status = "running"

        return self

    @property
    def default_account(self):
        if self._default_account:
            return self._default_account
        elif len(self.accounts) == 1:
            return toolz.first(self.accounts)
        elif self.user in self.accounts:
            return self.user
        elif self.user.lower() in self.accounts:
            return self.user.lower()
        else:
            raise ValueError(
                "Please provide an account among the following options",
                list(self.accounts),
            )

    async def _close(self) -> None:
        if self.session:
            await self.session.close()
        self.status = "closed"

    @overload
    def close(self: Cloud[Sync]) -> None:
        ...

    @overload
    def close(self: Cloud[Async]) -> Awaitable[None]:
        ...

    def close(self) -> Optional[Awaitable[None]]:
        """Close connection to Coiled"""
        result = self._sync(self._close)
        self._loop_runner.stop()
        return result

    def __await__(
        self: Cloud[Async],
    ) -> Generator[None, None, Cloud[Async]]:
        return self._start().__await__()

    async def __aenter__(self: Cloud[Async]) -> Cloud[Async]:
        return await self._start()

    async def __aexit__(self: Cloud[Async], typ, value, tb) -> None:
        await self._close()

    def __enter__(self: Cloud[Sync]) -> Cloud[Sync]:
        return self

    def __exit__(self: Cloud[Sync], typ, value, tb) -> None:
        self.close()

    @property
    def asynchronous(self) -> bool:
        """Are we running in the event loop?"""
        return in_async_call(self.loop, default=self._asynchronous)

    @overload
    def _sync(
        self: Cloud[Sync],
        func: Callable[..., Coroutine[None, None, _T]],
        *args,
        asynchronous: Union[Sync, Literal[None]] = None,
        callback_timeout=None,
        **kwargs,
    ) -> _T:
        ...

    @overload
    def _sync(
        self: Cloud[Async],
        func: Callable[..., Coroutine[None, None, _T]],
        *args,
        asynchronous: Union[bool, Literal[None]] = None,
        callback_timeout=None,
        **kwargs,
    ) -> Coroutine[None, None, _T]:
        ...

    def _sync(
        self,
        func: Callable[..., Coroutine[None, None, _T]],
        *args,
        asynchronous: Optional[bool] = None,
        callback_timeout=None,
        **kwargs,
    ) -> Union[_T, Coroutine[None, None, _T]]:
        callback_timeout = dask.utils.parse_timedelta(callback_timeout, "s")
        if asynchronous is None:
            asynchronous = self.asynchronous
        if asynchronous:
            future = func(*args, **kwargs)
            if callback_timeout is not None:
                future = asyncio.wait_for(future, callback_timeout)
            return future
        else:
            return sync(
                self.loop, func, *args, callback_timeout=callback_timeout, **kwargs
            )

    def _verify_account(self, account: str):
        """Perform sanity checks on account values

        In particular, this raises and informative error message if the
        account is not found, and provides a list of possible options.
        """
        account = account or self.default_account
        validate_account(account)
        if account not in self.accounts:
            raise PermissionError(
                "Account not found: '{}'\n"
                "Possible accounts: {}".format(account, sorted(self.accounts))
            )

    def _verify_per_cluster_backend_options(
        self, backend_options: Optional[dict] = None
    ):
        """Validation for cluster- (vs account-) level specified options."""
        backend_options = backend_options or {}
        if "network" in backend_options:
            raise PermissionError(
                "Network options cannot be specified per cluster. "
                "Use coiled.set_backend_options() to set for account."
            )

    @overload
    def create_api_token(
        self: Cloud[Sync],
        *,
        label: Optional[str] = None,
        days_to_expire: Optional[int] = None,
    ) -> dict:
        ...

    @overload
    def create_api_token(
        self: Cloud[Async],
        *,
        label: Optional[str] = None,
        days_to_expire: Optional[int] = None,
    ) -> Awaitable[dict]:
        ...

    def create_api_token(
        self, *, label: Optional[str] = None, days_to_expire: Optional[int] = None
    ) -> Union[dict, Awaitable[dict]]:
        return self._sync(
            self._create_api_token, label=label, days_to_expire=days_to_expire
        )

    @overload
    def list_api_tokens(
        self: Cloud[Sync], include_inactive: bool = False
    ) -> dict[str, dict]:
        ...

    @overload
    def list_api_tokens(
        self: Cloud[Async], include_inactive: bool = False
    ) -> Awaitable[dict[str, dict]]:
        ...

    def list_api_tokens(
        self, include_inactive: bool = False
    ) -> Union[Awaitable[dict[str, dict]], dict[str, dict]]:
        return self._sync(self._list_api_tokens, include_inactive=include_inactive)

    @overload
    def revoke_all_api_tokens(self: Cloud[Sync]) -> None:
        ...

    @overload
    def revoke_all_api_tokens(self: Cloud[Async]) -> Awaitable[None]:
        ...

    def revoke_all_api_tokens(self) -> Optional[Awaitable[None]]:
        return self._sync(
            self._revoke_all_api_tokens,
        )

    async def _revoke_all_api_tokens(self) -> None:
        tokens = await self._list_api_tokens(include_inactive=True)
        logged_in_token_id = None
        # we could be more asyncy here by kicking off multiple revokes
        # at once but this seems fine
        for token_id in tokens.keys():
            if self.token.startswith(token_id):
                # this is the current token! revoke it last
                logged_in_token_id = token_id
            else:
                await self._revoke_api_token(identifier=token_id)

        # after transitioning to new api tokens, we expect we would
        # find the in-use token in the tokens list
        # but in the meantime the in-use token might be an old-style one we can't revoke
        if logged_in_token_id is None:
            rich.print("Did not revoke the token you're logged in with now.")
        else:
            await self._revoke_api_token(identifier=logged_in_token_id)

    @overload
    def revoke_api_token(
        self: Cloud[Sync],
        *,
        identifier: Optional[str] = None,
        label: Optional[str] = None,
    ) -> None:
        ...

    @overload
    def revoke_api_token(
        self: Cloud[Async],
        *,
        identifier: Optional[str] = None,
        label: Optional[str] = None,
    ) -> Awaitable[None]:
        ...

    def revoke_api_token(
        self, *, identifier: Optional[str] = None, label: Optional[str] = None
    ) -> Union[None, Awaitable[None]]:
        return self._sync(self._revoke_api_token, identifier=identifier, label=label)

    @overload
    def create_software_environment(
        self: Cloud[Sync],
        name: Optional[str] = None,
        *,
        account: Optional[str] = None,
        conda: Optional[Union[list, dict, str]] = None,
        pip: Optional[Union[list, str]] = None,
        container: Optional[str] = None,
        post_build: Optional[Union[list, str]] = None,
        conda_env_name: Optional[str] = None,
        backend_options: Optional[Dict] = None,
        log_output=sys.stdout,
        private: bool = False,
        force_rebuild: bool = False,
        environ: Optional[Dict] = None,
        use_entrypoint: bool = True,
    ) -> None:
        ...

    @overload
    def create_software_environment(
        self: Cloud[Async],
        name: Optional[str] = None,
        *,
        account: Optional[str] = None,
        conda: Optional[Union[list, dict, str]] = None,
        pip: Optional[Union[list, str]] = None,
        container: Optional[str] = None,
        post_build: Optional[Union[list, str]] = None,
        conda_env_name: Optional[str] = None,
        backend_options: Optional[Dict] = None,
        log_output=sys.stdout,
        private: bool = False,
        force_rebuild: bool = False,
        environ: Optional[Dict] = None,
        use_entrypoint: bool = True,
    ) -> Awaitable[None]:
        ...

    def create_software_environment(
        self,
        name: Optional[str] = None,
        *,
        account: Optional[str] = None,
        conda: Optional[Union[list, dict, str]] = None,
        pip: Optional[Union[list, str]] = None,
        container: Optional[str] = None,
        post_build: Optional[Union[list, str]] = None,
        conda_env_name: Optional[str] = None,
        backend_options: Optional[Dict] = None,
        log_output=sys.stdout,
        private: bool = False,
        force_rebuild: bool = False,
        environ: Optional[Dict] = None,
        use_entrypoint: bool = True,
    ) -> Optional[Awaitable[None]]:
        return self._sync(
            self._create_software_environment,
            name=name,
            account=account,
            conda=conda,
            pip=pip,
            container=container,
            post_build=post_build,
            log_output=log_output,
            conda_env_name=conda_env_name,
            backend_options=backend_options,
            private=private,
            force_rebuild=force_rebuild,
            environ=environ,
            use_entrypoint=use_entrypoint,
        )

    @track_context
    async def _create_software_environment(
        self,
        name=None,
        *,
        account: Optional[str] = None,
        conda=None,
        pip=None,
        container=None,
        post_build=None,
        conda_env_name: Optional[str] = None,
        log_output=sys.stdout,
        backend_options: Optional[Dict] = None,
        private: bool = False,
        force_rebuild: bool = False,
        environ: Optional[Dict] = None,
        use_entrypoint: bool = True,
    ) -> None:
        """
        :param name:
        :param conda:
        :param pip:
        :param container:
        :param post_build:
        :param conda_env_name:
        :param log_output:
        :param backend_options: Dict or None
          backend_options["container_registry"]
        :param private:
        :param force_rebuild:
        :param environ: Dict or None
        :return:
        """
        session = self._ensure_session()
        if conda is None and container is None and pip is not None:
            v = ".".join(map(str, sys.version_info[:2]))
            conda = {"dependencies": [f"python={v}", {"pip": []}]}
        elif isinstance(conda, list):
            conda = {"dependencies": conda}
        elif isinstance(conda, (str, pathlib.Path)):
            if not os.path.isfile(conda):
                raise FileNotFoundError(
                    f"Unable to find file '{conda}', please make sure it exists "
                    "and the path is correct. If you are trying to create a "
                    "software environment by specifying dependencies, you can "
                    "do so by passing a list of dependencies or a dictionary. For example:\n"
                    "\tcoiled.create_software_environment(\n"
                    "\t    name='my-env', conda={'channels': ['conda-forge'], 'dependencies': ['coiled']}\n"
                    "\t)"
                )
            else:
                # Local conda environment YAML file
                with open(conda, mode="r") as f:
                    conda = yaml.safe_load(f)

        if isinstance(pip, (str, pathlib.Path)):
            if not os.path.isfile(pip):
                raise FileNotFoundError(
                    f"Unable to find file '{pip}', please make sure it exists "
                    "and the path is correct. If you are trying to create a "
                    "software environment by specifying dependencies, you can "
                    "do so by passing a list of dependencies. For example:\n"
                    "\tcoiled.create_software_environment(\n"
                    "\t    name='my-env', pip=['coiled']\n"
                    "\t)"
                )
            else:
                # Local pip requirements file
                with open(pip, mode="r") as f:
                    pip = f.read().splitlines()

        if isinstance(post_build, (str, pathlib.Path)):
            # Post-build script
            with open(post_build, mode="r") as f:
                post_build = f.read().splitlines()

        # Conda supports specifying pip packages via their CLI, but not when
        # using conda.api.Solver. So we move any pip packages to the pip portion
        # of this software environment
        if conda is not None:
            for idx, dep in enumerate(conda["dependencies"]):
                if isinstance(dep, dict) and list(dep.keys()) == ["pip"]:
                    # Copy conda to avoid mutating input from users
                    conda = copy.deepcopy(conda)
                    pip_packages = conda["dependencies"].pop(idx)["pip"]
                    if pip is not None:
                        pip = pip + pip_packages
                    else:
                        pip = pip_packages

        # Remove duplicates and ensure consistent package ordering which helps with
        # downstream tokenization of package spec
        if pip is not None:
            pip = sorted(set(pip))
        if conda is not None:
            conda["dependencies"] = sorted(set(conda["dependencies"]))

        if name is None and conda is not None and "name" in conda:
            name = conda["name"]
        if name is None:
            raise ValueError("Must provide a name when creating a software environment")

        account, name = self._normalize_name(
            str(name), context_account=account, raise_on_account_conflict=True
        )

        # Connect to the websocket, send the data and get some logs
        data = {
            "type": "build",
            "container": container,
            "conda": conda,
            "conda_env_name": conda_env_name,
            "pip": pip,
            "post_build": post_build,
            "options": {**self._default_backend_options, **(backend_options or {})},
            "private": private,
            "force_rebuild": force_rebuild,
            "environ": environ or {},
            "use_entrypoint": use_entrypoint,
        }

        ws_server = self.server.replace("http", "ws", 1)

        ws = WebsocketConnector(
            endpoint=f"{ws_server}/ws/api/v1/{account}/software_environments/{name}/",
            notifications_endpoint=f"{ws_server}/ws/api/v1/{account}/notifications/",
            session=session,
            log_output=log_output,
            connection_error_message=(
                "Unable to connect to server, do you have permissions to "
                f'create environments in the "{account}" account?'
            ),
        )
        await ws.connect()
        await ws.send_json(data)
        await ws.stream_messages()

    @track_context
    async def _create_api_token(
        self, label: Optional[str] = None, days_to_expire: Optional[int] = None
    ) -> dict:
        label_str = "no label" if label is None else f"label '{label}'"
        rich.print(
            f"Generating an API token with {label_str} expiring in {days_to_expire} days..."
        )

        data = {}
        if label is not None:
            data["label"] = label
        if days_to_expire is not None:
            expiry = datetime.datetime.utcnow() + datetime.timedelta(
                days=days_to_expire
            )
            data["expiry"] = expiry.isoformat()
        response = await self._do_request(
            "POST",
            self.server + "/api/v1/api-tokens/",
            json=data,
        )
        if response.status >= 400:
            await handle_api_exception(response)

        return await response.json()

    @track_context
    async def _list_api_tokens(self, include_inactive) -> dict[str, dict]:
        tokens = await self._depaginate(self._list_api_tokens_page)
        if include_inactive:
            return tokens
        else:
            return {
                t_id: t_details
                for t_id, t_details in tokens.items()
                if not t_details["revoked"] and not t_details["expired"]
            }

    @track_context
    async def _list_api_tokens_page(
        self, page: int
    ) -> Tuple[dict[str, dict], Optional[str]]:
        response = await self._do_request(
            "GET",
            self.server + "/api/v1/api-tokens/",
            params={"page": page},
        )
        if response.status >= 400:
            await handle_api_exception(response)
            return {}, None
        else:
            response_json = await response.json()
            results = {r["identifier"]: r for r in response_json["results"]}
            return results, response_json["next"]

    @track_context
    async def _revoke_api_token(
        self, *, identifier: Optional[str] = None, label: Optional[str] = None
    ) -> None:
        if label is None and identifier is None:
            raise ValueError("We need a label or identifier to revoke a token.")

        if label is not None:
            if identifier is not None:
                raise ValueError(
                    "Only a label or identifier should be provided, but not both."
                )

            tokens = await self._list_api_tokens(include_inactive=False)
            identifiers_found = [
                token_id
                for token_id, details in tokens.items()
                if details["label"] == label
            ]

            if len(identifiers_found) == 0:
                raise ValueError(f"Found no tokens with label '{label}'.")
            elif len(identifiers_found) > 1:
                raise ValueError(
                    f"Found multiple tokens with label '{label}'. Please revoke with the `identifier` instead."
                )

            else:
                [identifier] = identifiers_found

        rich.print(f"Revoking API token with identifier '{identifier}' ...")

        response = await self._do_request(
            "DELETE",
            self.server + f"/api/v1/api-tokens/{identifier}/revoke",
        )

        if response.status >= 400:
            if response.status == 404:
                raise ValueError(
                    f"Could not find an API token with identifier {identifier}"
                )
            await handle_api_exception(response)

    @staticmethod
    async def _depaginate(
        func: Callable[..., Awaitable[Tuple[dict, Optional[str]]]],
        *args,
        **kwargs,
    ) -> dict:
        results_all = {}
        page = 1
        while True:
            kwargs["page"] = page
            results, next = await func(*args, **kwargs)
            results_all.update(results)
            page += 1
            if (not results) or next is None:
                break
        return results_all

    @track_context
    async def _list_software_environments(self, account: Optional[str] = None) -> dict:
        return await self._depaginate(
            self._list_software_environments_page, account=account
        )

    @track_context
    async def _list_software_environments_page(
        self, page: int, account: Optional[str] = None
    ) -> Tuple[dict, Optional[str]]:
        account = account or self.default_account
        response = await self._do_request(
            "GET",
            self.server + f"/api/v1/{account}/software_environments/",
            params={"page": page},
        )
        if response.status >= 400:
            await handle_api_exception(response)
            return {}, None
        else:
            response_json = await response.json()
            results = {
                f"{format_account_output(r['account'])}/{r['name']}": format_software_environment_output(
                    r
                )
                for r in response_json["results"]
            }

            return results, response_json["next"]

    @track_context
    async def _list_instance_types(
        self,
        backend: Optional[str] = None,
        min_cores: Optional[int] = None,
        min_gpus: Optional[int] = None,
        min_memory: Optional[Union[int, str, float]] = None,
        cores: Optional[Union[int, list[int]]] = None,
        memory: Optional[
            Union[int, float, str, list[int], list[str], list[float]]
        ] = None,
        gpus: Optional[Union[int, list[int]]] = None,
    ) -> dict[str, VmType]:

        if backend:
            user_provider = backend
        else:
            user_provider = await self.get_account_provider_name(
                account=self.default_account
            )

        if user_provider and user_provider not in ALLOWED_PROVIDERS:
            raise UnsupportedBackendError(
                (
                    f"Unknown cloud provider provided - {user_provider} is not"
                    f" one of {ALLOWED_PROVIDERS}"
                )
            )

        all_instance_types = await self._depaginate(
            self._list_instance_types_page,
            min_cores=min_cores,
            min_gpus=min_gpus,
            min_memory=min_memory,
            cores=cores,
            memory=memory,
            gpus=gpus,
            backend=user_provider.lower(),
        )

        return {f"{name}": i for name, i in all_instance_types.items()}

    @delete_docstring
    def set_gcp_credentials(
        self,
        gcp_credentials: dict,
        instance_service_account: Optional[str] = None,
        account: Optional[str] = None,
    ):
        return self._sync(
            self._set_gcp_credentials,
            account=account,
            gcp_credentials=gcp_credentials,
            instance_service_account=instance_service_account,
        )

    @track_context
    async def _set_gcp_credentials(
        self,
        gcp_credentials: dict,
        instance_service_account: Optional[str],
        account: Optional[str] = None,
    ):
        account = account or self.default_account
        payload = {
            **gcp_credentials,
            "instance_service_account": instance_service_account,
        }
        response = await self._do_request(
            "POST",
            self.server + f"/api/v2/cloud-credentials/{account}/gcp",
            json=payload,
        )
        if not response.ok:
            logger.debug(
                f"Failed to update gcp creds {response.status}:{await response.text()}"
            )

    @delete_docstring
    def unset_gcp_credentials(self, account: Optional[str] = None):
        return self._sync(self._unset_gcp_credentials, account=account)

    @track_context
    async def _unset_gcp_credentials(self, account: Optional[str] = None):
        account = account or self.default_account
        response = await self._do_request(
            "DELETE",
            self.server + f"/api/v2/cloud-credentials/{account}/gcp",
        )
        if not response.ok:
            logger.debug(
                f"Failed to delete gcp creds {response.status}:{await response.text()}"
            )

    @delete_docstring
    def set_aws_credentials(self, aws_credentials: dict, account: Optional[str] = None):
        return self._sync(
            self._set_aws_credentials, account=account, aws_credentials=aws_credentials
        )

    @track_context
    async def _set_aws_credentials(
        self, aws_credentials: dict, account: Optional[str] = None
    ):
        account = account or self.default_account
        response = await self._do_request(
            "POST",
            self.server + f"/api/v2/cloud-credentials/{account}/aws",
            json=aws_credentials,
        )
        if not response.ok:
            logger.debug(
                f"Failed to update aws creds {response.status}:{await response.text()}"
            )

    @delete_docstring
    def unset_aws_credentials(self, account: Optional[str] = None):
        return self._sync(self._unset_aws_credentials, account=account)

    @track_context
    async def _unset_aws_credentials(self, account: Optional[str] = None):
        account = account or self.default_account
        response = await self._do_request(
            "DELETE",
            self.server + f"/api/v2/cloud-credentials/{account}/aws",
        )
        if not response.ok:
            logger.debug(
                f"Failed to delete aws creds {response.status}:{await response.text()}"
            )

    @track_context
    async def _list_instance_types_page(
        self,
        page: int,
        min_cores: Optional[int] = None,
        min_gpus: Optional[int] = None,
        min_memory: Optional[Union[int, str, float]] = None,
        cores: Optional[Union[int, list[int]]] = None,
        memory: Optional[
            Union[int, str, float, list[int], list[str], list[float]]
        ] = None,
        gpus: Optional[Union[int, list[int]]] = None,
        backend: Optional[str] = None,
    ) -> Tuple[dict, Optional[str]]:

        parsed_memory = parse_requested_memory(memory, min_memory)
        params = {"page": page, **parsed_memory}

        # This isn't particularly pretty, but we are handling the case
        # where users specify a range for cores/memory/gpus or an exact
        # match
        if isinstance(cores, list):
            params["cores__gte"] = min(cores)
            params["cores__lte"] = max(cores)
        elif isinstance(cores, int):
            params["cores"] = cores

        if isinstance(gpus, list):
            params["gpus__gte"] = min(gpus)
            params["gpus__lte"] = max(gpus)
        elif isinstance(gpus, int):
            params["gpus"] = gpus

        if min_cores:
            params["cores__gte"] = min_cores

        if min_gpus:
            params["gpus__gte"] = min_gpus

        if backend:
            params["backend_type"] = (
                backend if backend.startswith("vm_") else f"vm_{backend}"
            )

        response = await self._do_request(
            "GET",
            f"{self.server}/api/v1/vm-types/",
            params=params,
        )

        if response.status == 200:
            body = await response.json()

            results = {f"{r['name']}": r for r in body["results"]}
            return results, body["next"]

        else:
            msg = (
                f"Coiled API responded with a {response.status} status code "
                "while fetching available instance types."
            )
            raise ApiResponseStatusError(msg)

    @overload
    def list_software_environments(
        self: Cloud[Sync], account: Optional[str] = None
    ) -> dict:
        ...

    @overload
    def list_software_environments(
        self: Cloud[Async], account: Optional[str] = None
    ) -> Awaitable[dict]:
        ...

    @list_docstring
    def list_software_environments(
        self, account: Optional[str] = None
    ) -> Union[dict, Awaitable[dict]]:
        return self._sync(self._list_software_environments, account=account)

    def _normalize_name(
        self,
        name: str,
        context_account: Optional[str] = None,
        raise_on_account_conflict: bool = False,
        allow_uppercase: bool = False,
    ) -> Tuple[str, str]:
        account, parsed_name, _ = parse_identifier(
            name, allow_uppercase=allow_uppercase
        )
        if (
            raise_on_account_conflict
            and context_account is not None
            and account is not None
            and context_account != account
        ):
            raise AccountConflictError(
                unparsed_name=name,
                account_from_name=account,
                account=context_account,
            )
        account = account or context_account or self.default_account
        return account, parsed_name

    @overload
    def delete_software_environment(
        self: Cloud[Sync], name: str, account: Optional[str] = None
    ) -> None:
        ...

    @overload
    def delete_software_environment(
        self: Cloud[Async], name: str, account: Optional[str] = None
    ) -> Awaitable[None]:
        ...

    @delete_docstring
    def delete_software_environment(
        self, name: str, account: Optional[str] = None
    ) -> Optional[Awaitable[None]]:
        return self._sync(self._delete_software_environment, name, account)

    @track_context
    async def _delete_software_environment(
        self, name: str, account: Optional[str] = None
    ) -> None:
        context_account = account
        account, name, tag = parse_identifier(name)
        account = account or context_account or self.default_account

        if tag:
            name = ":".join([name, tag])
        response = await self._do_request(
            "DELETE",
            f"{self.server}/api/v1/{account}/software_environments/{name}/",
        )
        if response.status == 404:
            raise NotFound(
                f"Unable to find software environment with the name '{name}' "
                f"in the account '{account}'."
            )
        elif response.status == 403:
            await handle_api_exception(response, exception_cls=PermissionsError)
        elif response.status >= 400:
            await handle_api_exception(response)
        else:
            rich.print("[green]Software environment deleted successfully.")

    @overload
    def set_backend_options(
        self: Cloud[Sync],
        backend_options: dict,
        account: Optional[str] = None,
        log_output=sys.stdout,
    ) -> str:
        ...

    @overload
    def set_backend_options(
        self: Cloud[Async],
        backend_options: dict,
        account: Optional[str] = None,
        log_output=sys.stdout,
    ) -> Awaitable[str]:
        ...

    def set_backend_options(
        self,
        backend_options: dict,
        account: Optional[str] = None,
        log_output=sys.stdout,
    ) -> Union[str, Awaitable[str]]:

        return self._sync(
            self._set_backend_options,
            backend_options,
            account=account,
            log_output=log_output,
        )

    @track_context
    async def _set_backend_options(
        self,
        backend_options: dict,
        account: Optional[str] = None,
        log_output=sys.stdout,
    ) -> str:
        session = self._ensure_session()
        account = account or self.default_account
        self._verify_account(account)
        logging_context = {}
        default_configuration_message = {
            "type": "update_options",
            "logging_context": logging_context,
            "data": backend_options,
        }
        ws_server = self.server.replace("http", "ws", 1)
        ws = ConfigureBackendConnector(
            endpoint=f"{ws_server}/ws/api/v1/{account}/cluster-info/",
            notifications_endpoint=f"{ws_server}/ws/api/v1/{account}/notifications/",
            session=session,
            log_output=log_output,
            connection_error_message=(
                "Unable to connect to server, do you have permissions to "
                f'edit backend_options in the "{account}" account?'
            ),
        )
        await ws.connect()
        await ws.send_json(default_configuration_message)
        with Spinner():
            await ws.stream_messages()
        return f"{self.server}/{account}/account"

    @overload
    def list_instance_types(
        self: Cloud[Sync],
        backend: Optional[str],
        min_cores: Optional[int],
        min_gpus: Optional[int],
        min_memory: Optional[Union[int, str, float]],
        cores: Optional[Union[int, list[int]]],
        memory: Optional[Union[int, str, float, list[int], list[str], list[float]]],
        gpus: Optional[Union[int, list[int]]],
    ) -> dict[str, VmType]:
        ...

    @overload
    def list_instance_types(
        self: Cloud[Async],
        backend: Optional[str],
        min_cores: Optional[int],
        min_gpus: Optional[int],
        min_memory: Optional[Union[int, str, float]],
        cores: Optional[Union[int, list[int]]],
        memory: Optional[Union[int, str, float, list[int], list[str], list[float]]],
        gpus: Optional[Union[int, list[int]]],
    ) -> Awaitable[dict[str, VmType]]:
        ...

    def list_instance_types(
        self,
        backend: Optional[str] = None,
        min_cores: Optional[int] = None,
        min_gpus: Optional[int] = None,
        min_memory: Optional[Union[int, str, float]] = None,
        cores: Optional[Union[int, list[int]]] = None,
        memory: Optional[
            Union[int, str, float, list[int], list[str], list[float]]
        ] = None,
        gpus: Optional[
            Union[
                int,
                list[int],
            ]
        ] = None,
    ) -> Union[Awaitable[dict[str, VmType]], dict[str, VmType]]:
        return self._sync(
            self._list_instance_types,
            backend=backend,
            min_cores=min_cores,
            min_gpus=min_gpus,
            min_memory=min_memory,
            cores=cores,
            memory=memory,
            gpus=gpus,
        )

    @overload
    def list_gpu_types(self: Cloud[Sync]) -> dict:
        ...

    @overload
    def list_gpu_types(self: Cloud[Async]) -> Coroutine[None, None, dict]:
        ...

    def list_gpu_types(self):
        return self._sync(self._list_gpu_types)

    @track_context
    async def _list_gpu_types(self):
        title = "GCP GPU Types"
        allowed_gpus = "nvidia-tesla-t4"

        return {title: allowed_gpus}

    @track_context
    async def get_aws_credentials(self, account: Optional[str] = None):
        """Return the logged in user's AWS credentials"""
        # this doesn't work, since aws credentials aren't (currently) returned by this endpoint
        backend_options = await self.get_backend_options(account)
        credentials = backend_options.get("options", {}).get("credentials", {})
        return credentials

    @track_context
    async def get_backend_options(self, account: Optional[str] = None) -> dict:
        """Queries the API to get the backend options from account."""
        account = account or self.default_account
        response = await self._do_request(
            "GET",
            self.server + f"/api/v1/{account}/backend_options/",
        )
        if response.status >= 400:
            await handle_api_exception(response)

        backend_options = await response.json()
        return backend_options

    @track_context
    async def get_account_provider_name(self, account: Optional[str] = None) -> str:
        """Get the provider name used by the account.

        Currently we are using this method only for the validation of instance
        types when users provide them. So we are handling the three clouds only
        otherwise we will return whatever is in the backend or an empty string.

        """
        backend_options = await self.get_backend_options(account)

        if backend_options.get("backend") == "vm":
            provider_name = backend_options.get("options", {}).get("provider_name", "")

        elif backend_options.get("backend") == "vm_aws":
            provider_name = "aws"
        elif backend_options.get("backend") == "vm_gcp":
            provider_name = "gcp"
        else:
            provider_name = backend_options.get("backend", "")

        return provider_name

    @overload
    def get_software_info(
        self: Cloud[Sync], name: str, account: Optional[str] = None
    ) -> dict:
        ...

    @overload
    def get_software_info(
        self: Cloud[Async], name: str, account: Optional[str] = None
    ) -> Awaitable[dict]:
        ...

    def get_software_info(
        self, name: str, account: Optional[str] = None
    ) -> Union[dict, Awaitable[dict]]:
        return self._sync(self._get_software_info, name=name, account=account)

    @track_context
    async def _get_software_info(
        self, name: str, account: Optional[str] = None
    ) -> dict:
        """Retrieve solved spec for a Coiled software environment

        Parameters
        ----------
        name
            Software environment name

        Returns
        -------
        results
            Coiled software environment information
        """
        account, name = self._normalize_name(name, context_account=account)

        response = await self._do_request(
            "GET",
            self.server + f"/api/v1/{account}/software_environments/{name}/",
        )
        if response.status >= 400:
            text = await response.text()
            if "Not found" in text:
                raise ValueError(
                    f"Could not find a '{account}/{name}' Coiled software environment"
                )
            else:
                await handle_api_exception(response)

        results = await response.json()
        return results

    @overload
    def list_core_usage(self: Cloud[Sync], account: Optional[str] = None) -> dict:
        ...

    @overload
    def list_core_usage(
        self: Cloud[Async], account: Optional[str] = None
    ) -> Awaitable[dict]:
        ...

    def list_core_usage(
        self, account: Optional[str] = None
    ) -> Union[Awaitable[dict], dict]:
        return self._sync(self._list_core_usage, account=account)

    @track_context
    async def _list_core_usage(self, account: Optional[str] = None) -> dict:
        account = account or self.default_account

        response = await self._do_request(
            "GET", f"{self.server}/api/v1/{account}/usage/cores/"
        )

        if response.status >= 400:
            await handle_api_exception(response)

        result = await response.json()

        return result

    async def _list_local_versions(self) -> dict:
        try:
            conda_version = version("conda")
        except PackageNotFoundError:
            conda_version = "None"
        try:
            pip_version = version("pip")
        except PackageNotFoundError:
            pip_version = "None"

        return {
            "operating_system": platform.platform(),
            "python": PY_VERSION,
            "pip": pip_version,
            "conda": conda_version,
            "coiled": COILED_VERSION,
            "dask": dask.__version__,
            "distributed": distributed.__version__,
        }

    @overload
    def list_local_versions(self: Cloud[Sync]) -> dict:
        ...

    @overload
    def list_local_versions(self: Cloud[Async]) -> Awaitable[dict]:
        ...

    def list_local_versions(
        self,
    ) -> Union[Awaitable[dict], dict]:
        return self._sync(self._list_local_versions)

    @overload
    def get_notifications(
        self: Cloud[Sync],
        json: Literal[True],
        account: Optional[str] = None,
        limit: int = 100,
        level: Union[int, str] = logging.NOTSET,
        event_type: Optional[str] = None,
    ) -> List[dict]:
        ...

    @overload
    def get_notifications(
        self: Cloud[Async],
        json: Literal[True],
        account: Optional[str] = None,
        limit: int = 100,
        level: Union[int, str] = logging.NOTSET,
        event_type: Optional[str] = None,
    ) -> Awaitable[List[dict]]:
        ...

    @overload
    def get_notifications(
        self: Cloud[Sync],
        json: bool,
        account: Optional[str] = None,
        limit: int = 100,
        level: Union[int, str] = logging.NOTSET,
        event_type: Optional[str] = None,
    ) -> Optional[List[dict]]:
        ...

    @overload
    def get_notifications(
        self: Cloud[Async],
        json: bool,
        account: Optional[str] = None,
        limit: int = 100,
        level: Union[int, str] = logging.NOTSET,
        event_type: Optional[str] = None,
    ) -> Awaitable[Optional[List[dict]]]:
        ...

    def get_notifications(
        self,
        json: bool = False,
        account: Optional[str] = None,
        limit: int = 100,
        level: Union[int, str] = logging.NOTSET,
        event_type: Optional[str] = None,
    ) -> Union[Awaitable[Optional[List[dict]]], Optional[List[dict]]]:
        # TODO: warn
        return self._sync(
            self._get_notifications,
            json=json,
            account=account,
            limit=limit,
            level=level,
            event_type=event_type,
        )

    @track_context
    async def _get_notifications(
        self,
        json: bool = False,
        account: Optional[str] = None,
        limit: int = 100,
        level: Union[int, str] = logging.NOTSET,
        event_type: Optional[str] = None,
    ) -> Optional[List[dict]]:
        account = account or self.default_account
        params = {"limit": limit, "level": level}
        if event_type:
            params["event_type"] = event_type
        response = await self._do_request(
            "GET",
            f"{self.server}/api/v1/{account}/notifications/",
            params=params,
        )

        if response.status >= 400:
            await handle_api_exception(response)

        result = await response.json()
        notifications: List[dict] = result["notifications"]

        if json:
            return notifications

        notifications_table = Table(title="Notifications")
        notifications_table.add_column("time", justify="center", overflow="fold")
        notifications_table.add_column("id", justify="center", overflow="fold")
        notifications_table.add_column("level", justify="center", overflow="fold")
        notifications_table.add_column("event_type", justify="center", overflow="fold")
        notifications_table.add_column("elapsed", justify="center", overflow="fold")
        notifications_table.add_column("msg", justify="center", overflow="fold")
        notifications_table.add_column("data", justify="center", overflow="fold")

        for notification in notifications:
            try:
                local_time = time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime(notification["timestamp"])
                )
            except KeyError:
                local_time = "???"
            notifications_table.add_row(
                str(local_time),
                str(notification.get("id", "")),
                logging.getLevelName(notification.get("level", "")),
                str(notification.get("event_type", "")),
                str(notification.get("elapsed", "") or ""),
                str(notification["msg"]),
                str(notification.get("data", "")),
            )

        console = Console()
        console.print(notifications_table)
        return None

    @track_context
    async def _noop_wait(self, duration: int):
        response = await self._do_request(
            "GET", self.server + f"/api/v1/_noop_wait/{int(duration)}"
        )

        result = await response.json()
        return result

    @track_context
    async def _upload_performance_report(
        self,
        content: str,
        account: Optional[str] = None,
        filename: Optional[str] = None,
        private: bool = False,
    ) -> Dict:
        account = account or self.default_account

        data = aiohttp.MultipartWriter("form-data")
        part = data.append(open(content, "rb"))
        part.headers[
            aiohttp.hdrs.CONTENT_DISPOSITION
        ] = f'form-data; name="file"; filename="{filename}"; filename*="{filename}"'

        upload_type = "private" if private else "public"
        response = await self._do_request(
            "POST",
            f"{self.server}/api/v1/{account}/performance_reports/{upload_type}/",
            data=data,
        )

        if response.status >= 400:
            await handle_api_exception(response)

        result = await response.json()
        return result

    @overload
    def upload_performance_report(
        self: Cloud[Sync],
        content: str,
        account: Optional[str] = None,
        filename: Optional[str] = None,
        private: bool = False,
    ) -> Dict:
        ...

    @overload
    def upload_performance_report(
        self: Cloud[Async],
        content: str,
        account: Optional[str] = None,
        filename: Optional[str] = None,
        private: bool = False,
    ) -> Awaitable[Dict]:
        ...

    def upload_performance_report(
        self,
        content: str,
        account: Optional[str] = None,
        filename: Optional[str] = None,
        private: bool = False,
    ) -> Union[Dict, Awaitable[Dict]]:
        return self._sync(
            self._upload_performance_report,
            content,
            filename=filename,
            account=account,
            private=private,
        )

    @track_context
    async def _list_performance_reports(
        self,
        account: Optional[str] = None,
    ) -> List[Dict]:
        account = account or self.default_account
        response = await self._do_request(
            "GET",
            f"{self.server}/api/v1/{account}/performance_reports/all/",
        )
        if response.status >= 400:
            await handle_api_exception(response)

        result = await response.json()
        return result

    @overload
    def list_performance_reports(
        self: Cloud[Async],
        account: Optional[str] = None,
    ) -> Awaitable[List[Dict]]:
        ...

    @overload
    def list_performance_reports(
        self: Cloud[Sync],
        account: Optional[str] = None,
    ) -> List[Dict]:
        ...

    def list_performance_reports(
        self,
        account: Optional[str] = None,
    ) -> Union[List[Dict], Awaitable[List[Dict]]]:
        return self._sync(
            self._list_performance_reports,
            account=account,
        )

    @overload
    def list_user_information(self: Cloud[Sync]) -> dict:
        ...

    @overload
    def list_user_information(self: Cloud[Async]) -> Awaitable[dict]:
        ...

    def list_user_information(self) -> Union[Awaitable[dict], dict]:
        return self._sync(self._list_user_information)

    @track_context
    async def _list_user_information(
        self,
    ) -> dict:
        response = await self._do_request("GET", self.server + "/api/v1/users/me/")
        if response.status >= 400:
            await handle_api_exception(response)
        result = await response.json()

        return result

    @track_context
    async def _health_check(self) -> dict:
        response = await self._do_request("GET", self.server + "/api/v1/health")
        if response.status >= 400:
            await handle_api_exception(response)

        result = await response.json()
        return result

    @overload
    def health_check(self: Cloud[Sync]) -> dict:
        ...

    @overload
    def health_check(self: Cloud[Async]) -> Awaitable[dict]:
        ...

    def health_check(self) -> Union[Awaitable[dict], dict]:
        return self._sync(self._health_check)

    @track_context
    async def _get_billing_activity(
        self,
        account: Optional[str] = None,
        cluster: Optional[str] = None,
        cluster_id: Optional[int] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        kind: Optional[str] = None,
        page: Optional[int] = None,
    ) -> Dict:
        account = account or self.default_account
        params = {}
        if start_time:
            params["event_after"] = start_time
        if end_time:
            params["event_before"] = end_time
        if kind:
            params["kind"] = kind
        if cluster:
            params["cluster"] = cluster
        if cluster_id:
            params["cluster_id"] = cluster_id
        if page:
            params["page"] = page
        response = await self._do_request(
            "GET",
            f"{self.server}/api/v1/{account}/billing-events/",
            params=params,
        )
        if response.status >= 400:
            await handle_api_exception(response)

        result = await response.json()
        return result

    @overload
    def get_billing_activity(
        self: Cloud[Async],
        account: Optional[str] = None,
        cluster: Optional[str] = None,
        cluster_id: Optional[int] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        kind: Optional[str] = None,
        page: Optional[int] = None,
    ) -> Awaitable[Dict]:
        ...

    @overload
    def get_billing_activity(
        self: Cloud[Sync],
        account: Optional[str] = None,
        cluster: Optional[str] = None,
        cluster_id: Optional[int] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        kind: Optional[str] = None,
        page: Optional[int] = None,
    ) -> Dict:
        ...

    def get_billing_activity(
        self,
        account: Optional[str] = None,
        cluster: Optional[str] = None,
        cluster_id: Optional[int] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        kind: Optional[str] = None,
        page: Optional[int] = None,
    ) -> Union[Dict, Awaitable[Dict]]:
        return self._sync(
            self._get_billing_activity,
            account=account,
            cluster=cluster,
            start_time=start_time,
            end_time=end_time,
            kind=kind,
            page=page,
        )

    @track_context
    async def _add_interation(
        self,
        action: str,
        success: bool,
        version: int = 1,
        coiled_version: str = COILED_VERSION,
        error_message: Optional[str] = None,
        additional_text: Optional[str] = None,
        additional_data: Optional[dict] = None,
    ) -> None:
        data = {
            "action": action,
            "version": version,
            "success": success,
            "coiled_version": coiled_version[:30],  # dev version strings are long
            "error_message": error_message,
            "additional_text": additional_text,
            "additional_data": additional_data,
        }
        response = await self._do_request(
            "POST",
            f"{self.server}/api/v2/interactions/interaction",
            json=data,
        )
        if response.status >= 400:
            await handle_api_exception(response)

    @overload
    def add_interaction(
        self: Cloud[Async],
        action: str,
        success: bool,
        coiled_version: str = COILED_VERSION,
        version: int = 1,
        error_message: Optional[str] = None,
        additional_text: Optional[str] = None,
        additional_data: Optional[dict] = None,
    ) -> Coroutine[None, None, None]:
        ...

    @overload
    def add_interaction(
        self: Cloud[Sync],
        action: str,
        success: bool,
        coiled_version: str = COILED_VERSION,
        version: int = 1,
        error_message: Optional[str] = None,
        additional_text: Optional[str] = None,
        additional_data: Optional[dict] = None,
    ) -> None:
        ...

    def add_interaction(
        self,
        action: str,
        success: bool,
        coiled_version: str = COILED_VERSION,
        version: int = 1,
        error_message: Optional[str] = None,
        additional_text: Optional[str] = None,
        additional_data: Optional[dict] = None,
    ) -> Union[None, Coroutine[None, None, None]]:
        return self._sync(
            self._add_interation,
            action=action,
            version=version,
            success=success,
            coiled_version=coiled_version,
            error_message=error_message,
            additional_text=additional_text,
            additional_data=additional_data,
        )


# Utility functions for formatting list_* endpoint responses to be more user-friendly


def format_security_output(data, cluster_id, server, token):
    d = data.copy()
    scheme, _ = parse_address(d["public_address"])
    if scheme.startswith("ws"):
        address = f"{server.replace('http', 'ws')}/cluster/{cluster_id}/"
        d["public_address"] = address
        d["extra_conn_args"] = {
            "headers": {"Authorization": get_auth_header_value(token)}
        }
        d["dashboard_address"] = f"{server}/dashboard/{cluster_id}/status"
        d.pop("tls_key")
        d.pop("tls_cert")
    else:
        # can delete after backend no longer sends extra_conn_args
        d.pop("extra_conn_args", None)
    return d


def format_account_output(d):
    return d["slug"]


def format_software_environment_output(d):
    exclude_list = [
        "id",
        "name",
        "content_hash",
        "builds",
    ]
    d = {k: v for k, v in d.items() if k not in exclude_list}
    d["account"] = format_account_output(d["account"])
    return d


def format_cluster_output(d, server):
    d = d.copy()
    for key in ["auth_token", "name", "last_seen"]:
        d.pop(key)
    d["account"] = format_account_output(d["account"])
    # Rename "public_address" to "address"
    address = d.pop("public_address")
    scheme, _ = parse_address(address)
    if scheme.startswith("ws"):
        address = f"{server.replace('http', 'ws')}/cluster/{d['id']}/"
    d["address"] = address
    # Use proxied dashboard address if we're in a hosted notebook
    # or proxying through websockets
    if dask.config.get("coiled.dashboard.proxy", False) or scheme.startswith("ws"):
        d["dashboard_address"] = f"{server}/dashboard/{d['id']}/status"
    return d


# Public API


def create_api_token(
    *, label: Optional[str] = None, days_to_expire: Optional[int] = None
) -> dict:
    """Create a new API token.

    Parameters
    ---------
    label
        A label associated with the new API token, helpful for identifying it later.
    days_to_expire
        A number of days until the new API token expires.
    """
    with Cloud() as cloud:
        return cloud.create_api_token(
            label=label,
            days_to_expire=days_to_expire,
        )


def list_api_tokens(include_inactive=False) -> dict[str, dict]:
    """List your API tokens.

    Note that this does not provide the actual key value, which is only available when creating the key.

    Returns
    -------
    Dictionary with information about each API token for your account. Keys in the dictionary are the API tokens'
    identifiers of {kind}s, while the values contain information about the corresponding API token.
    """
    with Cloud() as cloud:
        return cloud.list_api_tokens(include_inactive=include_inactive)


def revoke_api_token(
    *, identifier: Optional[str] = None, label: Optional[str] = None
) -> None:
    """Revoke an API token. Note that this cannot be undone.

    Exactly one of ``identifier`` and ``label`` should be provided.

    Parameters
    ---------
    identifier
        The identifier of the API token.
    label
        The label of the API token(s) to revoke.
    """
    with Cloud() as cloud:
        return cloud.revoke_api_token(identifier=identifier, label=label)


def revoke_all_api_tokens() -> None:
    """Revoke all API tokens. Note that this cannot be undone."""
    with Cloud() as cloud:
        return cloud.revoke_all_api_tokens()


def create_software_environment(
    name: Optional[str] = None,
    *,
    account: Optional[str] = None,
    conda: Optional[Union[list, dict, str]] = None,
    pip: Optional[Union[list, str]] = None,
    container: Optional[str] = None,
    log_output=sys.stdout,
    post_build: Optional[Union[list, str]] = None,
    conda_env_name: Optional[str] = None,
    backend_options: Optional[Dict] = None,
    private: bool = False,
    force_rebuild: bool = False,
    environ: Optional[Dict] = None,
    use_entrypoint: bool = True,
) -> None:
    """Create a software environment

    Parameters
    ---------
    name
        Name of software environment. Name can't contain uppercase letters.
    account
        The account in which to create the software environment, if not given in the name.
    conda
        Specification for packages to install into the software environment using conda.
        Can be a list of packages, a dictionary, or a path to a conda environment YAML file.
    pip
        Packages to install into the software environment using pip.
        Can be a list of packages or a path to a pip requirements file.
    container
        Docker image to use for the software environment. Must be the name of a docker image
        on Docker hub. Defaults to ``coiled/default``.
    post_build
        List of commands or path to a local executable script to run after pip and conda packages
        have been installed.
    log_output
        Stream to output logs to. Defaults to ``sys.stdout``.
    conda_env_name
        Name of conda environment to install packages into. Note that this should *only* be used
        when specifying a non-default value for ``container`` *and* when the non-default Docker
        image used expects commands to run in a conda environment not named "coiled".
        Defaults to "coiled".
    backend_options
        Dictionary of backend specific options (e.g. ``{'region': 'us-east-2'}``). Any options
        specified with this keyword argument will take precedence over those stored in the
        ``coiled.backend-options`` configuration value.
    private
        Whether this software environment is private or public. Defaults to ``False``
    force_rebuild
        By default, if an existing software environment with the same name and dependencies already
        exists, a rebuild is aborted. If this is set to True, those checks are skipped and the
        environment will be rebuilt. Defaults to ``False``
    environ
        Dictionary of environment variables.
    use_entrypoint
        Whether to use (or override) entrypoint set on container.
    """
    error = False

    with Cloud() as cloud:
        try:
            return cloud.create_software_environment(
                name=name,
                account=account,
                conda=conda,
                pip=pip,
                container=container,
                post_build=post_build,
                log_output=log_output,
                conda_env_name=conda_env_name,
                backend_options=backend_options,
                private=private,
                force_rebuild=force_rebuild,
                environ=environ,
                use_entrypoint=use_entrypoint,
            )
        except Exception as e:
            error = e
            raise
        finally:
            data = {
                "error_class": error.__class__.__name__,
                "error_message": str(error),
                "name": str(name),
                "conda": bool(conda),
                "account": account,
                "pip": bool(pip),
                "container": container,
                "post_build": bool(post_build),
                "conda_env_name": bool(conda_env_name),
                "private": bool(private),
                "environ": bool(environ),
                "use_entrypoint": bool(use_entrypoint),
            }
            if error:
                cloud.add_interaction(
                    "create-software-environment",
                    success=False,
                    additional_data=data,
                )
            else:
                cloud.add_interaction(
                    "create-software-environment",
                    success=True,
                    additional_data=data,
                )


@list_docstring
def list_software_environments(account=None):
    with Cloud() as cloud:
        return cloud.list_software_environments(account=account)


@delete_docstring
def delete_software_environment(name, account: Optional[str] = None):
    with Cloud() as cloud:
        return cloud.delete_software_environment(name=name, account=account)


def get_software_info(name: str, account: Optional[str] = None) -> dict:
    """Retrieve solved spec for a Coiled software environment

    Parameters
    ----------
    name
        Software environment name

    Returns
    -------
    results
        Coiled software environment information
    """
    with Cloud() as cloud:
        return cloud.get_software_info(name=name, account=account)


def list_core_usage(account: Optional[str] = None) -> dict:
    """Get a list of used cores.

    Returns a table that shows the limit of cores that the user can use
    and a breakdown of the core usage split up between account, user and clusters.

    Parameters
    ----------
    account
        Name of the Coiled account to list core usage. If not provided,
        will use the coiled.account configuration value.
    json
        If set to ``True``, it will return this list in json format instead of
        a table.
    """
    with Cloud() as cloud:
        return cloud.list_core_usage(account=account)


def get_notifications(
    json: bool = False,
    account: Optional[str] = None,
    limit: int = 100,
    level: Union[int, str] = logging.NOTSET,
    event_type: Optional[event_type_list] = None,
) -> Union[List[dict], None]:
    """Get a list of all recent notifications.

    Parameters
    ----------
    account
        Name of the Coiled account to list notifications. If not provided,
        will use the coiled.account configuration value.
    json
        If set to ``True``, it will return this list in json format instead of
        a table.
    limit
        The max number of notifications to return.
    level
        A constant from the standard python logging library (e.g., ``logging.INFO``),
        or a string of one of the following: ``debug``, ``info``, ``warning``, ``error``,
        or ``critical``. This will be used to filter the returned notifications.
    event_type
        The event_type that you wish to get notifications for. For example, you might want
        to see only ``vm_event`` types.
    """
    with Cloud() as cloud:
        return cloud.get_notifications(
            json=json, account=account, limit=limit, level=level, event_type=event_type
        )


def list_local_versions() -> dict:
    """Get information about local versions.

    Returns the versions of Python, Coiled, Dask and Distributed that
    are installed locally. This information could be useful when
    troubleshooting issues.

    Parameters
    ----------
    json
        If set to ``True``, it will return this list in json format instead of a
        table.
    """
    with Cloud() as cloud:
        return cloud.list_local_versions()


def diagnostics(account: Optional[str] = None) -> dict:
    """Run a diagnose check aimed to help support with any issues.

    This command will call others to dump information that could help
    in troubleshooting issues. This command will return a json that will
    make it easier for you to share with the Coiled support team if needed.

    Parameters
    ----------
    account
        Name of the Coiled account to list core usage. If not provided,
        will use the coiled.account configuration value.
    """
    console = rich_console()
    with console.status("Gathering diagnostics..."):
        with Cloud() as cloud:
            data = {}

            health_check = cloud.health_check()
            status = health_check.get("status", "Issues found")

            data["health_check"] = health_check
            console.print(f"Performing health check.... Status: {status}")
            time.sleep(0.5)

            console.print("Gathering information about local environment...")
            local_versions = cloud.list_local_versions()
            data["local_versions"] = local_versions
            time.sleep(0.5)

            configuration = dask.config.config
            configuration["coiled"]["token"] = "hidden"
            data["coiled_configuration"] = configuration
            time.sleep(0.5)

            console.print("Getting user information...")
            user_info = cloud.list_user_information()
            data["user_information"] = user_info
            time.sleep(0.5)

            usage = cloud.list_core_usage(account=account)
            data["core_usage"] = usage
            time.sleep(0.5)

            notifications = cloud.get_notifications(json=True, account=account)
            data["notifications"] = notifications

            return data


def list_user_information() -> dict:
    """List information about your user.

    This command will give you more information about your account,
    which teams you are part of and any limits that your account might
    have.
    """
    with Cloud() as cloud:
        cloud.list_user_information()
        return cloud.list_user_information()


def _upload_report(filename, private=False, account=None) -> dict:
    """Private method for uploading report to Coiled"""
    if not os.path.isfile(filename):
        raise ValueError("Report file does not exist.")

    statinfo = os.stat(filename)
    max_mb = 50
    if statinfo.st_size >= 1048576 * max_mb:
        raise ValueError(f"Report file size greater than {max_mb}mb limit")

    # At this point Dask has generated a local file with the performance report contents
    with Cloud() as cloud:
        result = cloud.upload_performance_report(
            filename, filename=filename, private=private, account=account
        )
        return result


@dataclass
class PerformanceReportURL:
    url: Optional[str]


@experimental
@contextmanager
def performance_report(
    filename="dask-report.html",
    private=False,
    account=None,
) -> Generator[PerformanceReportURL, None, None]:
    """Generates a static performance report and saves it to Coiled Cloud

    This context manager lightly wraps Dask's performance_report. It generates a static performance
    report and uploads it to Coiled Cloud. After uploading, it prints out the url where the report is
    hosted. For a list of hosted performance reports, utilize coiled.list_performance_reports(). Note
    each user is limited to 5 hosted reports with each a maximum file size of 10mb.

    The context manager yields an object that will have the url as an attribute,
    though the URL is not available inside the context but only after (see example).

    Example::

        with coiled.performance_report("filename") as perf_url:
            dask.compute(...)

        assert isinstance(perf_url["url"], str)


    Parameters
    ----------

    filename
        The file name of the performance report file.
    private
        If set to ``True``, the uploaded performance report is only accessible to logged in Coiled users who
        are members of the current / default or specified account.
    account
        Associated the account which user wishes to upload to. If not specified, current / default
        account will be utilized.

    """
    perf_url = PerformanceReportURL(None)
    # stacklevel= is newer kwarg after version check below
    try:
        report_kwargs = {"stacklevel": 3} if DISTRIBUTED_VERSION >= "2021.05.0" else {}
        with dask.distributed.performance_report(filename=filename, **report_kwargs):
            yield perf_url
    except Exception as ex:
        raise Exception(
            "Exception in coiled.performance_report() context"
        ).with_traceback(ex.__traceback__)
    finally:
        # by this point dask will have written local file as <filename>
        results = _upload_report(filename, private=private, account=account)
        console = Console()
        perf_url.url = results["url"]
        text = Text(
            f'Performance Report Available at: {results["url"]}',
            style=f"link {results['url']}",
        )
        console.print(text)


@experimental
def list_performance_reports(account=None) -> List[Dict]:
    """List performance reports stored on Coiled Cloud

    Returns a list of dicts that contain information about Coiled Cloud hosted performance reports

    Parameters
    ----------

    account
        Associated account for which the user wishes to get reports from. If not specified, current / default
        account will be utilized.

    """
    with Cloud() as cloud:
        result = cloud.list_performance_reports(account=account)
        return result


def _parse_gcp_creds(
    gcp_service_creds_dict: Optional[Dict], gcp_service_creds_file: Optional[str]
) -> Dict:
    if not any([gcp_service_creds_dict, gcp_service_creds_file]):
        raise GCPCredentialsParameterError(
            "Parameter 'gcp_service_creds_file' or 'gcp_service_creds_dict' must be supplied"
        )

    if gcp_service_creds_file:
        if not os.path.isfile(gcp_service_creds_file):
            raise GCPCredentialsError(
                "The parameter 'gcp_service_creds_file' must be a valid file"
            )
        try:
            with open(gcp_service_creds_file, "r") as json_file:
                creds = json.load(json_file)

                required_keys = [
                    "type",
                    "project_id",
                    "private_key_id",
                    "private_key",
                    "client_email",
                    "client_id",
                    "auth_uri",
                    "token_uri",
                    "auth_provider_x509_cert_url",
                    "client_x509_cert_url",
                ]
                missing_keys = [key for key in required_keys if key not in creds]
                if missing_keys:
                    raise GCPCredentialsError(
                        message=(
                            f"The supplied file '{gcp_service_creds_file}' is missing the keys: "
                            f"{', '.join(missing_keys)}"
                        )
                    )

                return creds
        except JSONDecodeError:
            raise GCPCredentialsError(
                f"The supplied file '{gcp_service_creds_file}' is not a valid JSON file."
            )
    if gcp_service_creds_dict and not gcp_service_creds_dict.get("project_id"):
        raise GCPCredentialsError(
            "Unable to find 'project_id' in 'gcp_service_creds_dict', make sure this key exists in the dictionary"
        )

    # Type checker doesn't know that this should no longer
    # be None.
    return cast(Dict, gcp_service_creds_dict)


def set_backend_options(
    account: Optional[str] = None,
    backend: Literal["aws", "gcp"] = "aws",
    ingress: Optional[List[Dict]] = None,
    firewall: Optional[Dict] = None,
    network: Optional[Dict] = None,
    aws_region: str = "us-east-1",
    aws_access_key_id: Optional[str] = None,
    aws_secret_access_key: Optional[str] = None,
    gcp_service_creds_file: Optional[str] = None,
    gcp_service_creds_dict: Optional[dict] = None,
    gcp_project_id: Optional[str] = None,
    gcp_region: Optional[str] = None,
    gcp_zone: Optional[str] = None,
    instance_service_account: Optional[str] = None,
    zone: Optional[str] = None,
    registry_type: Literal["ecr", "docker_hub", "gar"] = "ecr",
    registry_namespace: Optional[str] = None,
    registry_access_token: Optional[str] = None,
    registry_uri: str = "docker.io",
    registry_username: Optional[str] = None,
    log_output=sys.stdout,
    **kwargs,
):
    """Configure account level settings for cloud provider and container registry.

    This method configures account level backend settings for cloud providers, container registries,
    and setting up an account-level VPC for running clusters and other Coiled managed resources.


    Parameters
    ----------

    account
        Coiled account to configure if user has access. If not specified, current / default
        account will be utilized.

    backend
        Supported backends such as AWS VM (aws) and GCP VM (gcp).

    ingress
        Specification of the ingress rules the firewall/security group that Coiled creates for the cluster scheduler.
        This is a list of ingress rules, each rule is a dictionary with a list of ports and a CIDR block from which to
        allow ingress on those ports to the scheduler. For example,
        ``[{"ports" [8787], "cidr": "0.0.0.0/0"}, {"ports" [8786], "cidr": "10.2.0.0/16"}]``
        would allow the dashboard on 8787 to be accessed from any IP address, and the scheduler comm on 8786 to only
        be accessed from IP addresses in the 10.2.0.0/16 local network block.

    firewall
        A single ingress rule for the scheduler firewall/security group; this is deprecated and ingress rules should be
        specified with ``ingress`` instead.

    network
        Specification for your network/subnets, dictionary can take ID(s) for existing network and/or subnet(s).

    aws_region
        The region which Coiled cloud resources will be deployed to and where other resources
        such as the docker registry are located or where a specified VPC will be created.

    aws_access_key_id
        For AWS support backend, this argument is required to create or use an existing Coiled managed VPC.

    aws_secret_access_key
        For AWS support backend, this argument is required to create or use an existing Coiled managed VPC.

    use_scheduler_public_ip
        Determines if the client connects to the Dask scheduler using it's public or internal address.

    gcp_service_creds_file
        A string filepath to a Google Cloud Compute service account json credentials file used for creating and
        managing a Coiled VPC.

    gcp_service_creds_dict
        A dictionary of the contents of a Google Cloud Compute service account json credentials file used for
        creating a VPC to host Coiled Cloud related assets.

    gcp_project_id
        The Google Cloud Compute project id in which a VPC will be created to host Coiled Cloud related assets.

    gcp_region
        The Google Cloud Compute region name in which a VPC will be created.

    instance_service_account
        Email for optional service account to attach to cluster instances; using this is the best practice
        for granting access to your data stored in Google Cloud services. This
        should be a scoped service instance with only the permissions needed to run
        your computations.

    zone
        Optional; used to specify zone to use for clusters (for either AWS or GCP).

    registry_type
        Custom software environments are stored in a docker container registry. By default, container images will be
        stored in AWS ECR. Users are able to store contains on a private registry by providing additional
        configuration registry_* arguments and specifying registry_type='docker_hub'. To use
        Google Artifact Registry, pass registry_type='gar', gcp_project_id, gcp_region,
        and one of gcp_service_creds_dict or gcp_service_creds_file.

    registry_uri
        The container registry URI. Defaults to docker.io. Only required if
        registry_type='docker_hub'.

    registry_username
        A registry username (should be lowercased). Only required if
        registry_type='docker_hub'.

    registry_namespace
        A namespace for storing the container images. Defaults to username if not specified. More information
        about docker namespaces can be found here: https://docs.docker.com/docker-hub/repos/#creating-a-repository.
        Only required if registry_type='docker_hub'.

    registry_access_token
        A token to access registry images. More information about access tokens ca be found here:
        https://docs.docker.com/docker-hub/access-tokens/. Only required if registry_type='docker_hub'.

    """
    if firewall:
        if ingress:
            raise ValueError(
                "You specified both `firewall` and `ingress`. These are redundant; you should use `ingress`."
            )
        else:
            logger.warning(
                "The `firewall` keyword argument is deprecated; in the future you should use\n"
                f"  ingress=[{{ {firewall} }}]\n"
                "to specify your desired firewall ingress rules."
            )
            ingress = [firewall]
    firewall_spec = {"ingress": ingress} if ingress else {}

    # TODO - see if way to add default in BE to avoid re-versioning of this
    backend_options = {
        "backend": "vm_aws",
        "options": {
            "aws_region_name": aws_region,
            "account_role": "",
            "credentials": {"aws_access_key_id": "", "aws_secret_access_key": ""},
            "firewall": {},
            "firewall_spec": firewall_spec,
            "network": network or {},
            "zone": zone,
        },
        "registry": {"type": "ecr", "credentials": {}, "public_ecr": False},
    }

    # override gcp_zone with zone, if set
    if zone and gcp_project_id:
        gcp_zone = zone

    output_msg = ""
    # Used to print warnings to the user
    console = Console()

    if backend not in SUPPORTED_BACKENDS:
        raise UnsupportedBackendError(
            f"Supplied backend: {backend} not in supported types: {SUPPORTED_BACKENDS}"
        )

    if aws_access_key_id and aws_secret_access_key:
        # verify that these are valid credentials
        verify_aws_credentials(aws_access_key_id, aws_secret_access_key)

    parsed_gcp_credentials: Optional[Dict] = None

    # Parse GCP region/zones or return default region/zone
    gcp_region, gcp_zone = parse_gcp_region_zone(region=gcp_region, zone=gcp_zone)

    if backend == "aws":
        backend_options["backend"] = "vm"
        backend_options["options"]["aws_region_name"] = aws_region
        if aws_access_key_id and aws_secret_access_key:
            backend_options["options"]["credentials"] = {
                "aws_access_key": aws_access_key_id,
                "aws_secret_key": aws_secret_access_key,
            }

            backend_options["options"]["provider_name"] = "aws"
            backend_options["options"]["type"] = "aws_cloudbridge_backend_options"
            output_msg = "Successfully set your backend options to Coiled Customer Hosted on AWS VM."
        else:
            raise AWSCredentialsParameterError(
                "Setting up AWS backend requires both: aws_access_key_id and aws_secret_access_key."
            )
    elif backend == "gcp":
        parsed_gcp_credentials = _parse_gcp_creds(
            gcp_service_creds_dict=gcp_service_creds_dict,
            gcp_service_creds_file=gcp_service_creds_file,
        )
        if not gcp_project_id:
            gcp_project_id = parsed_gcp_credentials.get("project_id", "")
        backend_options["options"]["gcp_service_creds_dict"] = parsed_gcp_credentials

        backend_options["backend"] = "vm"

        backend_options["options"]["provider_name"] = "gcp"
        backend_options["options"]["type"] = "gcp_cloudbridge_backend_options"

        backend_options["options"]["gcp_project_name"] = gcp_project_id
        backend_options["options"]["gcp_region_name"] = gcp_region
        backend_options["options"]["gcp_zone_name"] = gcp_zone
        backend_options["options"][
            "instance_service_account"
        ] = instance_service_account

        output_msg = (
            "Successfully set your backend options to Coiled Customer Hosted on GCP VM."
        )

    ### container registry
    if registry_type == "ecr":
        # TODO add aws credentials in here for VPCs
        backend_options["registry"]["region"] = aws_region
        if aws_access_key_id and aws_secret_access_key:
            backend_options["registry"]["credentials"][
                "aws_access_key_id"
            ] = aws_access_key_id
            backend_options["registry"]["credentials"][
                "aws_secret_access_key"
            ] = aws_secret_access_key

    elif registry_type == "docker_hub":
        registry = {
            "account": registry_namespace or registry_username,
            "password": registry_access_token,
            "type": registry_type,
            "uri": registry_uri,
            "username": registry_username,
        }

        # any missing values
        empty_registry_values = [f"registry_{k}" for k, v in registry.items() if not v]
        if any(empty_registry_values):
            raise RegistryParameterError(
                f"For setting your registry credentials, these fields cannot be empty: {empty_registry_values}"
            )

        # docker username /// account name cannot be uppercase
        if (
            registry_username
            and any(ele.isupper() for ele in registry_username) is True
        ):
            raise RegistryParameterError(
                "Your dockerhub [registry_username] must be lowercase"
            )

        backend_options["registry"] = registry
    elif registry_type == "gar":
        if parsed_gcp_credentials is None:
            parsed_gcp_credentials = _parse_gcp_creds(
                gcp_service_creds_dict=gcp_service_creds_dict,
                gcp_service_creds_file=gcp_service_creds_file,
            )
        if not gcp_project_id:
            gcp_project_id = parsed_gcp_credentials.get("project_id", "")
        gar_required_kwargs = {
            "gcp_region_name": gcp_region,
            "gcp_project_name": gcp_project_id,
            "one of gcp_service_creds_dict / gcp_service_creds_file": parsed_gcp_credentials,
        }
        missing_gar_kwargs = ", ".join(
            [kw for kw, val in gar_required_kwargs.items() if not val]
        )
        if missing_gar_kwargs:
            raise RegistryParameterError(
                f"Missing required args for Google Artifact Registry: {missing_gar_kwargs}"
            )
        backend_options["registry"] = {
            "type": registry_type,
            "location": gcp_region,
            "project_id": gcp_project_id,
            "credentials": parsed_gcp_credentials,
        }

    with Cloud(account=account) as cloud:
        account_options_url = cloud.set_backend_options(
            backend_options,
            account=account,
            log_output=log_output,
        )
        text = Text()
        text.append(output_msg, style="green")
        text.append("\n\n")
        text.append(
            f"Please confirm your account backend options here: {account_options_url}",
            style=f"link {account_options_url}",
        )
        console.print(text)


def list_instance_types(
    backend: Optional[str] = None,
    min_cores: Optional[int] = None,
    min_gpus: Optional[int] = None,
    min_memory: Optional[Union[int, str, float]] = None,
    cores: Optional[Union[int, list[int]]] = None,
    memory: Optional[Union[int, str, float, list[int], list[str], list[float]]] = None,
    gpus: Optional[Union[int, list[int]]] = None,
) -> dict[str, VmType]:
    """List allowed instance types for the cloud provider configured on your account.

    This command allows you to get all instance types available for a backend or a filtered
    list of instance types that match your requirements by using the available keyword
    arguments. Please refer to :doc:`tutorials/select_instance_types` for more information.

    Parameters
    ----------
    backend:
        Relevant cloud provider (aws or gcp) to get a list of allowed instance types. If
        not provided the list will show the instances for your account cloud provider.
    min_cores
        Filter results on the minimum number of required cores
    min_gpus
        Filter results on the minimum number of required GPUs
    min_memory
        Filter results on the minimum amount of memory
    cores:
        The exact number of cores to filter for example ``cores=1`` or a list containg the
        minimum and maximum amount of cores to filter instances by, for example ``cores=[2,8]``.
    memory:
        The exact amount of memory or a list containing the minimum and maximum
        amount of memory to filter instances by.
    gpus
        The exaxct number of gpus to filter or a list containing the minimum and maximum number
        of GPUS to filter instances by.
    """
    with Cloud() as cloud:
        return cloud.list_instance_types(
            backend=backend,
            min_cores=min_cores,
            min_gpus=min_gpus,
            min_memory=min_memory,
            cores=cores,
            memory=memory,
            gpus=gpus,
        )


def list_gpu_types() -> Dict:
    """List allowed GPU Types.

    For AWS the GPU types are tied to the instance type, but for GCP you can
    add different GPU types to GPU enabled instances. Please refer to
    :doc:`gpu` for more information.

    Parameters
    ----------
    json
        if set to ``True``, it will return this list in json format instead of a table.

    """
    with Cloud() as cloud:
        return cloud.list_gpu_types()


BillingEventKind = Literal[
    "instance",
    "monthly_grant",
    "manual_adjustment",
    "payg_payment",
]


def get_billing_activity(
    account: Optional[str] = None,
    cluster: Optional[str] = None,
    cluster_id: Optional[int] = None,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    kind: Optional[BillingEventKind] = None,
    page: Optional[int] = None,
) -> Dict:
    """Retrieve Billing information.

    Parameters
    ----------
    account
        The account to retrieve billing information from.
        If not provided, will default to ``Cloud.account`` configuration  value.

    cluster
        Cluster name. Filter billing events to this cluster. Defaults to ``None``.

    cluster_id
        Cluster id. Filter billing events to this cluster by id. Defaults to ``None``.

    start_time
        Filter events after this datetime (isoformat). Defaults to ``None``.

    end_time
        Filter events before this datetime (isoformat). Defaults to ``None``.

    kind
        Filter events to this kind of event. Defaults to ``None``.

    page
       Grab events from this page. Defaults to ``None``.
    """
    with Cloud() as cloud:
        return cloud.get_billing_activity(
            account=account,
            cluster=cluster,
            cluster_id=cluster_id,
            start_time=start_time,
            end_time=end_time,
            kind=kind,
            page=page,
        )


def add_interaction(
    action: str,
    *,
    success: bool,
    error_message: Optional[str] = None,
    additional_text: Optional[str] = None,
    **kwargs,
):
    with Cloud() as cloud:
        return cloud.add_interaction(
            action=action,
            success=success,
            error_message=error_message,
            additional_text=additional_text,
            additional_data=kwargs or None,
        )
