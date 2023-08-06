import asyncio
import logging
import pkgutil
import sys
from logging import basicConfig
from pathlib import Path

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from coiled.scan import scan_prefix


@click.group()
def package_sync():
    basicConfig(level=logging.INFO)


@package_sync.command
def scan():
    result = asyncio.run(scan_prefix(Path(sys.prefix)))
    table = Table(title="Packages")
    table.add_column("Package Name", style="cyan", no_wrap=True)
    table.add_column("Version", style="magenta")
    table.add_column("Source", style="magenta")
    table.add_column("Wheel target", style="green", overflow="fold")
    table.add_column("Path", overflow="fold")
    table.add_column("Can build wheel", style="green")
    rows = []
    for pkg in result:
        rows.append(
            (
                pkg["name"],
                pkg["version"],
                pkg["source"],
                str(pkg["wheel_target"] or ""),
                str(pkg["path"]),
                "true",
            )
        )

    for (_, name, ispkg) in pkgutil.iter_modules(path=["."]):
        will_sync = False
        if ispkg:
            for pkg in result:
                if pkg["path"]:
                    if (pkg["path"] / name).resolve() == (Path(".") / name).resolve():  # type: ignore
                        will_sync = True
        if not will_sync:
            rows.append(
                (
                    name,
                    "",
                    "cwd",
                    "",
                    str(Path(".") / name)
                    if ispkg
                    else str((Path(".") / name).with_suffix(".py")),
                    "[red]false[/red]",
                )
            )
    for row in sorted(rows, key=lambda x: (x[5], x[0].lower())):
        table.add_row(*row)
    console = Console()
    console.print(table)
    console.print(
        Panel(
            "[yellow]Warning: You have importable code in your path"
            " which won't be available on your cluster because we're"
            " unable to build wheel.[/yellow]"
        )
    )


@package_sync.command
def debug():
    table = Table(title="Debug")
    table.add_column("Path", no_wrap=True, overflow="fold")
    rows = []
    for path in sys.path:
        p = Path(path)
        if p.is_dir():
            for file in p.iterdir():
                rows.append(str(file))
        else:
            rows.append(str(p))
    rows = sorted(rows)
    for row in rows:
        table.add_row(row)
    console = Console()
    console.print(table)
