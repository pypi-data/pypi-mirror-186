# system modules
import warnings

# internal modules
from parmesan.errors import ParmesanWarning
from parmesan.units import units
from parmesan import bounds
from parmesan import utils
from parmesan.gas import constants
from parmesan.utils.function import FunctionCollection

# external modules
import pint
import numpy as np


absolute_humidity = FunctionCollection()
r"""
Collection of functions to calculate absolute humidity :math:`\rho_\mathrm{w}`
"""


@absolute_humidity.register
@units.ensure(
    "kg / m^3",
    water_vapour_pressure="Pa",
    temperature="kelvin",
)
@bounds.ensure(
    (0, None),
    water_vapour_pressure=(0, None),
    temperature=(0, None),
)
def absolute_humidity_from_water_vapour_pressure(
    water_vapour_pressure, temperature
):
    r"""
    Calculate the absolute humidity :math:`\rho_\mathrm{w}` from water vapour
    pressure :math:`e` and temperature :math:`T`:

    .. math::

        \rho_\mathrm{w} = \frac{e}{R_\mathrm{H_2O} \cdot T}
    """
    return water_vapour_pressure / (
        constants.GAS_CONSTANT_WATER_VAPOUR * temperature
    )


@absolute_humidity.register
@units.ensure(
    "kg / m^3",
    relative_humidity="ratio",
    temperature="kelvin",
)
@bounds.ensure(
    (0, None),
    relative_humidity=(0, 1),
    temperature=(0, None),
)
def absolute_humidity_from_relative_humidity(relative_humidity, temperature):
    r"""
    Like :func:`absolute_humidity_from_water_vapour_pressure`, but use
    :func:`water_vapour_pressure_over_water_magnus` to calculate the water
    vapour pressure :math:`e` from relative humidity :math:`RH`:

    .. math::

        \rho_\mathrm{w} = \frac{RH \cdot e_\mathrm{s,Magnus}\left(T\right)}
            {R_\mathrm{H_2O} \cdot T}
    """
    return absolute_humidity_from_water_vapour_pressure(
        water_vapour_pressure=water_vapour_pressure_over_water_magnus(
            relative_humidity=relative_humidity, temperature=temperature
        ),
        temperature=temperature,
    )


@absolute_humidity.register
@units.ensure(
    "kg / m^3",
    dewpoint_temperature="kelvin",
)
@bounds.ensure(
    (0, None),
    dewpoint_temperature=(0, None),
)
def absolute_humidity_from_dewpoint(dewpoint_temperature):
    r"""
    Calculate the absolute humidity :math:`\rho_\mathrm{w}` from the dewpoint
    temperature :math:`T_\mathrm{d}` like
    :func:`absolute_humidity_from_water_vapour_pressure` using
    :func:`saturation_water_vapour_pressure_over_water_magnus`:

    .. math::

        \rho_\mathrm{w} = \frac
            {e_\mathrm{s,Magnus}\left(T_\mathrm{d}\right)}
            {R_\mathrm{H_2O} \cdot T_\mathrm{d}}
    """
    return absolute_humidity_from_water_vapour_pressure(
        water_vapour_pressure=(
            saturation_water_vapour_pressure_over_water_magnus(
                temperature=dewpoint_temperature
            )
        ),
        temperature=dewpoint_temperature,
    )


specific_humidity = FunctionCollection()
"""
Collection of functions to calculate specific humidity :math:`q`
"""


@specific_humidity.register
@units.ensure("ratio", absolute_humidity="kg / m^3", density="kg / m^3")
@bounds.ensure(
    (0, 1),
    absolute_humidity=bounds.smaller_than("density"),
    density=(0, None),
)
def specific_humidity_via_densities(absolute_humidity, density):
    r"""
    Calculate the specific humidty :math:`q` from absolute humidity
    :math:`\rho_\mathrm{w}` and humid air density
    :math:`\rho_\mathrm{air,humit}` (including the water vapour):

    .. math::

        q = \frac{\rho_\mathrm{w}}{\rho_\mathrm{air,humid}}

    Args:
        absolute_humidity (numeric): the absolute humidity
        density (numeric): the density of the humid air

    https://de.wikipedia.org/wiki/Luftfeuchtigkeit#Spezifische_Luftfeuchtigkeit
    """
    return absolute_humidity / density


