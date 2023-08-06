import asyncio
import json
import os
import platform
import sys
import typing
from logging import getLogger
from pathlib import Path
from typing import Dict, List, Optional, Union

from importlib_metadata import Distribution

from coiled.types import CondaPackage, CondaPlaceHolder, PackageInfo

logger = getLogger("coiled.package_sync")
subdir_datas = {}
PYTHON_VERSION = platform.python_version_tuple()


async def scan_conda(prefix: Path) -> typing.Dict[str, PackageInfo]:
    conda_meta = prefix / "conda-meta"
    if conda_meta.exists() and conda_meta.is_dir():
        conda_packages = [
            CondaPackage(json.load(metafile.open("r")), prefix=prefix)
            for metafile in conda_meta.iterdir()
            if metafile.suffix == ".json"
        ]
        packages = await asyncio.gather(
            *[handle_conda_package(pkg) for pkg in conda_packages]
        )
        return {pkg["name"]: pkg for pkg in packages}
    else:
        return {}


async def handle_conda_package(pkg: CondaPackage) -> PackageInfo:
    # Are there conda packages that install multiple python packages?
    metadata_location = next(
        (Path(fp).parent for fp in pkg.files if fp.endswith("METADATA")), None
    )
    if metadata_location:
        dist = Distribution.at(pkg.prefix / metadata_location)
        name = dist.metadata["Name"] or pkg.name
    else:
        name = pkg.name
    return {
        "channel": pkg.channel,
        "path": None,
        "channel_url": pkg.channel_url,
        "source": "conda",
        "conda_name": pkg.name,
        "subdir": pkg.subdir,
        "name": name,
        "version": pkg.version,
        "wheel_target": None,
    }


async def handle_dist(
    dist: Distribution, locations: List[Path]
) -> Optional[Union[PackageInfo, CondaPlaceHolder]]:
    installer = dist.read_text("INSTALLER") or ""
    installer = installer.rstrip()
    # dist._path can sometimes be a zipp.Path or something else
    dist_path = Path(str(dist._path))  # type: ignore
    if installer == "conda":
        return CondaPlaceHolder(name=dist.name)
    elif dist_path.parent.suffix == ".egg":
        # egg files can be a directory OR a zip file
        # the zipp implementation of Path always uses
        # linux style seperators so we strip them too
        return {
            "name": dist.name,
            "path": dist_path.parent,
            "source": "pip",
            "channel": None,
            "subdir": None,
            "channel_url": None,
            "conda_name": None,
            "version": dist.version,
            "wheel_target": str(dist_path.parent).rstrip(os.sep + "/"),
        }
    else:
        direct_url_metadata = dist.read_text("direct_url.json")
        if direct_url_metadata:
            url_metadata = json.loads(direct_url_metadata)
            if url_metadata.get("vcs_info"):
                vcs_info = url_metadata.get("vcs_info")
                vcs = vcs_info["vcs"]
                commit = vcs_info["commit_id"]
                url = url_metadata["url"]
                if vcs == "git":
                    # TODO: Download source + build sdist?
                    # this would allow private repos to work well
                    pip_url = f"git+{url}@{commit}"
                    return {
                        "name": dist.name,
                        "path": dist_path,
                        "source": "pip",
                        "channel": None,
                        "channel_url": None,
                        "subdir": None,
                        "conda_name": None,
                        "version": dist.version,
                        "wheel_target": pip_url,
                    }
            elif url_metadata.get("url"):
                # if the install source is actually the pre 1.2 poetry cache location
                # they this is actually just normal a pypi
                # and we can ignore direct_url.json
                if str((Path("pypoetry") / "artifacts")) not in url_metadata["url"]:
                    return {
                        "name": dist.name,
                        "path": Path(url_metadata["url"].replace("file://", "")),
                        "source": "pip",
                        "channel": None,
                        "channel_url": None,
                        "subdir": None,
                        "conda_name": None,
                        "version": dist.version,
                        "wheel_target": url_metadata["url"].replace("file://", ""),
                    }

        egg_links = []
        for location in locations:
            if os.name == "nt":
                egg_link_pth = location / Path(dist.name).with_suffix(".egg-link")
                if egg_link_pth.is_file():
                    egg_links.append(
                        location / Path(dist.name).with_suffix(".egg-link")
                    )
            else:
                egg_link_pth = location / Path(dist.name).with_suffix(".egg-link")
                if egg_link_pth.is_file():
                    egg_links.append(
                        location / Path(dist.name).with_suffix(".egg-link")
                    )
        if egg_links:
            return {
                "name": dist.name,
                "path": dist_path.parent,
                "source": "pip",
                "channel": None,
                "channel_url": None,
                "subdir": None,
                "conda_name": None,
                "version": dist.version,
                "wheel_target": str(dist_path.parent),
            }
        return {
            "name": dist.name,
            "path": dist_path,
            "source": "pip",
            "channel": None,
            "channel_url": None,
            "subdir": None,
            "conda_name": None,
            "version": dist.version,
            "wheel_target": None,
        }


