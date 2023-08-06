# system modules
import logging
import warnings

# internal modules
from parmesan.gas import constants
from parmesan.gas import humidity
from parmesan.errors import ParmesanWarning
from parmesan.errors import ParmesanError
from parmesan import units
from parmesan import bounds
from parmesan import utils
from parmesan.utils.function import FunctionCollection

# external modules
import numpy as np
import pint

logger = logging.getLogger(__name__)


virtual_temperature = FunctionCollection()
"""
Collection of functions to calculate virtual temperature
"""


@virtual_temperature.register
@units.ensure(
    "kelvin",
    temperature="kelvin",
    specific_humidity="kg/kg",
)
@bounds.ensure(
    (0, None),
    temperature=(0, None),
    specific_humidity=(0, 1),
)
def virtual_temperature_from_specific_humidity(temperature, specific_humidity):
    r"""
    Calculate the virtual temperature :math:`T_\mathrm{v}` via the
    specific_humidity :math:`q`:

    .. math::

        T_\mathrm{v} = T \cdot
            \left( 1 +
                \left(
                \frac{R_\mathrm{w}}{R_\mathrm{dry air}}
                - 1
                \right) \cdot q
            \right)

    """
    return temperature * (
        1
        + (
            constants.GAS_CONSTANT_WATER_VAPOUR
            / constants.GAS_CONSTANT_DRY_AIR
            - 1
        )
        * specific_humidity
    )


@virtual_temperature.register
@units.ensure(
    "kelvin",
    temperature="kelvin",
    mixing_ratio="ratio",
)
@bounds.ensure(
    (0, None),
    temperature=(0, None),
    mixing_ratio=(0, 1),
)
def virtual_temperature_from_mixing_ratio(temperature, mixing_ratio):
    r"""
    Calculate the virtual temperature :math:`T_\mathrm{v}` via the
    mixing_ratio :math:`r`:

    .. math::

        T_\mathrm{v} = T \cdot
            \frac{r + \frac{R_\mathrm{dry air}}{R_\mathrm{w}}}
                 {
                 \frac{R_\mathrm{dry air}}{R_\mathrm{w}}
                 \cdot \left( 1 + r \right)
                 }

    https://en.wikipedia.org/wiki/Virtual_temperature#Variations
    """
    ratio = (
        constants.GAS_CONSTANT_DRY_AIR / constants.GAS_CONSTANT_WATER_VAPOUR
    )
    return temperature * (mixing_ratio + ratio) / (ratio * (1 + mixing_ratio))


@virtual_temperature.register
@units.ensure(
    "kelvin",
    temperature="kelvin",
    pressure="Pa",
    water_vapour_pressure="Pa",
)
@bounds.ensure(
    (0, None),
    temperature=(0, None),
    water_vapour_pressure=utils.doc(
        (lambda x, pressure, *a, **kw: x <= pressure), "smaller than pressure"
    ),
    pressure=(0, None),
)
def virtual_temperature_from_pressures(
    temperature, pressure, water_vapour_pressure
):
    r"""
    Calculate the virtual temperature :math:`T_\mathrm{v}` via the
    atmospheric pressure :math:`p`, and the water vapour pressure :math:`e`:

    .. math::

        T_\mathrm{v} = \frac{T}{
            1 - \frac{e}{p} \cdot
            \left( 1 - \frac{R_\mathrm{dry air}}{R_\mathrm{w}} \right)
            }

    https://en.wikipedia.org/wiki/Virtual_temperature#Variations
    """

    return temperature / (
        1
        - water_vapour_pressure
        / pressure
        * (
            1
            - constants.GAS_CONSTANT_DRY_AIR
            / constants.GAS_CONSTANT_WATER_VAPOUR
        )
    )


@virtual_temperature.register
@units.ensure(
    "kelvin",
    temperature="kelvin",
    pressure="Pa",
    relative_humidity="ratio",
)
@bounds.ensure(
    (0, None),
    pressure=(0, None),
    relative_humidity=(0, 1),
)
def virtual_temperature_from_relative_humidity(
    temperature, pressure, relative_humidity
):
    """
    Like :func:`virtual_temperature_from_pressures` but use
    :func:`water_vapour_pressure_over_water_magnus` to calculate the water
    vapour pressure.
    """
    return virtual_temperature_from_pressures(
        temperature=temperature,
        pressure=pressure,
        water_vapour_pressure=humidity.water_vapour_pressure_over_water_magnus(
            temperature=temperature,
            relative_humidity=relative_humidity,
        ),
    )


@units.ensure(
    "kelvin",
    pressure="Pa",
    reference_pressure="Pa",
    temperature="kelvin",
    gas_constant="J / (kg*kelvin)",
    specific_isobaric_heat_capacity="J / (kg*kelvin)",
)
@bounds.ensure(
    (0, None),
    pressure=(0, None),
    reference_pressure=(0, None),
    gas_constant=(0, None),
    specific_isobaric_heat_capacity=(0, None),
)
def potential_temperature(
    temperature,
    pressure,
    reference_pressure=(1000 * units.units.hPa).to("Pa"),
    gas_constant=constants.GAS_CONSTANT_DRY_AIR,
    specific_isobaric_heat_capacity=(
        constants.SPECIFIC_ISOBARIC_HEAT_CAPACITY_DRY_AIR
    ),
):
    r"""
    Calculate the potential temperature.

    The defaults assume dry air.

    .. math::

        \Theta = T \cdot \left( \frac{p_\mathrm{ref}}{p} \right) ^
        {\left(\frac{R_\mathrm{gas}}{c_\mathrm{p}}\right)}

    Args:
        temperature (numeric): air temperature
        pressure (numeric): air pressure
        reference_pressure (numeric, optional): the reference pressure to which
            to adiabatically move the air parcel.
        gas_constant (numeric, optional): the specific gas constant of the gas.
            Defaults to dry air.
        specific_isobaric_heat_capacity (numeric, optional): the specific
            isobaric heat capacity of the gas. Defaults to dry air.

    Returns:
        pint.quantity.Quantity : the potential temperature
    """
    return temperature * (reference_pressure / pressure) ** (
        gas_constant / specific_isobaric_heat_capacity
    )
