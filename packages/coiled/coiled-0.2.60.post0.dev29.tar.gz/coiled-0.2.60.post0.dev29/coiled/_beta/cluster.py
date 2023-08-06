from __future__ import annotations

import asyncio
import contextlib
import datetime
import logging
import re
import sys
import time
import uuid
import warnings
import weakref
from asyncio import wait_for
from contextlib import suppress
from copy import deepcopy
from os import environ
from pathlib import Path
from typing import (
    Awaitable,
    Callable,
    Dict,
    Generic,
    Iterable,
    List,
    Optional,
    Set,
    Tuple,
    TypeVar,
    Union,
    cast,
    overload,
)

import botocore
import dask
import dask.distributed
import distributed
import tlz as toolz
from dateutil import tz
from distributed.core import Status
from distributed.deploy.adaptive import Adaptive
from typing_extensions import Literal

from coiled import magic
from coiled.cluster import CoiledAdaptive, CredentialsPreferred
from coiled.compatibility import DISTRIBUTED_VERSION
from coiled.context import track_context
from coiled.core import IsAsynchronous
from coiled.errors import ClusterCreationError, DoesNotExist
from coiled.exceptions import ArgumentCombinationError, InstanceTypeError
from coiled.types import PackageLevel
from coiled.utils import (
    COILED_LOGGER_NAME,
    GCP_SCHEDULER_GPU,
    cluster_firewall,
    get_details_url,
    get_grafana_url,
    get_instance_type_from_cpu_memory,
    name_to_version,
    parse_identifier,
    parse_wait_for_workers,
    validate_vm_typing,
)

from ..core import Async, AWSSessionCredentials, Sync
from .core import (
    AWSOptions,
    CloudBeta,
    GCPOptions,
    log_cluster_debug_info,
    setup_logging,
)
from .cwi_log_link import cloudwatch_url
from .states import (
    ClusterStateEnum,
    InstanceStateEnum,
    ProcessStateEnum,
    flatten_log_states,
    log_states,
    summarize_status,
)
from .widgets import EXECUTION_CONTEXT, HAS_RICH

logger = logging.getLogger(COILED_LOGGER_NAME)

_T = TypeVar("_T")


def use_rich_widget():
    return EXECUTION_CONTEXT in ["ipython_terminal", "notebook"] and HAS_RICH


BEHAVIOR_TO_LEVEL = {"critical-only": 100, "warning-or-higher": 50, "any": 0}