@specific_humidity.register
@units.ensure(
    "ratio",
    water_vapour_mass="kg",
    air_mass="kg",
)
@bounds.ensure(
    (0, 1),
    water_vapour_mass=bounds.smaller_than("air_mass"),
    air_mass=(0, None),
)
def specific_humidity_via_masses(water_vapour_mass, air_mass):
    r"""
    Calculate the specific humidity :math:`q` given the masses of
    water vapour :math:`m_\mathrm{w}` and humid air
    :math:`\rho_\mathrm{air,humid}`:

    .. math::

        q = \frac{m_\mathrm{w}}{m_\mathrm{air,humid}}

    https://de.wikipedia.org/wiki/Luftfeuchtigkeit#Spezifische_Luftfeuchtigkeit
    """
    return water_vapour_mass / air_mass


@specific_humidity.register
@units.ensure(
    "ratio",
    water_vapour_pressure="Pa",
    pressure="Pa",
)
@bounds.ensure(
    (0, 1),
    water_vapour_pressure=bounds.smaller_than("pressure"),
    pressure=(0, None),
)
def specific_humidity_via_pressures(water_vapour_pressure, pressure):
    r"""
    Calculate the specific humidity :math:`q` given the water vapour pressure
    :math:`e` and the atmospheric pressure :math:`p` and the molar masses for
    water vapour :math:`M_\mathrm{H_2O}` and dry air :math:`M_\mathrm{dry
    air}`:

    .. math::

        q = \frac
            { \frac{M_\mathrm{H_2O}}{M_\mathrm{dry air}} \cdot e }
            { p -
                \left( 1-\frac{M_\mathrm{H_2O}}{M_\mathrm{dry air}} \right)
                \cdot e }

    https://de.wikipedia.org/wiki/Luftfeuchtigkeit#Spezifische_Luftfeuchtigkeit
    """
    ratio = constants.MOLAR_MASS_WATER_VAPOUR / constants.MOLAR_MASS_DRY_AIR
    return (ratio * water_vapour_pressure) / (
        pressure - (1 - ratio) * water_vapour_pressure
    )


@specific_humidity.register
@units.ensure(
    "ratio",
    relative_humidity="fraction",
    temperature="kelvin",
    pressure="Pa",
)
@bounds.ensure(
    (0, 1),
    relative_humidity=(0, 1),
    pressure=(0, None),
    temperature=(0, None),
)
def specific_humidity_via_relative_humidity(
    relative_humidity, pressure, temperature
):
    r"""
    Like :func:`specific_humidity_via_pressures` but calculate the water vapour
    pressure from the relative humidity via
    :func:`water_vapour_pressure_over_water_magnus`.

    https://de.wikipedia.org/wiki/Luftfeuchtigkeit#Spezifische_Luftfeuchtigkeit
    """
    return specific_humidity_via_pressures(
        water_vapour_pressure=water_vapour_pressure_over_water_magnus(
            relative_humidity=relative_humidity,
            temperature=temperature,
        ),
        pressure=pressure,
    )


mixing_ratio = FunctionCollection()
"""
Collection of functions to calculate the mixing ratio
"""


@mixing_ratio.register
@units.ensure(
    "ratio",
    absolute_humidity="kg/m^3",
    density="kg/m^3",
)
@bounds.ensure(
    (0, 1),
    absolute_humidity=bounds.smaller_than("density"),
    density=(0, None),
)
def mixing_ratio_via_humid_densities(absolute_humidity, density):
    r"""
    Calculate the mixing ratio :math:`r` given the absolute humidity
    :math:`\rho_\mathrm{w}` and the density of the humid air
    :math:`\rho_\mathrm{air,humid}`:

    .. math::

        r = \frac
            {\rho_\mathrm{w}}
            {\rho_\mathrm{air,humid} - \rho_\mathrm{w}}

    https://de.wikipedia.org/wiki/Luftfeuchtigkeit#Mischungsverh%C3%A4ltnis
    """
    return absolute_humidity / (density - absolute_humidity)


