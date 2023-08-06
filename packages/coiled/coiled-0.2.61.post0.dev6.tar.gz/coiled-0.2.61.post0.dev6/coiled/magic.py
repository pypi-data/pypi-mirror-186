import asyncio
import logging
import platform
import subprocess
import typing
from logging import getLogger
from pathlib import Path
from sys import executable
from tempfile import TemporaryDirectory
from threading import Lock
from typing import Dict, List, Optional, Set, TextIO, Union

from packaging.utils import parse_wheel_filename

from coiled._beta.core import CloudBeta
from coiled.scan import PackageInfo, scan_prefix
from coiled.types import ResolvedPackageInfo
from coiled.utils import validate_wheel

logger = getLogger("coiled.package_sync")
subdir_datas = {}
PYTHON_VERSION = platform.python_version_tuple()
ANY_AVAILABLE = "ANY-AVAILABLE"


async def create_subprocess_shell(
    cmd: str,
    stdout: Union[TextIO, int, None] = None,
    stderr: Union[TextIO, int, None] = None,
) -> subprocess.CompletedProcess:
    # asyncio.create_subprocess_shell is
    # not supported on windows
    # and broken on py3.7
    loop = asyncio.get_running_loop()
    result = loop.run_in_executor(
        None, lambda: subprocess.run(cmd, shell=True, stdout=stdout, stderr=stderr)
    )
    return await result


async def default_python() -> PackageInfo:
    python_version = platform.python_version()
    return {
        "name": "python",
        "path": None,
        "source": "conda",
        "channel_url": ANY_AVAILABLE,
        "channel": ANY_AVAILABLE,
        "subdir": "linux-64",
        "conda_name": "python",
        "version": python_version,
        "wheel_target": None,
    }


class PackageBuildError(Exception):
    pass


WHEEL_BUILD_LOCKS: Dict[str, Lock] = {}


async def create_wheel(pkg_name: str, version: str, src: str) -> ResolvedPackageInfo:
    lock = WHEEL_BUILD_LOCKS.setdefault(pkg_name, Lock())
    with lock:
        tmpdir = TemporaryDirectory()
        outdir = Path(tmpdir.name) / Path(pkg_name)
        logger.info(f"Attempting to create a wheel for {pkg_name} @ {src}")
        # must use executable to avoid using some other random python
        p = await create_subprocess_shell(
            cmd=f"{executable} -m pip wheel --wheel-dir {outdir} --no-deps --use-pep517 --no-cache-dir {src}",
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE,
        )
        if p.returncode:
            print(f"---Wheel Build Log for {pkg_name}---\n{p.stdout.decode()}")
            return {
                "name": pkg_name,
                "source": "pip",
                "channel": None,
                "conda_name": None,
                "client_version": version,
                "specifier": "",
                "include": False,
                "error": (
                    "Failed to build a wheel for the"
                    " package, will not be included in environment, check stdout for the build log"
                ),
                "note": None,
                "sdist": None,
                "md5": None,
            }
        wheel_fn = next(file for file in outdir.iterdir() if file.suffix == ".whl")
        _, build_version, _, _ = parse_wheel_filename(str(wheel_fn.name))
        has_python, md5 = await validate_wheel(wheel_fn)
    return {
        "name": pkg_name,
        "source": "pip",
        "channel": None,
        "conda_name": None,
        "client_version": str(build_version),
        "specifier": "",
        "include": True,
        "error": None if has_python else "Built wheel contains no python files!",
        "note": f"Wheel built from {src}",
        "sdist": wheel_fn.open("rb"),
        "md5": md5,
    }


async def create_wheel_from_egg(
    pkg_name: str, version: str, src: str
) -> ResolvedPackageInfo:
    tmpdir = TemporaryDirectory()
    outdir = Path(tmpdir.name) / Path(pkg_name)
    outdir.mkdir(parents=True)
    logger.info(f"Attempting to create a wheel for {pkg_name} in directory {src}")
    # must use executable to avoid using some other random python
    p = await create_subprocess_shell(
        cmd=f"{executable} -m wheel convert --dest-dir {outdir} {src}",
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE,
    )
    if p.returncode:
        print(f"---Egg to wheel conversion Log for {pkg_name}---\n{p.stdout.decode()}")
        return {
            "name": pkg_name,
            "source": "pip",
            "channel": None,
            "conda_name": None,
            "client_version": version,
            "specifier": "",
            "include": False,
            "error": (
                "Failed to convert the package egg to a wheel"
                ", will not be included in environment, check stdout for egg conversion log"
            ),
            "note": None,
            "sdist": None,
            "md5": None,
        }
    wheel_fn = next(file for file in outdir.iterdir() if file.suffix == ".whl")
    has_python, md5 = await validate_wheel(Path(wheel_fn))
    return {
        "name": pkg_name,
        "source": "pip",
        "channel": None,
        "conda_name": None,
        "client_version": version,
        "specifier": "",
        "include": True,
        "error": None if has_python else "Built wheel has no python files!",
        "note": "Wheel built from local egg",
        "sdist": wheel_fn.open("rb"),
        "md5": md5,
    }


