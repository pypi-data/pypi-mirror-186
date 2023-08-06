import logging
from pathlib import Path

from .report import report as report_func
from pyroll.cli import main, State
import click

DEFAULT_REPORT_FILE = "report.html"


@click.command()
@click.option(
    "-f", "--file",
    help="File to write to.",
    type=click.Path(dir_okay=False, path_type=Path),
    default=DEFAULT_REPORT_FILE, show_default=True
)
@click.pass_obj
def report(state: State, file: Path):
    """Generates a HTML report from the simulation results and writes it to FILE."""
    log = logging.getLogger(__name__)

    rendered = report_func(state.sequence)

    file.write_text(rendered, encoding='utf-8')
    log.info(f"Wrote report to: {file.absolute()}")