@mixing_ratio.register
@units.ensure(
    "ratio",
    water_vapour_mass="kg",
    air_mass="kg",
)
@bounds.ensure(
    (0, 1),
    water_vapour_mass=bounds.smaller_than("air_mass"),
)
def mixing_ratio_via_masses(water_vapour_mass, air_mass):
    r"""
    Calculate the mixing ratio :math:`r` given the masses of
    water vapour :math:`m_\mathrm{w}` and humid air
    :math:`\rho_\mathrm{air,humid}`:

    .. math::

        r = \frac{m_\mathrm{w}}{m_\mathrm{air,humid} - m_\mathrm{w}}

    https://de.wikipedia.org/wiki/Luftfeuchtigkeit#Mischungsverh%C3%A4ltnis
    """
    return water_vapour_mass / (air_mass - water_vapour_mass)


@mixing_ratio.register
@units.ensure(
    "ratio",
    water_vapour_pressure="Pa",
    pressure="Pa",
)
@bounds.ensure(
    [0, 1],
    water_vapour_pressure=bounds.smaller_than("pressure"),
)
def mixing_ratio_via_pressures(water_vapour_pressure, pressure):
    r"""
    Calculate the mixing ratio :math:`r` given the water vapour pressure
    :math:`e` and the atmospheric pressure :math:`p` using the molar masses for
    water vapour :math:`M_\mathrm{H_2O}` and dry air :math:`M_\mathrm{dry
    air}`:

    .. math::

        r = \frac{M_\mathrm{H_2O}}{M_\mathrm{dry air}}
            \cdot
            \frac{e}{p - e}

    https://de.wikipedia.org/wiki/Luftfeuchtigkeit#Mischungsverh%C3%A4ltnis
    """
    return (
        constants.MOLAR_MASS_WATER_VAPOUR
        / constants.MOLAR_MASS_DRY_AIR
        * water_vapour_pressure
        / (pressure - water_vapour_pressure)
    )


@mixing_ratio.register
@units.ensure(
    "ratio",
    relative_humidity="fraction",
    pressure="Pa",
    temperature="K",
)
@bounds.ensure(
    (0, 1),
    relative_humidity=(0, 1),
    pressure=(0, None),
    temperature=(0, None),
)
def mixing_ratio_via_relative_humidity(
    relative_humidity, pressure, temperature
):
    r"""
    Like :func:`mixing_ratio_via_pressures` but use
    :func:`water_vapour_pressure_over_water_magnus` to calculate the water
    vapor pressure from the relative humidity.
    """
    return mixing_ratio_via_pressures(
        water_vapour_pressure=water_vapour_pressure_over_water_magnus(
            relative_humidity=relative_humidity, temperature=temperature
        ),
        pressure=pressure,
    )


saturation_water_vapour_pressure = FunctionCollection()
"""
Collection of functions to calculate the saturation water vapour pressure
"""


@saturation_water_vapour_pressure.register
@units.ensure(
    "Pa",
    temperature="kelvin",
)
@bounds.ensure(
    (0, None),
    temperature=(
        units.Quantity(-45, "celsius").to("kelvin").m,
        units.Quantity(60, "celsius").to("kelvin").m,
    ),
)
def saturation_water_vapour_pressure_over_water_magnus(
    temperature, over_water=True
):
    """
    Water vapour saturation pressure over flat water according to the
    Magnus-formula

    Args:
        temperature: the temperature
        over_water (bool, optional): unused dummy argument to distinguish from
            :func:`saturation_water_vapour_pressure_over_ice_magnus` when
            calling via :any:`saturation_water_vapour_pressure`.

    - https://de.wikipedia.org/wiki/S%C3%A4ttigungsdampfdruck
    - WMO's `Guide to Meteorological Instruments and Methods of
      Observation <https://www.weather.gov/media/epz/mesonet/CWOP-WMO8.pdf>`_
    """
    # get temperature magnitude in °C
    temperature = (
        (
            temperature
            if hasattr(temperature, "to")
            else (temperature * units.kelvin)
        )
        .to("celsius")
        .magnitude
    )
    return (6.112 * units.hPa).to("Pa") * np.exp(
        17.62 * temperature / (243.12 + temperature)
    )


