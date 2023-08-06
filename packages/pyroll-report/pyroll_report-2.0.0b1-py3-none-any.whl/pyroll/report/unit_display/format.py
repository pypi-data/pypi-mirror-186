from typing import Sequence

import numpy as np

from pyroll.core.repr import ReprMixin
from pyroll.report.pluggy import hookimpl, plugin_manager
from .properties import render_properties_table, DoNotPrint
import shapely.geometry


def _is_float_like(value: object):
    return isinstance(value, float) or (
            isinstance(value, np.ndarray) and np.isscalar(value) and np.issubdtype(value.dtype, np.floating))


@hookimpl(specname="property_format", trylast=True)
def default_format(value: object):
    return str(value)


@hookimpl(specname="property_format")
def int_format(value: object):
    if isinstance(value, int):
        return "{:d}".format(value)


@hookimpl(specname="property_format")
def float_format(value: object):
    if _is_float_like(value):
        order = np.log10(np.abs(value)) // 3
        if not np.isfinite(order):
            return np.format_float_positional(value)
        exp = int(order) * 3
        mantissa = value / 10 ** exp
        return f"{np.format_float_positional(mantissa, trim='0', precision=3)}e{exp:+03d}"


@hookimpl(specname="property_format")
def temperature_format(name: str, value: object):
    if _is_float_like(value) and "temperature" in name:
        return np.format_float_positional(value, precision=1)


@hookimpl(specname="property_format")
def strain_format(name: str, value: object):
    if _is_float_like(value) and (
            "strain" in name
            or "elongation" in name
            or "draught" in name
            or "spread" in name
    ):
        return np.format_float_positional(value, precision=4)


@hookimpl(specname="property_format")
def array_format(value: object):
    if isinstance(value, np.ndarray):
        return np.array_str(value)


@hookimpl(specname="property_format")
def repr_mixin_format(value: object):
    if isinstance(value, ReprMixin):
        return f"""
        <details open>
        <summary>{str(value)}</summary>
            <div>
                {render_properties_table(value)}
            </div>
        </details>
        """


@hookimpl(specname="property_format")
def shapely_format(value: object):
    if isinstance(value, (shapely.geometry.Polygon, shapely.geometry.LineString)):
        # noinspection PyTypeChecker
        return f"""
        <details open>
            <summary>{str(value)}</summary>
            <div>
                {render_properties_table(value)}
            </div>
        </details>
        """


@hookimpl(specname="property_format")
def disk_elements_format(name: str, value: object):
    if isinstance(value, Sequence) and name == "disk_elements":
        displays = "\n".join(
            [
                d
                for u in value
                for d in plugin_manager.hook.unit_display(unit=u, level=6)
            ]
        )

        if displays:
            return f"""
            <details>
                <summary>Disk Elements (click to expand)</summary>
                <div>
                    {displays}
                </div>
            </details>
            """

        raise DoNotPrint()


@hookimpl(specname="property_format")
def do_not_print_units(name: str):
    if name == "units":
        raise DoNotPrint()


@hookimpl(specname="property_format")
def do_not_print_label(name: str):
    if name == "label":
        raise DoNotPrint()
