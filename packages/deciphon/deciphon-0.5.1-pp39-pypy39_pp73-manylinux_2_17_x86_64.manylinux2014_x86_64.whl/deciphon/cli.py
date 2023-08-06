from __future__ import annotations

from enum import IntEnum
from pathlib import Path
from typing import Optional

import typer
from blx.meta import __version__
from rich.progress import track

from deciphon.press import Press
from deciphon.service_exit import ServiceExit, register_service_exit

__all__ = ["app"]


class EXIT_CODE(IntEnum):
    SUCCESS = 0
    FAILURE = 1


app = typer.Typer(add_completion=False)

PROGRESS_OPTION = typer.Option(
    True, "--progress/--no-progress", help="Display progress bar."
)


@app.callback(invoke_without_command=True)
def cli(version: Optional[bool] = typer.Option(None, "--version", is_eager=True)):
    if version:
        print(__version__)
        raise typer.Exit()


@app.command()
def press(hmm: Path, progress: bool = PROGRESS_OPTION):
    """
    Press HMM into DCP.
    """
    register_service_exit()

    try:
        dcp = Path(hmm.stem + ".dcp")
        with Press(hmm, dcp) as press:
            for _ in track(press, "Press", disable=not progress):
                pass
    except ServiceExit:
        raise typer.Exit(EXIT_CODE.FAILURE)

    raise typer.Exit(EXIT_CODE.SUCCESS)