async def scan_pip(
    locations: List[Path],
) -> typing.Dict[str, Union[PackageInfo, CondaPlaceHolder]]:
    # distributions returns ALL distributions
    # even ones that are not active
    # this is a trick so we only get the distribution
    # that is last in stack
    locations = [
        location for location in locations if location.exists() and location.is_dir()
    ]
    paths: List[str] = [str(location) for location in locations]
    for location in locations:
        for fp in location.iterdir():
            if fp.suffix in [".pth", ".egg-link"]:
                for line in fp.read_text().split("\n"):
                    if line.startswith("#"):
                        continue
                    elif line.startswith(("import", "import\t")):
                        continue
                    elif line.rstrip() == ".":
                        continue
                    else:
                        p = location / Path(line.rstrip())
                        full_path = str(p.resolve())
                        if p.exists() and full_path not in paths:
                            paths.append(full_path)
    active_dists: Dict[str, Distribution] = {
        dist.name: dist for dist in Distribution.discover(path=list(paths))
    }
    dists = active_dists.values()
    return {
        pkg["name"]: pkg
        for pkg in await asyncio.gather(
            *(handle_dist(dist, locations) for dist in dists)
        )
        if pkg
    }


async def scan_prefix(
    prefix: Optional[Path] = None, locations: Optional[List[Path]] = None
) -> typing.List[PackageInfo]:
    # TODO: private conda channels
    # TODO: detect pre-releases and only set --pre flag for those packages (for conda)
    if not prefix:
        prefix = Path(sys.prefix)
    conda_env_future = asyncio.create_task(scan_conda(prefix=prefix))
    # only pass locations to support testing, otherwise we should be using sys.path
    pip_env_future = asyncio.create_task(
        scan_pip(locations=locations or [Path(p) for p in sys.path])
    )
    conda_env = await conda_env_future
    pip_env = await pip_env_future
    filterd_conda = {}
    # the pip list is the "truth" of what is imported for python deps
    for name, package in conda_env.items():
        # if a package exists in the pip list but is not a conda place holder
        # then the conda package wont be imported and should be discarded
        if pip_env.get(name):
            if isinstance(pip_env[name], CondaPlaceHolder):
                filterd_conda[name] = package
            elif pip_env[name]["version"] == package["version"]:
                pip_env.pop(name, None)
                filterd_conda[name] = package
        else:
            # a non python package and safe to include
            filterd_conda[name] = package
    # remove conda placeholders
    pip_env = {
        pkg_name: pkg
        for pkg_name, pkg in pip_env.items()
        if not isinstance(pkg, CondaPlaceHolder)
    }
    return sorted(
        list(pip_env.values()) + list(filterd_conda.values()),
        key=lambda pkg: pkg["name"],
    )