async def approximate_packages(
    cloud: CloudBeta,
    packages: List[PackageInfo],
    priorities: Dict[str, int],
    strict: bool = False,
) -> typing.List[ResolvedPackageInfo]:
    user_conda_installed_python = next(
        (p for p in packages if p["name"] == "python"), None
    )
    user_conda_installed_pip = next(
        (
            i
            for i, p in enumerate(packages)
            if p["name"] == "pip" and p["source"] == "conda"
        ),
        None,
    )
    if not user_conda_installed_pip:
        # This means pip was installed by pip, or the system
        # package manager
        # Insert a conda version of pip to be installed first, it will
        # then be used to install the users version of pip
        packages.append(
            {
                "name": "pip",
                "path": None,
                "source": "conda",
                "channel_url": "https://repo.anaconda.com/pkgs/main",
                "channel": "pkgs/main",
                "subdir": "linux-64",
                "conda_name": "pip",
                "version": "22.3.1",
                "wheel_target": None,
            }
        )
    coiled_selected_python = None
    if not user_conda_installed_python:
        # insert a special python package
        # that the backend will pick a channel for
        coiled_selected_python = await default_python()
        packages.append(coiled_selected_python)

    results = await cloud._approximate_packages(
        packages=[
            {
                "name": pkg["name"],
                "priority_override": 100 if strict else priorities.get(pkg["name"]),
                "python_major_version": PYTHON_VERSION[0],
                "python_minor_version": PYTHON_VERSION[1],
                "python_patch_version": PYTHON_VERSION[2],
                "source": pkg["source"],
                "channel_url": pkg["channel_url"],
                "channel": pkg["channel"],
                "subdir": pkg["subdir"],
                "conda_name": pkg["conda_name"],
                "version": pkg["version"],
                "wheel_target": pkg["wheel_target"],
            }
            for pkg in packages
        ]
    )
    result_map = {r["name"]: r for r in results}
    finalized_packages: typing.List[ResolvedPackageInfo] = []

    if not user_conda_installed_python and coiled_selected_python:
        # user has no python version installed by conda
        # we should have a result of asking the backend to
        # pick conda channel that has the users python version
        assert result_map["python"]["note"]
        channel_url, channel = result_map["python"]["note"].split(",")
        finalized_packages.append(
            {
                "name": "python",
                "source": "conda",
                "channel": channel,
                "conda_name": "python",
                "client_version": coiled_selected_python["version"],
                "specifier": result_map["python"]["specifier"] or "",
                "include": result_map["python"]["include"],
                "note": None,
                "error": result_map["python"]["error"],
                "sdist": None,
                "md5": None,
            }
        )
        # we can pull our special python package out of the list
        # now
        packages.remove(coiled_selected_python)
    for pkg in packages:
        if pkg["wheel_target"] and result_map[pkg["name"]]["include"]:
            if pkg["wheel_target"].endswith(".egg"):
                finalized_packages.append(
                    await create_wheel_from_egg(
                        pkg_name=pkg["name"],
                        version=pkg["version"],
                        src=pkg["wheel_target"],
                    )
                )
            else:
                finalized_packages.append(
                    await create_wheel(
                        pkg_name=pkg["name"],
                        version=pkg["version"],
                        src=pkg["wheel_target"],
                    )
                )
        else:
            finalized_packages.append(
                {
                    "name": pkg["name"],
                    "source": pkg["source"],
                    "channel": pkg["channel"],
                    "conda_name": pkg["conda_name"],
                    "client_version": pkg["version"],
                    "specifier": result_map[pkg["name"]]["specifier"] or "",
                    "include": result_map[pkg["name"]]["include"],
                    "note": result_map[pkg["name"]]["note"],
                    "error": result_map[pkg["name"]]["error"],
                    "sdist": None,
                    "md5": None,
                }
            )
    return finalized_packages


async def create_environment_approximation(
    cloud: CloudBeta,
    priorities: Dict[str, int],
    only: Optional[Set[str]] = None,
    strict: bool = False,
) -> typing.List[ResolvedPackageInfo]:
    packages = await scan_prefix()
    if only:
        packages = filter(lambda pkg: pkg["name"] in only, packages)
    # TODO: private conda channels
    result = await approximate_packages(
        cloud=cloud,
        packages=[pkg for pkg in packages],
        priorities=priorities,
        strict=strict,
    )

    return result


if __name__ == "__main__":
    from logging import basicConfig

    basicConfig(level=logging.INFO)

    from rich.console import Console
    from rich.table import Table

    async def run():
        async with CloudBeta(asynchronous=True) as cloud:
            return await create_environment_approximation(
                cloud=cloud,
                priorities={"dask": 100, "twisted": -2, "graphviz": -1, "icu": -1},
            )

    result = asyncio.run(run())

    table = Table(title="Packages")
    keys = ("name", "source", "include", "client_version", "specifier", "error", "note")

    for key in keys:
        table.add_column(key)

    for pkg in result:
        row_values = [str(pkg.get(key, "")) for key in keys]
        table.add_row(*row_values)
    console = Console()
    console.print(table)
    console.print(table)
