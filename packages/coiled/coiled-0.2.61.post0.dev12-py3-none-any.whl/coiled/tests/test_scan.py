import asyncio
from pathlib import Path

from coiled.scan import scan_prefix


def test_scan():
    prefix = Path(__file__).parent / "dummy-env"
    pypath = [
        prefix / "lib" / "python3.9" / "site-packages",
        prefix / "lib" / "python3.9",
    ]
    env = asyncio.run(scan_prefix(prefix=prefix, locations=pypath))
    assert env == [
        {
            "channel": "conda-forge",
            "channel_url": "https://conda.anaconda.org/conda-forge",
            "conda_name": "condapythonpackage",
            "name": "conda_python_package_python_name",
            "path": None,
            "source": "conda",
            "subdir": "noarch",
            "version": "0.1.0",
            "wheel_target": None,
        },
        {
            "channel": "conda-forge",
            "channel_url": "https://conda.anaconda.org/conda-forge",
            "conda_name": "condabinpackage",
            "name": "condabinpackage",
            "path": None,
            "source": "conda",
            "subdir": "osx-arm64",
            "version": "0.0.2",
            "wheel_target": None,
        },
        {
            "channel": None,
            "channel_url": None,
            "conda_name": None,
            "name": "dist_info_git_package",
            "source": "pip",
            "path": prefix
            / "lib"
            / "python3.9"
            / "site-packages"
            / "dist_info_git_package.dist-info",
            "subdir": None,
            "version": "0.0.10",
            "wheel_target": "git+https://github.com/dask/distributed.git@c2dfea237ffe802883b85617f20f7a7ad7b16080",
        },
        {
            "channel": None,
            "channel_url": None,
            "conda_name": None,
            "name": "dist_info_package",
            "path": prefix
            / "lib"
            / "python3.9"
            / "site-packages"
            / "dist_info_package.dist-info",
            "source": "pip",
            "subdir": None,
            "version": "0.0.11",
            "wheel_target": None,
        },
        {
            "channel": None,
            "channel_url": None,
            "conda_name": None,
            "name": "egg_info_package",
            "path": prefix
            / "lib"
            / "python3.9"
            / "site-packages"
            / "egg_info_package.egg-info",
            "source": "pip",
            "subdir": None,
            "version": "0.0.15",
            "wheel_target": None,
        },
        {
            "channel": None,
            "channel_url": None,
            "conda_name": None,
            "name": "egg_link_package",
            "source": "pip",
            "subdir": None,
            "version": "0.0.5",
            "wheel_target": str(prefix / "src" / "egg_link_package"),
            "path": prefix / "src" / "egg_link_package",
        },
        {
            "channel": None,
            "channel_url": None,
            "conda_name": None,
            "name": "egg_package",
            "path": prefix / "lib" / "python3.9" / "site-packages" / "egg_package.egg",
            "source": "pip",
            "subdir": None,
            "version": "0.0.20",
            "wheel_target": str(
                prefix / "lib" / "python3.9" / "site-packages" / "egg_package.egg"
            ),
        },
        {
            "channel": None,
            "channel_url": None,
            "conda_name": None,
            "name": "poetry_package",
            "path": Path("/some/where/over/the/rainbow"),
            "source": "pip",
            "subdir": None,
            "version": "0.0.11",
            "wheel_target": "/some/where/over/the/rainbow",
        },
        {
            "channel": None,
            "channel_url": None,
            "conda_name": None,
            "name": "pth_package",
            "path": Path("/some/where/over/the/rainbow"),
            "source": "pip",
            "subdir": None,
            "version": "0.0.25",
            "wheel_target": "/some/where/over/the/rainbow",
        },
    ]
