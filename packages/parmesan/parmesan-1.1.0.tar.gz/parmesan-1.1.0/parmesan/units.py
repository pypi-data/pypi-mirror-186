# system modules
import functools
import textwrap
import inspect
import csv
import logging
import types
import io
import contextvars
from contextlib import contextmanager

# internal modules;-
from parmesan import utils
from parmesan.utils.mode import Mode

# external modules
import pint


logger = logging.getLogger(__name__)

mode = Mode(states={None, "implicit", "explicit"}, default="implicit")
"""
When unit mode state is set to ``"explicit"``, :func:`units.ensure` requires
that all specified arguments given to the decorated function have a
:class:`pint.unit.Unit` associated. Otherwise, an error will be raised.

With unit mode ``"implicit"`` (the default), arguments without units
automatically get the desired unit associated.

With unit mode set to ``None`` unit checking is disabled completely. Use this
if there are weird casting problems and you are sure that you provide the input
in the right unit.

It is strongly recommended to active ``explicit`` unit mode.

The unit mode can be set globally with

.. code-block:: python

    # disable unit checking
    parmesan.units.mode.state = None
    # enable automatic unit conversion
    parmesan.units.mode.state = "implicit"
    # enable explicit unit checking
    parmesan.units.mode.state = "explicit"

The unit mode can also be set temporarily for a block of code:

.. code-block:: python

    # temporarily disable unit mode
    with parmesan.units.unit_mode(None):
        # ... code here is executed with loose unit mode
"""

units = pint.UnitRegistry()
"""
The unit registry for :mod:`PARMESAN`.

This unit registry has a couple more units defined:

- fractions, ratios and percentages
- gas particle ratios like ppm, ppt, ppb

"""

units.define("fraction = [] = ratio")
units.define("percent = 1e-2 fraction = %")
units.define("ppt = 1e-3 fraction")
units.define("ppm = 1e-6 fraction")
units.define("ppb = 1e-9 fraction")


def ensure(return_unit, _units=units, **argument_units):
    """
    Decorator to transparently teach a function what :class:`pint.unit.Unit` s
    its arguments should have. Depending on the current :any:`mode`
    state, the returned function behaves differently:

    ``"implicit"`` (the default)
        Arguments to the decorated function without unit are silently turned
        into a :class:`pint.quantity.Quantity` of the specified unit.

    ``"explicit"``
        Arguments **must** be given as :class:`pint.quantity.Quantity` with a
        *compatible* unit as they will be converted to the target unit,
        otherwise a :class:`ValueError` is raised.

    ``None``
        Disable unit checking completely.

    This is an improved reimplementation of :meth:`pint.UnitRegistry.wraps`.

    A pretty-formated table detailing the units is prepended to the decorated
    function's docstring.

    Args:
        return_unit: the unit of the return value
        _units (pint.UnitRegistry, optional): the unit registry to use.
            Defaults to :any:`parmesan.units.units`.
        **argument_units: mapping of argument names to unit definitions

    Example
    =======

    .. code-block:: python

        import parmesan
        from parmesan import units

        @units.ensure(
            temperature="kelvin",
            density="kg/m^3",
            gas_constant="J / ( kg * kelvin )",
        )
        def calculate_pressure(temperature, density, gas_constant):
            # ideal gas law
            return density * gas_constant * temperature

        # arguments without units are automatically converted
        print(calculate_pressure(300, 1.2, 287).to("hPa"))
        # 1033.2 hectopascal

        # invalid units raise an error
        calculate_pressure(300 * units.pascal, 1.2, 287)
        # ValueError: pascal couldn't be converted to kelvin

        # With explicit unit mode enabled, all arguments need to have a unit
        with parmesan.units.explicit_unit_mode.enabled():
            calculate_pressure(300, 1.2, 287).to("hPa")
            # ValueError: With explicit unit mode enabled temperature=300 needs
            # to be specified with a unit compatible to 'kelvin'
    """
    for arg, unit in argument_units.items():
        try:
            _units.Unit(unit)
        except BaseException as e:
            raise ValueError(
                "{}={} is not a pint unit: {}".format(arg, repr(unit), e)
            )

    def decorator(decorated_fun):
        signature = inspect.signature(decorated_fun)

        @functools.wraps(decorated_fun)
        def wrapper(*args, **kwargs):
            if mode.state is None:
                return decorated_fun(*args, **kwargs)
            bound_args = signature.bind(*args, **kwargs)
            bound_args.apply_defaults()
            arguments = bound_args.arguments
            for arg, value in arguments.items():
                should_be_unit = argument_units.get(arg)
                if should_be_unit is None:
                    # never mind if argument was not specified
                    continue
                if not hasattr(value, "units"):
                    if mode.state == "explicit":
                        raise ValueError(
                            f"With unit mode {repr(mode.state)} "
                            f" argument {arg}={repr(value)} "
                            f"needs to be specified with a "
                            f"unit compatible to "
                            f"{units.Unit(should_be_unit).format_babel()}"
                        )
                    else:
                        try:
                            arguments[arg] = _units.Quantity(
                                getattr(value, "values", value), should_be_unit
                            )
                        except TypeError as e1:
                            try:
                                arguments[arg] = (
                                    getattr(value, "values", value)
                                    * should_be_unit
                                )
                            except BaseException as e2:
                                raise TypeError(
                                    "It is not possible to "
                                    "add a unit to this:"
                                    "\n\n{}\n\nError: {} and {}".format(
                                        repr(value), repr(e1), repr(e2)
                                    )
                                )
                        continue
                try:
                    arguments[arg] = value.to(should_be_unit)
                except BaseException as e:
                    raise ValueError(
                        f"{arg}={repr(value)} could not be converted to "
                        f"{units.Unit(should_be_unit).format_babel()}: {e}"
                    )
            return_value = decorated_fun(**arguments)
            if mode.state is not None:
                if hasattr(return_value, "to"):
                    return return_value.to(return_unit)
                elif return_unit is None:
                    return return_value
                else:
                    return units.Quantity(return_value, return_unit)
            else:
                return return_value

        docbuf = io.StringIO()
        writer = csv.DictWriter(
            docbuf,
            fieldnames=["Argument", "Unit"],
            quoting=csv.QUOTE_ALL,
            lineterminator="\n",
        )
        docbuf.write(":header: ")
        writer.writeheader()
        docbuf.write("\n")

        for arg, unit in argument_units.items():
            writer.writerow(
                {
                    "Argument": "``{}``".format(arg),
                    "Unit": ":math:`{}`".format(
                        r"{:~L}".format(_units.Unit(unit))
                        or r"\mathrm{unitless}"
                    ),
                }
            )

        wrapper.__doc__ = utils.string.add_to_docstring(
            docstring=getattr(wrapper, "__doc__", "") or "",
            extra_doc=(
                textwrap.dedent(
                    """

            .. csv-table:: {title}. Arguments are supposed to be given in the
                below units:
            {csv_table}

            """
                )
                if argument_units
                else "{title}"
            ).format(
                title="This function is decorated with "
                ":any:`units.ensure` and returns values "
                "with unit :math:`{return_unit}`".format(
                    return_unit="{:~L}".format(_units.Unit(return_unit))
                    or r"\mathrm{unitless}"
                ),
                csv_table=textwrap.indent(docbuf.getvalue(), prefix="    "),
            ),
            prepend=True,
        )

        return wrapper

    return decorator


@functools.wraps(ensure)
def ensure_monkeypatched(self, *args, **kwargs):
    return ensure(*args, _units=self, **kwargs)


# Add ensure() as method by monkey-patching
units.ensure = types.MethodType(ensure_monkeypatched, units)
