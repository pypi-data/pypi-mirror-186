# mypy: disable-error-code = misc
from typer import Exit
from typer import Typer

from .plot import plot_events


events = Typer()


@events.command()
def plot(check: bool = False) -> None:
    if plot_events(check):
        raise Exit(code=1)