@units.ensure(
    "kelvin",
    water_vapour_pressure="Pa",
)
@bounds.ensure(
    (
        units.Quantity(-45, "celsius").to("kelvin").m,
        units.Quantity(60, "celsius").to("kelvin").m,
    ),
    water_vapour_pressure=(0, None),
)
def temperature_from_e_magnus_over_water(
    water_vapour_pressure,
):
    """
    Inversion of :func:`saturation_water_vapour_pressure_over_water_magnus`

    - see WMO's `Guide to Meteorological Instruments and Methods of
      Observation <https://www.weather.gov/media/epz/mesonet/CWOP-WMO8.pdf>`_
    """
    water_vapour_pressure = (
        (
            water_vapour_pressure
            if hasattr(water_vapour_pressure, "to")
            else (water_vapour_pressure * units.Pa)
        )
        .to("Pa")
        .magnitude
    )
    d = np.log(water_vapour_pressure / 611.2)
    return units.Quantity((243.12 * d / (17.62 - d)), "celsius").to("kelvin")


@saturation_water_vapour_pressure.register
@units.ensure(
    "Pa",
    temperature="kelvin",
)
@bounds.ensure(
    (0, None),
    temperature=(
        units.Quantity(-65, "celsius").to("kelvin").m,
        units.Quantity(0.01, "celsius").to("kelvin").m,
    ),
)
def saturation_water_vapour_pressure_over_ice_magnus(
    temperature, over_ice=True
):
    """
    Water vapour saturation pressure over flat ice according to the
    Magnus-formula

    Args:
        temperature: the temperature
        over_ice (bool, optional): unused dummy argument to distinguish from
            :func:`saturation_water_vapour_pressure_over_water_magnus` when
            calling via :any:`saturation_water_vapour_pressure`.

    - https://de.wikipedia.org/wiki/S%C3%A4ttigungsdampfdruck
    - WMO's `Guide to Meteorological Instruments and Methods of
      Observation <https://www.weather.gov/media/epz/mesonet/CWOP-WMO8.pdf>`_
    """
    # get temperature magnitude in °C
    temperature = (
        (
            temperature
            if hasattr(temperature, "to")
            else (temperature * units.kelvin)
        )
        .to("celsius")
        .magnitude
    )
    return (6.112 * units.hPa).to("Pa") * np.exp(
        22.46 * temperature / (272.62 + temperature).magnitude
    )


water_vapour_pressure = FunctionCollection()
"""
Collection of functions to calculate water vapour pressure
"""


@water_vapour_pressure.register
@units.ensure(
    "Pa",
    relative_humidity="fraction",
    temperature="kelvin",
)
@bounds.ensure(
    (0, None),
    relative_humidity=(0, 1),
    temperature=(0, None),
)
def water_vapour_pressure_over_water_magnus(relative_humidity, temperature):
    r"""
    Calculate water vapour pressure :math:`e` from relative humidity and
    temperature :math:`T` via the saturation water vapour pressure (using
    :func:`saturation_water_vapour_pressure_over_water_magnus`):

    .. math::

        e = RH \cdot e_\mathrm{s,Magnus}\left(T\right)
    """
    return (
        relative_humidity
        * saturation_water_vapour_pressure_over_water_magnus(temperature)
    )


@water_vapour_pressure.register
@units.ensure(
    "Pa",
    absolute_humidity="kg / m^3",
    temperature="kelvin",
)
@bounds.ensure(
    (0, None),
    absolute_humidity=(0, None),
    temperature=(0, None),
)
def water_vapour_pressure_via_gas_law(absolute_humidity, temperature):
    r"""
    Calculate the water vapour pressure :math:`e` using the absolute humdity
    :math:`\rho_\mathrm{w}` and the temperature :math:`T` according to the
    ideal gas law with the specific gas constant for water vapour
    :math:`R_\mathrm{H_2O}` (:any:`GAS_CONSTANT_WATER_VAPOUR`):

    .. math::

        e = \rho_\mathrm{w} \cdot R_\mathrm{H_2O} \cdot T
    """
    return (
        absolute_humidity * constants.GAS_CONSTANT_WATER_VAPOUR * temperature
    )


relative_humidity = FunctionCollection()
"""
Collection of functions to calculate relative humidity
"""


