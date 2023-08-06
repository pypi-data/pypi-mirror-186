from typing import Union

from matplotlib.figure import Figure

from pyroll.report.pluggy import hookspec
from pyroll.core import Unit


@hookspec
def unit_display(unit: Unit, level: int) -> str:
    """Return HTML code as str which displays the given unit.
    Multiple implementations will be included sequentially into the report.
    Other return types as HTML str are possible, if respective hook wrappers for conversion exist."""


@hookspec
def unit_plot(unit: Unit) -> Union[Figure, str]:
    """Generate a matplotlib figure or SVG code visualizing a unit.
    All loaded hook implementations are listed in the report."""


@hookspec(firstresult=True)
def property_format(name: str, value: object) -> str:
    """Format the value of a property as string for display in the report. This hook is first result."""