class ClusterBeta(distributed.deploy.Cluster, Generic[IsAsynchronous]):
    """Create a Dask cluster with Coiled

    Parameters
    ----------
    n_workers
        Number of workers in this cluster. Defaults to 4.
    name
        Name to use for identifying this cluster. Defaults to ``None``.
    software
        Name of the software environment to use.
    worker_class
        Worker class to use. Defaults to :class:`distributed.nanny.Nanny`.
    worker_options
        Mapping with keyword arguments to pass to ``worker_class``. Defaults
        to ``{}``.
    worker_vm_types
        List of instance types that you would like workers to use, default instance type
        selected contains 2 cores. You can use the command ``coiled.list_instance_types()``
        to see a list of allowed types.
    worker_cpu
        Number, or range, of CPUs requested for each worker. Specify a range by
        using a list of two elements, for example: ``worker_cpu=[2, 8]``.
    worker_memory
        Amount of memory to request for each worker, Coiled will use a +/- 10% buffer
        from the memory that you specify. You may specify a range of memory by using a
        list of two elements, for example: ``worker_memory=["2GiB", "4GiB"]``.
    worker_disk_size
        Non-default size of persistent disk attached to each worker instance, specified
        in GB.
    worker_gpu
        For instance types that don't come with a fixed number of GPUs, the number of
        GPUs to attach. This only applies to GCP, and will default to 1 if you specify
        ``worker_gpu_type``. Coiled currently only supports a single GPU per instance.
    worker_gpu_type
        For instance types that don't always come with GPU, the type of GPU to attach.
        This only applied to GCP. Should match the way the cloud provider specifies the
        GPU, for example: ``worker_gpu_type="nvidia-tesla-t4"``.
    scheduler_class
        Scheduler class to use. Defaults to :class:`distributed.scheduler.Scheduler`.
    scheduler_options
        Mapping with keyword arguments to pass to ``scheduler_class``. Defaults
        to ``{}``.
    scheduler_vm_types
        List of instance types that you would like the scheduler to use, default instances
        type selected contains 2 cores. You can use the command
        ``coiled.list_instance_types()`` to se a list of allowed types.
    scheduler_cpu
        Number, or range, of CPUs requested for the scheduler. Specify a range by
        using a list of two elements, for example: ``scheduler_cpu=[2, 8]``.
    scheduler_memory
        Amount of memory to request for the scheduler, Coiled will use a +/-10%
        buffer from the memory what you specify. You may specify a range of memory by using a
        list of two elements, for example: ``scheduler_memory=["2GiB", "4GiB"]``.
    scheduler_gpu
        Whether to attach GPU to scheduler. This will affect instance type (if not specified explicitly).
        For Google Cloud, it will also add a single "guest" T4 to the scheduler.
        It's recommended to use GPU on scheduler for GPU clusters.
    asynchronous
        Set to True if using this Cloud within ``async``/``await`` functions or
        within Tornado ``gen.coroutines``. Otherwise this should remain
        ``False`` for normal use. Default is ``False``.
    cloud
        Cloud object to use for interacting with Coiled. This object contains user/authentication/account
        information. If this is None (default), we look for a recently-cached Cloud object, and if none
        exists create one.
    account
        Name of Coiled account to use. If not provided, will
        default to the user account for the ``cloud`` object being used.
    shutdown_on_close
        Whether or not to shut down the cluster when it finishes.
        Defaults to True, unless name points to an existing cluster.
    use_scheduler_public_ip
        Boolean value that determines if the Python client connects to the
        Dask scheduler using the scheduler machine's public IP address. The
        default behaviour when set to True is to connect to the scheduler
        using its public IP address, which means traffic will be routed over
        the public internet. When set to False, traffic will be routed over
        the local network the scheduler lives in, so make sure the scheduler
        private IP address is routable from where this function call is made
        when setting this to False.
    credentials
        Which credentials to use for Dask operations and forward to Dask
        clusters -- options are "local", or None. The default
        behavior is to use local credentials if available.
        NOTE: credential handling currently only works with AWS credentials.
    credentials_duration_seconds
        For "local" credentials shipped to cluster as STS token, set the duration of STS token.
        If not specified, the AWS default will be used.
    timeout
        Timeout in seconds to wait for a cluster to start, will use
        ``default_cluster_timeout`` set on parent Cloud by default.
    environ
        Dictionary of environment variables.
    send_dask_config
        Whether to send a frozen copy of local dask.config to the cluster.
    backend_options
        Dictionary of backend specific options.
    tags
        Dictionary of tags.
    wait_for_workers
        Whether to wait for a number of workers before returning control
        of the prompt back to the user. Usually, computations will run better
        if you wait for most workers before submitting tasks to the cluster.
        You can wait for all workers by passing ``True``, or not wait for any
        by passing ``False``. You can pass a fraction of the total number of
        workers requested as a float(like 0.6), or a fixed number of workers
        as an int (like 13). If None, the value from ``coiled.wait-for-workers``
        in your Dask config will be used. Default: 0.3. If the requested number
        of workers don't launch within 10 minutes, the cluster will be shut
        down, then a TimeoutError is raised.
    package_sync
        Attempt to synchronize package versions between your local environment and the cluster.
        Cannot be used with the `software` option. Passing `True` will sync all packages (recommended).
        Passing specific packages as a list of strings will attempt to synchronize only those packages,
        use with caution.
        We strongly recommend reading the additional documentation
        for this feature (see https://docs.coiled.io/user_guide/package_sync.html)!
    package_sync_strict
        Only allow exact packages matches, not recommended unless your client platform/architecture
        matches the cluster platform/architecture
    private_to_creator
        Only allow the cluster creator, not other members of team account, to connect to this cluster.
    use_best_zone
        Allow the cloud provider to pick the zone (in your specified region) that has best availability
        for your requested instances. We'll keep the scheduler and workers all in a single zone in
        order to avoid any interzone network traffic (which would be billed).
    compute_purchase_option
        Purchase option to use for workers in your cluster, options are "on-demand", "spot", and
        "spot_with_fallback". (Google Cloud refers to this as "provisioning model" for your instances.)
        **Spot instances** are much cheaper, but can have more limited availability and may be terminated
        while you're still using them if the cloud provider needs more capacity for other customers.
        **On-demand instances** have the best availability and are almost never
        terminated while still in use, but they're significantly more expensive than spot instances.
        For most workloads, "spot_with_fallback" is a good option: Coiled will try to get as many spot
        instances as we can, and if we get less than you requested, we'll try to get the remaining
        instances as on-demand.
        For AWS, when we're notified that an active spot instance is going to be terminated,
        we'll attempt to get a replacement instance (spot if available, but could be on-demand if you've
        enabled "fallback"). Dask on the active instance will attempt a graceful shutdown before the
        instance is terminated so that computed results won't be lost.
    scheduler_port
        Specify a port other than the default (8786) for communication with Dask scheduler; this is useful
        if your client is on a network that blocks 8786.
    allow_ingress_from
        Control the CIDR from which cluster firewall allows ingress to scheduler; by default this is open
        to any source address (0.0.0.0/0). You can specify CIDR, or "me" for just your IP address.
    allow_ssh
        Allow connections to scheduler over port 22, used for SSH.
    """

    _instances = weakref.WeakSet()

    def __init__(
        self,
        name: Optional[str] = None,
        *,
        software: Optional[str] = None,
        n_workers: int = 4,
        worker_class: Optional[str] = None,
        worker_options: Optional[dict] = None,
        worker_vm_types: Optional[list] = None,
        worker_cpu: Optional[Union[int, List[int]]] = None,
        worker_memory: Optional[Union[str, List[str]]] = None,
        worker_disk_size: Optional[int] = None,
        worker_gpu: Optional[int] = None,
        worker_gpu_type: Optional[str] = None,
        scheduler_class: Optional[str] = None,
        scheduler_options: Optional[dict] = None,
        scheduler_vm_types: Optional[list] = None,
        scheduler_cpu: Optional[Union[int, List[int]]] = None,
        scheduler_memory: Optional[Union[str, List[str]]] = None,
        scheduler_gpu: Optional[bool] = None,
        asynchronous: bool = False,
        cloud: Optional[CloudBeta] = None,
        account: Optional[str] = None,
        shutdown_on_close=None,
        use_scheduler_public_ip: Optional[bool] = None,
        credentials: Optional[str] = "local",
        credentials_duration_seconds: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
        environ: Optional[Dict[str, str]] = None,
        tags: Optional[Dict[str, str]] = None,
        send_dask_config: bool = True,
        backend_options: Optional[
            Union[AWSOptions, GCPOptions]
        ] = None,  # intentionally not in the docstring yet
        show_widget: bool = True,
        configure_logging: bool = False,
        wait_for_workers: Optional[Union[int, float, bool]] = None,
        package_sync: Union[bool, List[str]] = False,
        package_sync_strict: bool = False,
        package_sync_fail_on: Literal[
            "critical-only", "warning-or-higher", "any"
        ] = "critical-only",
        private_to_creator: Optional[bool] = None,
        use_best_zone: bool = True,
        compute_purchase_option: Optional[
            Literal["on-demand", "spot", "spot_with_fallback"]
        ] = None,
        # easier network config
        scheduler_port: Optional[int] = None,
        allow_ingress_from: Optional[str] = None,
        allow_ssh: Optional[bool] = None,
    ):
        # NOTE:
        # this attribute is only updated while we wait for cluster to come up
        self.errored_worker_count: int = 0
        self.init_time = datetime.datetime.now()
        type(self)._instances.add(self)
        if package_sync and software:
            raise ValueError(
                "Both parameters 'software' and 'package_sync'"
                "were passed. Please only pass one"
            )
        self.package_sync = bool(
            package_sync
        )  # TODO: this should be mutually exclusive with passing a software env
        if isinstance(package_sync, list):
            # ensure python is always included
            self.package_sync_only = set(package_sync)
            self.package_sync_only.add("python")
        else:
            self.package_sync_only = None
        self.package_sync_strict = package_sync_strict
        self.package_sync_fail_on = BEHAVIOR_TO_LEVEL[package_sync_fail_on]
        self.show_widget = show_widget
        self._cluster_status_logs = []
        if configure_logging:
            setup_logging()

        # Determine consistent sync/async
        if cloud and asynchronous is not None and cloud.asynchronous != asynchronous:
            warnings.warn(
                f"Requested a Cluster with asynchronous={asynchronous}, but "
                f"cloud.asynchronous={cloud.asynchronous}, so the cluster will be"
                f"{cloud.asynchronous}"
            )

            asynchronous = cloud.asynchronous

        self.scheduler_comm: Optional[dask.distributed.rpc] = None

        # It's annoying that the user must pass in `asynchronous=True` to get an async Cluster object
        # But I can't think of a good alternative right now.
        self.cloud: CloudBeta[IsAsynchronous] = cloud or CloudBeta.current(
            asynchronous=asynchronous
        )
        # if cloud:
        #     self.cleanup_cloud = False
        #     self.cloud: CloudBeta[IsAsynchronous] = cloud
        # else:
        #     self.cleanup_cloud = True
        #     self.cloud: CloudBeta[IsAsynchronous] = CloudBeta(asynchronous=asynchronous)

        # As of distributed 2021.12.0, deploy.Cluster has a ``loop`` attribute on the
        # base class. We add the attribute manually here for backwards compatibility.
        # TODO: if/when we set the minimum distributed version to be >= 2021.12.0,
        # remove this check.
        if DISTRIBUTED_VERSION >= "2021.12.0":
            kwargs = {"loop": self.cloud.loop}
        else:
            kwargs = {}
            self.loop = self.cloud.loop

        # we really need to call this first before any of the below code errors
        # out; otherwise because of the fact that this object inherits from
        # deploy.Cloud __del__ (and perhaps __repr__) will have AttributeErrors
        # because the gc will run and attributes like `.status` and
        # `.scheduler_comm` will not have been assigned to the object's instance
        # yet
        super().__init__(asynchronous, **kwargs)

        self.timeout = (
            timeout if timeout is not None else self.cloud.default_cluster_timeout
        )

        # Set cluster attributes from kwargs (first choice) or dask config

        self.private_to_creator = (
            dask.config.get("coiled.private-to-creator")
            if private_to_creator is None
            else private_to_creator
        )
        self.software_environment = software or dask.config.get("coiled.software")
        self.worker_class = worker_class or dask.config.get("coiled.worker.class")
        self.worker_cpu = worker_cpu or dask.config.get("coiled.worker.cpu")

        if isinstance(worker_cpu, int) and worker_cpu <= 1:
            raise ValueError("`worker_cpu` should be at least 2.")

        self.worker_memory = worker_memory or dask.config.get("coiled.worker.memory")
        # FIXME get these from dask config
        self.worker_vm_types = worker_vm_types
        self.worker_disk_size = worker_disk_size
        self.worker_gpu_count = worker_gpu
        self.worker_gpu_type = worker_gpu_type
        self.worker_options = {
            **(dask.config.get("coiled.worker-options", {})),
            **(worker_options or {}),
        }

        self.scheduler_vm_types = scheduler_vm_types
        self.scheduler_class = scheduler_class or dask.config.get(
            "coiled.scheduler.class"
        )

        self.scheduler_class = scheduler_class or dask.config.get(
            "coiled.scheduler.class"
        )

        self.scheduler_class = scheduler_class or dask.config.get(
            "coiled.scheduler.class"
        )
        self.scheduler_cpu = scheduler_cpu or dask.config.get("coiled.scheduler.cpu")
        self.scheduler_memory = scheduler_memory or dask.config.get(
            "coiled.scheduler.memory"
        )
        self.scheduler_gpu = (
            scheduler_gpu
            if scheduler_gpu is not None
            else dask.config.get("coiled.scheduler.gpu")
        )
        self.use_best_zone = use_best_zone
        self.compute_purchase_option = compute_purchase_option

        self.scheduler_vm_types = scheduler_vm_types
        self.scheduler_options = {
            **(dask.config.get("coiled.scheduler-options", {})),
            **(scheduler_options or {}),
        }

        self.name = name or dask.config.get("coiled.name")
        self.account = account
        self._start_n_workers = n_workers
        self._lock = None
        self._asynchronous = asynchronous
        self.shutdown_on_close = shutdown_on_close
        self.environ = {k: str(v) for (k, v) in (environ or {}).items() if v}
        self.tags = {k: str(v) for (k, v) in (tags or {}).items() if v}
        self.frozen_dask_config = (
            deepcopy(dask.config.config) if send_dask_config else {}
        )
        self.credentials = CredentialsPreferred(credentials)
        self._credentials_duration_seconds = credentials_duration_seconds
        self._default_protocol = dask.config.get("coiled.protocol", "tls")
        self._wait_for_workers_arg = wait_for_workers
        self._last_logged_state_summary = None

        # these are sets of names of workers, only including workers in states that might eventually reach
        # a "started" state
        # they're used in our implementation of scale up/down (mostly inherited from coiled.Cluster)
        # and their corresponding properties are used in adaptive scaling (at least once we
        # make adaptive work with ClusterBeta).
        #
        # (Adaptive expects attributes `requested` and `plan`, which we implement as properties below.)
        #
        # Some good places to learn about adaptive:
        # https://github.com/dask/distributed/blob/39024291e429d983d7b73064c209701b68f41f71/distributed/deploy/adaptive_core.py#L31-L43
        # https://github.com/dask/distributed/issues/5080
        self._requested: Set[str] = set()
        self._plan: Set[str] = set()

        self._adaptive_options: Dict[str, Union[str, int]] = {}
        self.cluster_id: Optional[int] = None
        self.use_scheduler_public_ip: bool = (
            dask.config.get("coiled.use_scheduler_public_ip", True)
            if use_scheduler_public_ip is None
            else use_scheduler_public_ip
        )

        self.backend_options = backend_options

        if (
            allow_ingress_from is not None
            or allow_ssh is not None
            or scheduler_port is not None
        ):
            if backend_options is not None and "ingress" in backend_options:
                raise ArgumentCombinationError(
                    "You cannot use `allow_ingress_from` or `allow_ssh` or `scheduler_port` when "
                    "`ingress` is also specified in `backend_options`."
                )
            firewall_kwargs = {
                "target": allow_ingress_from or "everyone",
                "ssh": False if allow_ssh is None else allow_ssh,
            }

            if scheduler_port is not None:
                firewall_kwargs["scheduler"] = scheduler_port
                self.scheduler_options["port"] = scheduler_port

            self.backend_options = self.backend_options or {}
            self.backend_options["ingress"] = cluster_firewall(**firewall_kwargs)[  # type: ignore
                "ingress"
            ]  # type: ignore

        if not self.asynchronous:
            # If we don't close the cluster, the user's ipython session gets spammed with
            # messages from distributed.
            #
            # Note that this doesn't solve all such spammy dead clusters (which is probably still
            # a problem), just spam created by clusters who failed initial creation.
            error = None
            try:
                self.sync(self._start)
            except (ClusterCreationError, InstanceTypeError) as e:
                error = e
                self.close()
                if self.cluster_id:
                    log_cluster_debug_info(self.cluster_id, self.account)
                raise e.with_traceback(None)
            except KeyboardInterrupt as e:
                error = e
                if self.cluster_id is not None and self.shutdown_on_close in (
                    True,
                    None,
                ):
                    logger.warning(
                        f"Received KeyboardInterrupt, deleting cluster {self.cluster_id}"
                    )
                    self.cloud.delete_cluster(self.cluster_id, account=self.account)
                raise
            except Exception as e:
                error = e
                self.close()
                raise e
            finally:
                if error:
                    self.sync(
                        self.cloud.add_interaction,
                        "cluster-create",
                        success=False,
                        additional_data={
                            "error_class": error.__class__.__name__,
                            "error_message": str(error),
                            **self._as_json_compatible(),
                        },
                    )
                else:
                    self.sync(
                        self.cloud.add_interaction,
                        "cluster-create",
                        success=True,
                        additional_data={
                            **self._as_json_compatible(),
                        },
                    )

    @property
    def details_url(self):
        return get_details_url(self.cloud.server, self.account, self.cluster_id)

    @property
    def _grafana_url(self) -> Optional[str]:
        """for internal Coiled use"""
        if not self.cluster_id:
            return None

        details = self.cloud._get_cluster_details_synced(
            cluster_id=self.cluster_id, account=self.account
        )
        return get_grafana_url(
            details, account=self.account, cluster_id=self.cluster_id
        )

    def _ipython_display_(self):
        cloud = self.cloud
        widget = None
        from IPython.display import display

        if use_rich_widget():
            from .widgets.rich import RichClusterWidget

            widget = RichClusterWidget(server=self.cloud.server, account=self.account)

        if widget and self.cluster_id:
            # TODO: These synchronous calls may be too slow. They can be done concurrently
            cluster_details = cloud._get_cluster_details_synced(
                cluster_id=self.cluster_id, account=self.account
            )
            self.sync(self._update_cluster_status_logs, asynchronous=False)
            widget.update(cluster_details, self._cluster_status_logs)
            display(widget)

    def _repr_mimebundle_(
        self, include: Iterable[str], exclude: Iterable[str], **kwargs
    ):
        # In IPython 7.x This is called in an ipython terminal instead of
        # _ipython_display_ : https://github.com/ipython/ipython/pull/10249
        # In 8.x _ipython_display has been re-enabled in the terminal to
        # allow for rich outputs: https://github.com/ipython/ipython/pull/12315/files
        # So this function *should* only be calle  when in an ipython context using
        # IPython 7.x.
        cloud = self.cloud
        if use_rich_widget() and self.cluster_id:
            from .widgets.rich import RichClusterWidget

            rich_widget = RichClusterWidget(
                server=self.cloud.server, account=self.account
            )
            cluster_details = cloud._get_cluster_details_synced(
                cluster_id=self.cluster_id, account=self.account
            )
            self.sync(self._update_cluster_status_logs, asynchronous=False)
            rich_widget.update(cluster_details, self._cluster_status_logs)
            return rich_widget._repr_mimebundle_(include, exclude, **kwargs)
        else:
            return {"text/plain": repr(self)}

    async def _get_cluster_vm_types_to_use(self):
        cloud = self.cloud
        if (self.worker_cpu or self.worker_memory) and not self.worker_vm_types:
            # match worker types by cpu and/or memory
            worker_vm_types_to_use = get_instance_type_from_cpu_memory(
                self.worker_cpu,
                self.worker_memory,
                gpus=self.worker_gpu_count,
                backend=await self._get_account_cloud_provider_name(),
            )
        elif (self.worker_cpu or self.worker_memory) and self.worker_vm_types:
            raise ArgumentCombinationError(
                "Argument 'worker_vm_types' used together with 'worker_cpu' or 'worker_memory' only "
                "'worker_vm_types' or 'worker_cpu'/'worker_memory' should be used."
            )
        else:
            # get default types from dask config
            if self.worker_vm_types is None:
                self.worker_vm_types = dask.config.get("coiled.worker.vm-types")
            # accept string or list of strings
            if isinstance(self.worker_vm_types, str):
                self.worker_vm_types = [self.worker_vm_types]
            validate_vm_typing(self.worker_vm_types)
            worker_vm_types_to_use = self.worker_vm_types

        if (
            self.scheduler_cpu or self.scheduler_memory
        ) and not self.scheduler_vm_types:
            # match scheduler types by cpu and/or memory
            scheduler_vm_types_to_use = get_instance_type_from_cpu_memory(
                self.scheduler_cpu,
                self.scheduler_memory,
                gpus=1 if self.scheduler_gpu else 0,
                backend=await self._get_account_cloud_provider_name(),
            )
        elif (self.scheduler_cpu or self.scheduler_memory) and self.scheduler_vm_types:
            raise ArgumentCombinationError(
                "Argument 'scheduler_vm_types' used together with 'scheduler_cpu' or "
                "'scheduler_memory' only 'scheduler_vm_types' or "
                "'scheduler_cpu'/'scheduler_memory' should be used."
            )
        else:
            # get default types from dask config
            if self.scheduler_vm_types is None:
                self.scheduler_vm_types = dask.config.get("coiled.scheduler.vm_types")
            # accept string or list of strings
            if isinstance(self.scheduler_vm_types, str):
                self.scheduler_vm_types = [self.scheduler_vm_types]
            validate_vm_typing(self.scheduler_vm_types)
            scheduler_vm_types_to_use = self.scheduler_vm_types

        # If we still don't have instance types, use the defaults
        if not scheduler_vm_types_to_use or not worker_vm_types_to_use:
            provider = await self._get_account_cloud_provider_name()

            if not self.scheduler_gpu and not self.worker_gpu_count:
                # When no GPUs, us same default for scheduler and workers
                default_vm_types = await cloud._get_default_instance_types(
                    provider=provider,
                    gpu=False,
                )
                scheduler_vm_types_to_use = (
                    scheduler_vm_types_to_use or default_vm_types
                )
                worker_vm_types_to_use = worker_vm_types_to_use or default_vm_types
            else:
                # GPUs so there might be different defaults for scheduler/workers
                if not scheduler_vm_types_to_use:
                    scheduler_vm_types_to_use = await cloud._get_default_instance_types(
                        provider=provider,
                        gpu=self.scheduler_gpu,
                    )
                if not worker_vm_types_to_use:
                    worker_vm_types_to_use = await cloud._get_default_instance_types(
                        provider=provider,
                        gpu=bool(self.worker_gpu_count),
                    )

        return scheduler_vm_types_to_use, worker_vm_types_to_use

    async def _get_account_cloud_provider_name(self) -> str:
        if not hasattr(self, "_cached_account_cloud_provider_name"):
            self._cached_account_cloud_provider_name = (
                await self.cloud.get_account_provider_name(account=self.account)
            )

        return self._cached_account_cloud_provider_name

    async def _check_create_or_reuse(self):
        cloud = self.cloud
        if self.name:
            try:
                self.cluster_id = await cloud._get_cluster_by_name(
                    name=self.name,
                    account=self.account,
                )
            except DoesNotExist:
                should_create = True
            else:
                logger.info(
                    f"Using existing cluster: '{self.name} (id: {self.cluster_id})'"
                )
                should_create = False
        else:
            should_create = True
            self.name = (
                self.name
                or (self.account or cloud.default_account)
                + "-"
                + str(uuid.uuid4())[:10]
            )
        return should_create

    async def _determine_senv(self) -> Tuple[bool, Optional[int]]:
        # Attempt to match Coiled software environment to local versions of Python and coiled-runtime
        # FIXME get local coiled-runtime version when it was installed with pip
        warn_for_unspecified_senv = False
        if self.software_environment is None and not self.package_sync:

            py_version = f"py{''.join(map(str, sys.version_info[:2]))}"
            warn_for_unspecified_senv = True
            try:
                senvs = await self.cloud.list_software_environments(account="coiled")  # type: ignore
                runtime_versions = [
                    env
                    for env in senvs
                    if env.endswith(py_version) and "coiled/coiled-runtime" in env
                ]
                self.software_environment = max(runtime_versions, key=name_to_version)  # type: ignore
            except ValueError:
                self.software_environment = f"coiled/default-{py_version}"
            conda_prefix = environ.get("CONDA_PREFIX")
            if conda_prefix:
                conda_meta = Path(conda_prefix) / "conda-meta"
                if conda_meta.exists():
                    coiled_runtime = next(conda_meta.glob("coiled-runtime*.json"), None)
                    if coiled_runtime:
                        match = re.match(
                            r"coiled-runtime-(\d+\.\d+.\d+)", coiled_runtime.name
                        )
                        if match:
                            runtime_version = match[1].replace(".", "-")
                            self.software_environment = (
                                f"coiled/coiled-runtime-{runtime_version}-{py_version}"
                            )
                            warn_for_unspecified_senv = False

        # For package sync, this is where we scrape local environment, determine
        # what to install on cluster, and build/upload wheels as needed.
        if self.package_sync:
            logger.info("Resolving your local python environment...")
            packageLevels = await self.cloud._fetch_package_levels()
            packageLevelLookup = {pkg["name"]: pkg["level"] for pkg in packageLevels}

            approximation = await magic.create_environment_approximation(
                cloud=self.cloud,
                only=self.package_sync_only,
                priorities=packageLevelLookup,
                strict=self.package_sync_strict,
            )

            if not self.package_sync_only:
                # if we're not operating on a subset, check
                # all the coiled defined critical packages are present
                packages_by_name: Dict[str, magic.ResolvedPackageInfo] = {
                    p["name"]: p for p in approximation
                }
                self._check_halting_issues(packageLevels, packages_by_name)
            packages_with_errors = [
                (pkg, packageLevelLookup.get(pkg["name"], 50))
                for pkg in approximation
                if pkg["error"]
            ]
            for (pkg_with_error, level) in packages_with_errors:
                if level >= 50:
                    logfunc = logger.warn
                else:
                    logfunc = logger.info
                logfunc(
                    f"Package - {pkg_with_error['name']}, {pkg_with_error['error']}"
                )
            packages_with_notes = [pkg for pkg in approximation if pkg["note"]]
            for pkg_with_note in packages_with_notes:
                logger.info(
                    f"Package - {pkg_with_note['name']}, {pkg_with_note['note']}"
                )

            if HAS_RICH and self.show_widget:
                from .widgets.rich import print_rich_package_table

                print_rich_package_table(packages_with_notes, packages_with_errors)
            package_sync_env = await self.cloud._create_package_sync_env(
                packages=approximation, account=self.account
            )
            logger.info("Environment magic complete")
        else:
            package_sync_env = None

        return warn_for_unspecified_senv, package_sync_env

    def _check_halting_issues(
        self,
        packageLevels: List[PackageLevel],
        packages_by_name: Dict[str, magic.ResolvedPackageInfo],
    ):
        critical_packages = [
            pkg["name"] for pkg in packageLevels if pkg["level"] == 100
        ]
        halting_failures = []
        for critical_package in critical_packages:
            if critical_package not in packages_by_name:
                problem: magic.ResolvedPackageInfo = {
                    "name": critical_package,
                    "sdist": None,
                    "source": "pip",
                    "channel": None,
                    "conda_name": critical_package,
                    "client_version": "n/a",
                    "specifier": "n/a",
                    "include": False,
                    "note": None,
                    "error": f"Could not detect package locally, please install {critical_package}",
                    "md5": None,
                }
                halting_failures.append(problem)
            elif not packages_by_name[critical_package]["include"]:
                halting_failures.append(packages_by_name[critical_package])
        for packageLevel in packageLevels:
            package = packages_by_name.get(packageLevel["name"])
            if package and package["error"]:
                if (
                    packageLevel["level"] > self.package_sync_fail_on
                    or self.package_sync_strict
                ):
                    halting_failures.append(package)
        if halting_failures:
            failure_str = ", ".join(
                [f'{pkg["name"]} - {pkg["error"]}' for pkg in halting_failures]
            )
            raise RuntimeError(f"Issues with critical packages: {failure_str}")

    async def _attach_to_cluster(self, is_new_cluster: bool):
        # update our view of workers in case someone tries scaling
        # it might be better to continually update this while waiting for the
        # cluster in _security below, but this seems OK for now
        await self._set_plan_requested()

        # this is what waits for the cluster to be "ready"
        await self._wait_until_ready(is_new_cluster)
        self.security, security_info = await self.cloud._security(
            cluster_id=self.cluster_id,
            account=self.account,
        )

        await self._set_plan_requested()  # update our view of workers
        self._proxy = bool(self.security.extra_conn_args)

        self._dashboard_address = security_info["dashboard_address"]

        if self.use_scheduler_public_ip:
            rpc_address = security_info["public_address"]
        else:
            rpc_address = security_info["private_address"]
            logger.info(
                f"Connecting to scheduler on its internal address: {rpc_address}"
            )

        try:
            self.scheduler_comm = dask.distributed.rpc(
                rpc_address,
                connection_args=self.security.get_connection_args("client"),
            )
            await self._send_credentials()
        except IOError as e:
            if "Timed out" in "".join(e.args):
                raise RuntimeError(
                    "Unable to connect to Dask cluster. This may be due "
                    "to different versions of `dask` and `distributed` "
                    "locally and remotely.\n\n"
                    f"You are using distributed={DISTRIBUTED_VERSION} locally.\n\n"
                    "With pip, you can upgrade to the latest with:\n\n"
                    "\tpip install --upgrade dask distributed"
                )
            raise

    @track_context
    async def _start(self):
        did_error = False
        await self.cloud
        try:
            cloud = self.cloud
            self.account = self.account or self.cloud.default_account

            (
                scheduler_vm_types_to_use,
                worker_vm_types_to_use,
            ) = await self._get_cluster_vm_types_to_use()
            should_create = await self._check_create_or_reuse()

            # Set shutdown_on_close here instead of in __init__ to make sure
            # the dask config default isn't used when we are reusing a cluster
            if self.shutdown_on_close is None:
                self.shutdown_on_close = should_create and dask.config.get(
                    "coiled.shutdown-on-close"
                )

            if should_create:
                # Update backend options for cluster based on the friendlier kwargs
                if self.scheduler_gpu:
                    user_provider = await self._get_account_cloud_provider_name()
                    if user_provider == "gcp":
                        self.backend_options = {
                            **GCP_SCHEDULER_GPU,
                            **(self.backend_options or {}),
                        }
                if self.use_best_zone:
                    self.backend_options = {
                        **(self.backend_options or {}),
                        "multizone": True,
                    }
                if self.compute_purchase_option:
                    purchase_configs = {
                        "on-demand": {"spot": False},
                        "spot": {
                            "spot": True,
                            "spot_on_demand_fallback": False,
                        },
                        "spot_with_fallback": {
                            "spot": True,
                            "spot_on_demand_fallback": True,
                        },
                    }

                    if self.compute_purchase_option not in purchase_configs:
                        valid_options = ", ".join(purchase_configs.keys())
                        raise ValueError(
                            f"{self.compute_purchase_option} is not a valid compute_purchase_option; "
                            f"valid options are: {valid_options}"
                        )

                    self.backend_options = {
                        **(self.backend_options or {}),
                        **purchase_configs[self.compute_purchase_option],
                    }

                # Determine software environment (legacy or package sync)
                (
                    warn_for_unspecified_senv,
                    senv_v2_id,
                ) = await self._determine_senv()

                # TODO: more sensible logging
                if warn_for_unspecified_senv:
                    logger.warning(
                        f"Using {self.software_environment} as a software environment\n"
                        "It's recommended that you specify a software environment or use the "
                        "`coiled-runtime` package.\n"
                        "For more information visit"
                        " https://docs.coiled.io/user_guide/tutorials/matching_coiled_senvs.html"
                    )
                # Elsewhere (in _wait_until_ready) we actually decide how many workers to wait for,
                # in a way that's unified/correct for both the "should_create" case and the case
                # where a cluster already exists.
                #
                # However, we should check here to make sure _wait_for_workers_arg is valid to
                # avoid creating the cluster if it's not valid.
                #
                # (We can't do this check earlier because we don't know until now if we're
                # creating a cluster, and if we're not then "_start_n_workers" may be the wrong
                # number of workers...)
                parse_wait_for_workers(
                    self._start_n_workers, self._wait_for_workers_arg
                )

                # Validate software environment name, setting `can_have_revision` to False since
                # we don't seem to be using this yet.
                if not self.package_sync:
                    parse_identifier(
                        self.software_environment,
                        property_name="software_environment",
                        can_have_revision=False,
                    )

                self.cluster_id = await cloud._create_cluster(
                    account=self.account,
                    name=self.name,
                    workers=self._start_n_workers,
                    software_environment=self.software_environment,
                    worker_class=self.worker_class,
                    worker_options=self.worker_options,
                    worker_cpu=self.worker_cpu,
                    worker_memory=self.worker_memory,
                    worker_disk_size=self.worker_disk_size,
                    gcp_worker_gpu_type=self.worker_gpu_type,
                    gcp_worker_gpu_count=self.worker_gpu_count,
                    scheduler_class=self.scheduler_class,
                    scheduler_options=self.scheduler_options,
                    scheduler_cpu=self.scheduler_cpu,
                    scheduler_memory=self.scheduler_memory,
                    environ=self.environ,
                    tags=self.tags,
                    dask_config=self.frozen_dask_config,
                    scheduler_vm_types=scheduler_vm_types_to_use,
                    worker_vm_types=worker_vm_types_to_use,
                    backend_options=self.backend_options,
                    use_scheduler_public_ip=self.use_scheduler_public_ip,
                    senv_v2_id=senv_v2_id,
                    private_to_creator=self.private_to_creator,
                )

            if not self.cluster_id:
                raise RuntimeError(f"Failed to find/create cluster {self.name}")

            if should_create:
                logger.info(
                    f"Creating Cluster (name: {self.name}, {self.details_url} ). This might take a few minutes..."
                )
            else:
                logger.info(
                    f"Attaching to existing cluster (name: {self.name}, {self.details_url} )"
                )

            await self._attach_to_cluster(is_new_cluster=should_create)
            await super()._start()

            # Set adaptive maximum value based on available config and user quota
            self._set_adaptive_options()
        except Exception as e:
            if self._asynchronous:
                did_error = True
                asyncio.create_task(
                    self.cloud.add_interaction(
                        "cluster-create",
                        success=False,
                        additional_data={
                            "error_class": e.__class__.__name__,
                            "error_message": str(e),
                            **self._as_json_compatible(),
                        },
                    )
                )
            raise
        finally:
            if self._asynchronous and not did_error:
                asyncio.create_task(
                    self.cloud.add_interaction(
                        "cluster-create",
                        success=True,
                        additional_data={
                            **self._as_json_compatible(),
                        },
                    )
                )

    def _as_json_compatible(self):
        # the typecasting here is to avoid accidentally
        # submitting something passed in that is not json serializable
        # (user error may cause this)
        return {
            "name": str(self.name),
            "software_environment": str(self.software_environment),
            "show_widget": bool(self.show_widget),
            "async": bool(self._asynchronous),
            "worker_class": str(self.worker_class),
            "worker_cpu": str(self.worker_cpu),
            "worker_memory": str(self.worker_memory),
            "worker_vm_types": str(self.worker_vm_types),
            "worker_gpu_count": str(self.worker_gpu_count),
            "worker_gpu_type": str(self.worker_gpu_type),
            "scheduler_class": str(self.scheduler_class),
            "scheduler_cpu": str(self.scheduler_class),
            "scheduler_memory": str(self.scheduler_memory),
            "scheduler_vm_types": str(self.scheduler_vm_types),
            "n_workers": int(self._start_n_workers),
            "shutdown_on_close": bool(self.shutdown_on_close),
            "use_scheduler_public_ip": bool(self.use_scheduler_public_ip),
            "package_sync": bool(self.package_sync),
            "execution_context": EXECUTION_CONTEXT,
            "account": self.account,
            "timeout": self.timeout,
            "wait_for_workers": self._wait_for_workers_arg,
            "cluster_id": self.cluster_id,
            "backend_options": self.backend_options,
            "scheduler_gpu": self.scheduler_gpu,
            "use_best_zone": self.use_best_zone,
            "compute_purchase_option": self.compute_purchase_option,
            "errored_worker_count": self.errored_worker_count,
            # NOTE: this is not a measure of the CLUSTER life time
            # just a measure of how long this object has been around
            "cluster_object_life": str(datetime.datetime.now() - self.init_time),
        }

    def _maybe_log_summary(self, cluster_details):
        now = time.time()
        if (
            self._last_logged_state_summary is None
            or now > self._last_logged_state_summary + 5
        ):
            logger.info(summarize_status(cluster_details))
            self._last_logged_state_summary = now

    @track_context
    async def _wait_until_ready(self, is_new_cluster) -> None:
        cloud = self.cloud
        cluster_id = self._assert_cluster_id()
        timeout_at = (
            datetime.datetime.now() + datetime.timedelta(seconds=self.timeout)
            if self.timeout is not None
            else None
        )
        self._latest_dt_seen = None

        if self.show_widget:
            if use_rich_widget():
                from .widgets.rich import RichClusterWidget

                widget = RichClusterWidget(
                    n_workers=self._start_n_workers,
                    server=self.cloud.server,
                    account=self.account,
                )
                ctx = widget
            else:
                widget = None
                ctx = contextlib.nullcontext()
        else:
            widget = None
            ctx = contextlib.nullcontext()

        num_workers_to_wait_for = None
        with ctx:
            while True:
                cluster_details = await cloud._get_cluster_details(
                    cluster_id=cluster_id, account=self.account
                )
                # Computing num_workers_to_wait_for inside the while loop is kinda goofy, but I don't want to add an
                # extra _get_cluster_details call right now since that endpoint can be very slow for big clusters.
                # Let's optimize it, and then move this code up outside the loop.

                if num_workers_to_wait_for is None:
                    cluster_desired_workers = cluster_details["desired_workers"]
                    num_workers_to_wait_for = parse_wait_for_workers(
                        cluster_desired_workers, self._wait_for_workers_arg
                    )
                    if not is_new_cluster and (
                        self._start_n_workers != cluster_desired_workers
                    ):
                        logging.warning(
                            f"Ignoring your request for {self._start_n_workers} workers since you are "
                            f"connecting to a cluster that had been requested with {cluster_desired_workers} workers"
                        )

                await self._update_cluster_status_logs()
                self._maybe_log_summary(cluster_details)

                if widget:
                    widget.update(
                        cluster_details,
                        self._cluster_status_logs,
                    )

                cluster_state = ClusterStateEnum(
                    cluster_details["current_state"]["state"]
                )
                reason = cluster_details["current_state"]["reason"]

                scheduler_current_state = cluster_details["scheduler"]["current_state"]
                scheduler_state = ProcessStateEnum(scheduler_current_state["state"])
                if cluster_details["scheduler"].get("instance"):
                    scheduler_instance_state = InstanceStateEnum(
                        cluster_details["scheduler"]["instance"]["current_state"][
                            "state"
                        ]
                    )
                else:
                    scheduler_instance_state = InstanceStateEnum.queued
                worker_current_states = [
                    w["current_state"] for w in cluster_details["workers"]
                ]
                ready_worker_current = [
                    current
                    for current in worker_current_states
                    if ProcessStateEnum(current["state"]) == ProcessStateEnum.started
                ]
                self.errored_worker_count = sum(
                    [
                        1
                        for current in worker_current_states
                        if ProcessStateEnum(current["state"]) == ProcessStateEnum.error
                    ]
                )

                if (
                    scheduler_state == ProcessStateEnum.started
                    and scheduler_instance_state
                    in [
                        InstanceStateEnum.ready,
                        InstanceStateEnum.started,
                    ]
                ):
                    scheduler_ready = True
                    scheduler_reason_not_ready = ""
                else:
                    scheduler_ready = False
                    scheduler_reason_not_ready = "Scheduler not ready."

                n_workers_ready = len(ready_worker_current)
                final_update = None
                if n_workers_ready >= num_workers_to_wait_for:
                    if n_workers_ready == self._start_n_workers:
                        final_update = "All workers ready."
                    else:
                        final_update = (
                            "Most of your workers have arrived. Cluster ready for use."
                        )

                    workers_ready = True
                    workers_reason_not_ready = ""

                else:
                    workers_ready = False
                    workers_reason_not_ready = (
                        f"Only {len(ready_worker_current)} workers ready "
                        f"(was waiting for at least {num_workers_to_wait_for}). "
                    )
                # TODO -- if all workers are ready *or error* then give final update

                if scheduler_ready and workers_ready:
                    assert final_update is not None
                    if widget:
                        widget.update(
                            cluster_details,
                            self._cluster_status_logs,
                            final_update=final_update,
                        )
                    logger.info(summarize_status(cluster_details))
                    return
                else:
                    reason_not_ready = (
                        scheduler_reason_not_ready
                        if not scheduler_ready
                        else workers_reason_not_ready
                    )
                    if cluster_state in (
                        ClusterStateEnum.error,
                        ClusterStateEnum.stopped,
                    ):
                        # this cluster will never become ready; raise an exception
                        error = f"Cluster status is {cluster_state.value} (reason: {reason})"
                        if widget:
                            widget.update(
                                cluster_details,
                                self._cluster_status_logs,
                                final_update=error,
                            )
                        logger.info(summarize_status(cluster_details))
                        raise ClusterCreationError(
                            error,
                            cluster_id=self.cluster_id,
                        )
                    elif cluster_state == ClusterStateEnum.ready:
                        # (cluster state "ready" means all worked either started or errored, so
                        # this cluster will ever have all the workers we want)
                        if widget:
                            widget.update(
                                cluster_details,
                                self._cluster_status_logs,
                                final_update=reason_not_ready,
                            )
                        logger.info(summarize_status(cluster_details))
                        raise ClusterCreationError(
                            reason_not_ready,
                            cluster_id=self.cluster_id,
                        )
                    elif (
                        timeout_at is not None and datetime.datetime.now() > timeout_at
                    ):
                        error = "User-specified timeout expired: " + reason_not_ready
                        if widget:
                            widget.update(
                                cluster_details,
                                self._cluster_status_logs,
                                final_update=error,
                            )
                        logger.info(summarize_status(cluster_details))
                        raise ClusterCreationError(
                            error,
                            cluster_id=self.cluster_id,
                        )
                    else:
                        await asyncio.sleep(1.0)

    async def _update_cluster_status_logs(self):
        cluster_id = self._assert_cluster_id()
        states_by_type = await self.cloud._get_cluster_states_declarative(
            cluster_id, self.account, start_time=self._latest_dt_seen
        )
        states = flatten_log_states(states_by_type)
        if states:
            if not self.show_widget or EXECUTION_CONTEXT == "terminal":
                log_states(states)
            self._latest_dt_seen = states[-1].updated
            self._cluster_status_logs.extend(states)

    def _assert_cluster_id(self) -> int:
        if self.cluster_id is None:
            raise RuntimeError(
                "'cluster_id' is not set, perhaps the cluster hasn't been created yet"
            )
        return self.cluster_id

    def cwi_logs_url(self):
        if self.cluster_id is None:
            raise ValueError(
                "cluster_id is None. Cannot get CloudWatch link without a cluster"
            )

        # kinda hacky, probably something as important as region ought to be an attribute on the
        # cluster itself already and not require an API call
        cluster_details = self.cloud._get_cluster_details_synced(
            cluster_id=self.cluster_id, account=self.account
        )
        if cluster_details["backend_type"] != "vm_aws":
            raise ValueError("Sorry, the cwi_logs_url only works for AWS clusters.")
        region = cluster_details["cluster_options"]["region_name"]

        return cloudwatch_url(self.account, self.name, region)

    def details(self):
        if self.cluster_id is None:
            raise ValueError("cluster_id is None. Cannot get details without a cluster")
        return self.cloud.cluster_details(
            cluster_id=self.cluster_id, account=self.account
        )

    async def _set_plan_requested(self):
        eventually_maybe_good_statuses = [
            ProcessStateEnum.starting,
            ProcessStateEnum.pending,
            ProcessStateEnum.started,
        ]
        eventually_maybe_good_workers = await self.cloud._get_worker_names(
            account=self.account,
            cluster_id=self.cluster_id,
            statuses=eventually_maybe_good_statuses,
        )
        self._plan = eventually_maybe_good_workers
        self._requested = eventually_maybe_good_workers

    @track_context
    async def _scale(self, n: int) -> None:
        await self._set_plan_requested()  # need to update our understanding of current workers before scaling
        logger.debug(f"current _plan: {self._plan}")
        if not self.cluster_id:
            raise ValueError("No cluster available to scale!")
        recommendations = await self.recommendations(n)
        logger.debug(f"scale recommmendations: {recommendations}")
        status = recommendations.pop("status")
        if status == "same":
            return
        if status == "up":
            return await self.scale_up(**recommendations)
        if status == "down":
            return await self.scale_down(**recommendations)

    @track_context
    async def scale_up(self, n: int) -> None:
        """
        Scales up *to* a target number of ``n`` workers

        It's documented that scale_up should scale up to a certain target, not scale up BY a certain amount:

        https://github.com/dask/distributed/blob/main/distributed/deploy/adaptive_core.py#L60
        """
        if not self.cluster_id:
            raise ValueError(
                "No cluster available to scale! "
                "Check cluster was not closed by another process."
            )
        target = n - len(self.plan)
        response = await self.cloud._scale_up(
            account=self.account,
            cluster_id=self.cluster_id,
            n=target,
        )
        if response:
            self._plan.update(set(response.get("workers", [])))
            self._requested.update(set(response.get("workers", [])))

    def _set_adaptive_options(self, **kwargs):
        # legacy version got dict with data about account limit and worker size
        # and then used that to determine maximum size for adaptive scaling
        self._adaptive_options = {
            "interval": "5s",
            "wait_count": 12,
            "target_duration": "5m",
            "minimum": 1,
            # TODO: want a more sensible limit; see _set_adaptive_options in coiled.Cluster
            # for inspiration from the logic there
            "maximum": 200,
        }

    @track_context
    async def _close(self, force_shutdown: bool = False) -> None:
        # My small changes to _close probably make sense for legacy Cluster too, but I don't want to carefully
        # test them, so copying this method over.

        with suppress(AttributeError):
            self._adaptive.stop()

        # Stop here because otherwise we get intermittent `OSError: Timed out` when
        # deleting cluster takes a while and callback tries to poll cluster status.
        for pc in self.periodic_callbacks.values():
            pc.stop()

        if hasattr(self, "cluster_id") and self.cluster_id:
            # If the initial create call failed, we don't have a cluster ID.
            # But the rest of this method (at least calling distributed.deploy.Cluster.close)
            # is important.
            if force_shutdown or self.shutdown_on_close in (True, None):
                await self.cloud._delete_cluster(
                    account=self.account,
                    cluster_id=self.cluster_id,
                )
        await super()._close()

    @property
    def requested(self):
        return self._requested

    @property
    def plan(self):
        return self._plan

    @overload
    def sync(
        self: ClusterBeta[Sync],
        func: Callable[..., Awaitable[_T]],
        *args,
        asynchronous: Union[Sync, Literal[None]] = None,
        callback_timeout=None,
        **kwargs,
    ) -> _T:
        ...

    @overload
    def sync(
        self: ClusterBeta[Async],
        func: Callable[..., Awaitable[_T]],
        *args,
        asynchronous: Union[bool, Literal[None]] = None,
        callback_timeout=None,
        **kwargs,
    ) -> Awaitable[_T]:
        ...

    def sync(
        self,
        func: Callable[..., Awaitable[_T]],
        *args,
        asynchronous: Optional[bool] = None,
        callback_timeout=None,
        **kwargs,
    ) -> Union[_T, Awaitable[_T]]:
        return super().sync(
            func,
            *args,
            asynchronous=asynchronous,
            callback_timeout=callback_timeout,
            **kwargs,
        )

    def _ensure_scheduler_comm(self) -> dask.distributed.rpc:
        """
        Guard to make sure that the scheduler comm exists before trying to use it.
        """
        if not self.scheduler_comm:
            raise RuntimeError(
                "Scheduler comm is not set, have you been disconnected from Coiled?"
            )
        return self.scheduler_comm

    @track_context
    async def _wait_for_workers(
        self,
        n_workers,
        timeout=None,
        err_msg=None,
    ) -> None:
        if timeout is None:
            deadline = None
        else:
            timeout = dask.utils.parse_timedelta(timeout, "s")
            deadline = time.time() + timeout
        while n_workers and len(self.scheduler_info["workers"]) < n_workers:
            if deadline and time.time() > deadline:
                err_msg = err_msg or (
                    f"Timed out after {timeout} seconds waiting for {n_workers} workers to arrive, "
                    "check your notifications with coiled.get_notifications() for further details"
                )
                raise TimeoutError(err_msg)
            await asyncio.sleep(1)

    @staticmethod
    def _sync_get_aws_local_session_token(
        duration_seconds: Optional[int] = None,
    ) -> AWSSessionCredentials:
        token_creds = AWSSessionCredentials(
            AccessKeyId="", SecretAccessKey="", SessionToken=None, Expiration=None
        )
        try:
            from boto3.session import Session

            session = Session()
            sts = session.client("sts")
            try:
                kwargs = (
                    {"DurationSeconds": duration_seconds} if duration_seconds else {}
                )
                credentials = sts.get_session_token(**kwargs)

                credentials = credentials["Credentials"]
                token_creds = AWSSessionCredentials(
                    AccessKeyId=credentials.get("AccessKeyId", ""),
                    SecretAccessKey=credentials.get("SecretAccessKey", ""),
                    SessionToken=credentials.get("SessionToken"),
                    Expiration=credentials.get("Expiration"),
                )
            except botocore.errorfactory.ClientError as e:
                if "session credentials" in str(e):
                    # Credentials are already an STS token, which gives us this error:
                    # > Cannot call GetSessionToken with session credentials
                    # In this case we'll just use the existing STS token for the active, local session.
                    # Note that in some cases this will have a shorter TTL than the default 12 hour tokens.
                    credentials = session.get_credentials()
                    frozen_creds = credentials.get_frozen_credentials()

                    expiration = (
                        credentials._expiry_time
                        if hasattr(credentials, "_expiry_time")
                        else None
                    )

                    logger.debug(
                        "Local AWS session is already using STS token, this will be used since we can't "
                        f"generate a new STS token from this. Expiration: {expiration}."
                    )

                    token_creds = AWSSessionCredentials(
                        AccessKeyId=frozen_creds.access_key,
                        SecretAccessKey=frozen_creds.secret_key,
                        SessionToken=frozen_creds.token,
                        Expiration=expiration,
                    )

        except (
            botocore.exceptions.ProfileNotFound,
            botocore.exceptions.NoCredentialsError,
        ):
            # no AWS credentials (maybe not running against AWS?), fail gracefully
            pass
        except Exception as e:
            # for some aiobotocore versions (e.g. 2.3.4) we get one of these errors
            # rather than NoCredentialsError
            if "Could not connect to the endpoint URL" in str(e):
                pass
            elif "Connect timeout on endpoint URL" in str(e):
                pass
            else:
                # warn, but don't crash
                logger.warning(f"Error getting STS token from client AWS session: {e}")

        return token_creds

    async def _get_aws_local_session_token(
        self,
        duration_seconds: Optional[int] = None,
    ) -> AWSSessionCredentials:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            None, self._sync_get_aws_local_session_token, duration_seconds
        )

    def send_credentials(self, automatic_refresh: bool = False):
        """
        Manually trigger sending STS token to cluster.

        Usually STS token is automatically sent and refreshed by default, this allows
        you to manually force a refresh in case that's needed for any reason.
        """
        return self.sync(self._send_credentials, schedule_callback=automatic_refresh)

    async def _send_credentials(self, schedule_callback: bool = True):
        """
        Get credentials and pass them to the scheduler.
        """
        if self.credentials is not CredentialsPreferred.NONE:
            try:
                if self.credentials is CredentialsPreferred.ACCOUNT:
                    # cloud.get_aws_credentials doesn't return credentials for currently implemented backends
                    # aws_creds = await cloud.get_aws_credentials(self.account)
                    logger.warning(
                        "Using account backend AWS credentials is not currently supported, "
                        "local AWS credentials (if present) will be used."
                    )

                token_creds = await self._get_aws_local_session_token(
                    duration_seconds=self._credentials_duration_seconds
                )
                if token_creds:
                    scheduler_comm = self._ensure_scheduler_comm()

                    await scheduler_comm.aws_update_credentials(
                        credentials={
                            k: token_creds.get(k)
                            for k in [
                                "AccessKeyId",
                                "SecretAccessKey",
                                "SessionToken",
                            ]
                        }
                    )

                    if schedule_callback:
                        # schedule callback for updating creds before they expire

                        # default to updating every 45 minutes
                        delay = 45 * 60

                        if (
                            self._credentials_duration_seconds
                            and self._credentials_duration_seconds < 900
                        ):
                            # 15 minutes is min duration for STS token, but if shorter duration explicitly
                            # requested, then we'll update as if that were the duration (with lower bound of 5s).
                            delay = max(
                                5, int(self._credentials_duration_seconds * 0.5)
                            )
                        else:
                            # Otherwise, get duration from expiration set on the STS token.
                            expiration = token_creds.get("Expiration")
                            if expiration:
                                diff = expiration - datetime.datetime.now(tz=tz.UTC)
                                delay = int((diff * 0.5).total_seconds())

                                if diff < datetime.timedelta(minutes=5):
                                    # usually the existing STS token will be from a role assumption and
                                    # will expire in ~1 hour, but just in case the local session has a very
                                    # short lived token, let the user know
                                    # TODO give user information about what to do in this case
                                    logger.warning(
                                        f"Locally generated AWS STS token expires in less than 5 minutes ({diff}). "
                                        "Code running on your cluster may be unable to access other AWS services "
                                        "(e.g, S3) when this token expires."
                                    )

                                # don't try to update sooner than in 1 minute
                                delay = max(60, delay)

                        self.loop.call_later(
                            delay=delay, callback=self._send_credentials
                        )
                        logger.debug(
                            "AWS STS token from local credentials shipped to cluster, "
                            f"planning to refresh in {delay} seconds"
                        )
                    else:
                        logger.debug(
                            "AWS STS token from local credentials shipped to cluster, no scheduled refresh"
                        )

            except Exception as e:
                terminating_states = (
                    Status.closing,
                    Status.closed,
                    Status.closing_gracefully,
                    Status.failed,
                )
                if self.status not in terminating_states:
                    # warn, but don't crash
                    logger.warning(f"error sending AWS credentials to cluster: {e}")

    def __await__(self: ClusterBeta[Async]):
        async def _():
            if self._lock is None:
                self._lock = asyncio.Lock()
            async with self._lock:
                if self.status == Status.created:
                    await wait_for(self._start(), self.timeout)
                assert self.status == Status.running
            return self

        return _().__await__()

    @overload
    def close(self: ClusterBeta[Sync], force_shutdown: bool = False) -> None:
        ...

    @overload
    def close(
        self: ClusterBeta[Async], force_shutdown: bool = False
    ) -> Awaitable[None]:
        ...

    def close(self, force_shutdown: bool = False) -> Union[None, Awaitable[None]]:
        """
        Close the cluster.
        """
        return self.sync(self._close, force_shutdown=force_shutdown)

    @overload
    def shutdown(self: ClusterBeta[Sync]) -> None:
        ...

    @overload
    def shutdown(self: ClusterBeta[Async]) -> Awaitable[None]:
        ...

    def shutdown(self) -> Union[None, Awaitable[None]]:
        """
        Shutdown the cluster; useful when shutdown_on_close is False.
        """
        return self.sync(self._close, force_shutdown=True)

    @overload
    def scale(self: ClusterBeta[Sync], n: int) -> None:
        ...

    @overload
    def scale(self: ClusterBeta[Async], n: int) -> Awaitable[None]:
        ...

    def scale(self, n: int) -> Optional[Awaitable[None]]:
        """Scale cluster to ``n`` workers

        Parameters
        ----------
        n
            Number of workers to scale cluster size to.
        """
        return self.sync(self._scale, n=n)

    @track_context
    async def scale_down(self, workers: set) -> None:
        if not self.cluster_id:
            raise ValueError("No cluster available to scale!")
        cloud = cast(CloudBeta[Async], self.cloud)
        try:
            scheduler_comm = self._ensure_scheduler_comm()
            await scheduler_comm.retire_workers(
                names=workers,
                remove=True,
                close_workers=True,
            )
        except Exception as e:
            logging.warning(f"error retiring workers {e}. Trying more forcefully")
        # close workers more forcefully
        await cloud._scale_down(
            account=self.account,
            cluster_id=self.cluster_id,
            workers=workers,
        )
        self._plan.difference_update(workers)
        self._requested.difference_update(workers)

    async def recommendations(self, target: int) -> dict:
        """
        Make scale up/down recommendations based on current state and target
        """
        plan = self.plan
        requested = self.requested
        observed = self.observed

        if target == len(plan):
            return {"status": "same"}

        if target > len(plan):
            return {"status": "up", "n": target}

        not_yet_arrived = requested - observed
        to_close = set()
        if not_yet_arrived:
            to_close.update(toolz.take(len(plan) - target, not_yet_arrived))

        if target < len(plan) - len(to_close):
            L = await self.workers_to_close(target=target)
            to_close.update(L)
        return {"status": "down", "workers": list(to_close)}

    async def workers_to_close(self, target: int):
        """
        Determine which, if any, workers should potentially be removed from
        the cluster.

        Notes
        -----
        ``Cluster.workers_to_close`` dispatches to Scheduler.workers_to_close(),
        but may be overridden in subclasses.

        Returns
        -------
        List of worker addresses to close, if any

        See Also
        --------
        Scheduler.workers_to_close
        """
        scheduler_comm = self._ensure_scheduler_comm()
        ret = await scheduler_comm.workers_to_close(
            target=target,
            attribute="name",
        )
        return ret

    def adapt(self, Adaptive=CoiledAdaptive, **kwargs) -> Adaptive:
        """Dynamically scale the number of workers in the cluster
        based on scaling heuristics.

        Parameters
        ----------
        minimum : int
            Minimum number of workers that the cluster should have while
            on low load, defaults to 1.
        maximum : int
            Maximum numbers of workers that the cluster should have while
            on high load. If maximum is not set, this value will be based
            on your core count limit. This value is also capped by your
            core count limit.
        wait_count : int
            Number of consecutive times that a worker should be suggested
            for removal before the cluster removes it, defaults to 60.
        interval : timedelta or str
            Milliseconds between checks, default sto 5000 ms.
        target_duration : timedelta or str
            Amount of time we want a computation to take. This affects how
            aggressively the cluster scales up, defaults to 5s.

        """
        maximum = kwargs.pop("maximum", None)
        if maximum is not None:
            kwargs["maximum"] = maximum
        return super().adapt(Adaptive=Adaptive, **kwargs)

    def __enter__(self: ClusterBeta[Sync]) -> ClusterBeta[Sync]:
        return self.sync(self.__aenter__)

    def __exit__(self: ClusterBeta[Sync], *args, **kwargs) -> None:
        return self.sync(self.__aexit__, *args, **kwargs)

    @overload
    def get_logs(
        self: ClusterBeta[Sync], scheduler: bool, workers: bool = True
    ) -> dict:
        ...

    @overload
    def get_logs(
        self: ClusterBeta[Async], scheduler: bool, workers: bool = True
    ) -> Awaitable[dict]:
        ...

    def get_logs(
        self, scheduler: bool = True, workers: bool = True
    ) -> Union[dict, Awaitable[dict]]:
        """Return logs for the scheduler and workers
        Parameters
        ----------
        scheduler : boolean
            Whether or not to collect logs for the scheduler
        workers : boolean
            Whether or not to collect logs for the workers
        Returns
        -------
        logs: Dict[str]
            A dictionary of logs, with one item for the scheduler and one for
            the workers
        """
        return self.sync(self._get_logs, scheduler=scheduler, workers=workers)

    @track_context
    async def _get_logs(self, scheduler: bool = True, workers: bool = True) -> dict:
        if not self.cluster_id:
            raise ValueError("No cluster available for logs!")
        cloud = cast(CloudBeta[Async], self.cloud)
        return await cloud.cluster_logs(
            cluster_id=self.cluster_id,
            account=self.account,
            scheduler=scheduler,
            workers=workers,
        )

    @property
    def dashboard_link(self):
        # Only use proxied dashboard address if we're in a hosted notebook
        # Otherwise fall back to the non-proxied address
        if self._proxy or dask.config.get("coiled.dashboard.proxy", False):
            return f"{self.cloud.server}/dashboard/{self.cluster_id}/status"
        else:
            return self._dashboard_address