@relative_humidity.register
@units.ensure(
    "ratio",
    temperature="kelvin",
    water_vapour_pressure="Pa",
)
@bounds.ensure(
    (0, 1),
    water_vapour_pressure=(0, None),
    temperature=(0, None),
)
def relative_humidity_via_water_vapour_pressure(
    water_vapour_pressure, temperature
):
    r"""
    Calculate relative humidity :math:`RH` from water vapour pressure :math:`e`
    and the saturation water vapour pressure :math:`e_\mathrm{s,Magnus}(T)`
    using :func:`saturation_water_vapour_pressure_over_water_magnus`:

    .. math::

        RH = \frac{e}{e_\mathrm{s,Magnus}(T)}
    """
    return (
        water_vapour_pressure
        / saturation_water_vapour_pressure_over_water_magnus(temperature)
    )


@relative_humidity.register
@units.ensure(
    "ratio",
    dewpoint_temperature="kelvin",
    temperature="kelvin",
)
@bounds.ensure(
    (0, 1),
    dewpoint_temperature=bounds.smaller_than("temperature"),
    temperature=(0, None),
)
def relative_humidity_via_dewpoint(
    dewpoint_temperature,
    temperature,
):
    r"""
    Calculate relative humidity :math:`RH` from dewpoint temperature
    :math:`T_\mathrm{d}` and temperature :math:`T`:

    .. math::

        RH = \frac{T}{T_\mathrm{d}} \cdot
            \frac{e_\mathrm{s,Magnus}\left(T_\mathrm{d}\right)}
                 {e_\mathrm{s,Magnus}\left(T\right)}
    """
    return (temperature / dewpoint_temperature) * (
        saturation_water_vapour_pressure_over_water_magnus(
            temperature=dewpoint_temperature
        )
        / saturation_water_vapour_pressure_over_water_magnus(
            temperature=temperature
        )
    )


dewpoint = FunctionCollection()
"""
Collection of functions to calculate the dew point
"""


@dewpoint.register
@units.ensure(
    "kelvin",
    temperature="kelvin",
    relative_humidity="fraction",
)
@bounds.ensure(
    (0, None),
    temperature=(0, None),
    relative_humidity=(0, 1),
)
def dewpoint_from_relative_humidity(relative_humidity, temperature):
    r"""
    Calculate the dew point :math:`T_\mathrm{d}` from relative humidity
    :math:`RH` and temperature :math:`T`:

    .. math::

        T_\mathrm{d} = \frac
            {B\left[\mathrm{ln}\left(RH\right) + \frac{A \cdot T}{B+T}\right]}
            {A - \mathrm{ln}\left(RH\right) - \frac{A\cdot T}{B+T}}


    From `Lawrence (2005) <https://doi.org/10.1175/BAMS-86-2-225>`_ (parameter
    A seems to be missing a leading ``1`` there)

    .. warning::

        This doesn't seem to be a perfect inversion of
        :func:`relative_humidity_via_dewpoint`, round-tripping doesn't yield
        the exact same result (c.f. the tests).

        Neither `WolframAlpha
        <https://www.wolframalpha.com/input/?i=solve+exp%28%28bD%29%2F%28c%2BD%29%29%2FD+%3D+R+*+exp%28%28bT%29%2F%28c%2BT%29%29%2FT+for+real+D%2Cb%3D17.62>`_
        nor `SymPyGamma
        <https://sympygamma.com/input/?i=solve%28a*exp%28%28b*T%29%2F%28c%2BT%29%29%2FT+-+X%2CT%29>`_
        seem to be able to invert the equation analytically.

        If you need to calculate the dewpoint temperature from relative
        humidity more precisely, consider inverting
        :func:`relative_humidity_via_dewpoint` numerically and use/implement a
        more precise approximation than
        :func:`saturation_water_vapour_pressure_over_water_magnus`.
    """
    # get temperature magnitude in °C
    temperature = (
        (
            temperature
            if hasattr(temperature, "to")
            else (temperature * units.kelvin)
        )
        .to("celsius")
        .magnitude
    )
    A = 17.625
    B = 243.04
    frac = (A * temperature) / (B + temperature)
    log = np.log(relative_humidity.magnitude)
    dewpoint = (B * (log + frac)) / (A - log - frac)
    return units.Quantity(dewpoint, "celsius").to("kelvin")
