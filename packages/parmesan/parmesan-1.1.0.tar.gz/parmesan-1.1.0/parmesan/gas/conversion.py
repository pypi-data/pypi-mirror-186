# system modules
import logging
import warnings

# internal modules
from parmesan.gas import constants
from parmesan.errors import ParmesanWarning
from parmesan.errors import ParmesanError
from parmesan import units

# external modules
import numpy as np
import pint

logger = logging.getLogger(__name__)


@units.ensure(
    "kg / m^3",
    pressure="Pa",
    temperature="kelvin",
    particle_ratio="ratio",
    gas_constant="J / (kg * kelvin)",
)
def trace_gas_mass_density_from_particle_ratio(
    pressure,
    temperature,
    particle_ratio,
    gas_constant,
):
    r"""
    Calculate the mass density :math:`\rho_\mathrm{trace}` of a trace gas in a
    gas mixture from the particle ratio :math:`X_\mathrm{trace}`, the
    temperature :math:`T`, the pressure :math:`p` and the trace gas constant
    :math:`R_\mathrm{trace}`:

    .. math::

        \rho_\mathrm{trace} = X_\mathrm{trace} \cdot
            \frac{p}{R_\mathrm{trace} \cdot T}

    Args:
        particle_ratio: the particle ratio of the trace gas
            :math:`\frac{N_\mathrm{trace}}{N_\mathrm{total}}`. Either this
            or ``density`` needs to be specified.
        gas_constant: the trace gas' gas constant (e.g.
            taken from :mod:`parmesan.gas.constants`).

    https://gitlab.com/tue-umphy/co2mofetten/co2mofetten-project/-/wikis/Gas-Calculations
    """
    return particle_ratio * pressure / (gas_constant * temperature)


@units.ensure(
    "ratio",
    pressure="Pa",
    temperature="kelvin",
    density="kg / m^3",
    gas_constant="J / (kg * kelvin)",
)
def trace_gas_particle_ratio_from_mass_density(
    pressure,
    temperature,
    density,
    gas_constant,
):
    r"""
    Calculate the particle ratio :math:`X_\mathrm{trace}` of a trace gas in a
    gas mixture from the mass density :math:`\rho_\mathrm{trace}`, the
    temperature :math:`T`, the pressure :math:`p` and the trace gas constant
    :math:`R_\mathrm{trace}`:

    .. math::

        X_\mathrm{trace} = \rho_\mathrm{trace} \cdot
            \frac{R_\mathrm{trace} \cdot T}{p}

    Args:
        density : the mass density of the trace gas
        gas_constant: the trace gas' gas constant (e.g.  taken from
            :mod:`parmesan.gas.constants`).

    https://gitlab.com/tue-umphy/co2mofetten/co2mofetten-project/-/wikis/Gas-Calculations
    """
    return density * (gas_constant * temperature) / pressure
