# system modules

# internal modules
from parmesan.units import units
from parmesan import bounds
from parmesan.radiation import constants

# external modules


@units.ensure(
    "watt / m**2",
    temperature="kelvin",
)
@bounds.ensure(
    (0, None),
    temperature=(0, None),
)
def blackbody_radiation(temperature):
    r"""
    Calculate the total emitted radiation for a blackbody surface at a given
    temperature according to the Stefan-Boltzmann law:

    .. math::

        I_\mathrm{total} = \sigma \, T ^ 4

    Args:
        temperature (numeric): the temperature of the blackbody

    Returns:
        numpy.ndarray : the total emitted blackbody radiation
        :math:`\left[I_\mathrm{total}\right] = \frac{W}{m^2}`
    """
    return constants.STEFAN_BOLTZMANN_CONSTANT * temperature**4


@units.ensure(
    "kelvin",
    temperature="kelvin",
    temperature_ambient="kelvin",
    emissivity_new="dimensionless",
    emissivity_old="dimensionless",
)
@bounds.ensure(
    (0, None),
    temperature=(0, None),
    temperature_ambient=(0, None),
    emissivity_new=(0, 1),
    emissivity_old=(0, 1),
)
def adjust_radiation_temperature_to_other_emissivity(
    temperature, emissivity_old=1, emissivity_new=1, temperature_ambient=0
):
    r"""
    Given a radiation temperature :math:`T` (``temperature``) that
    was obtained using an emissivity of :math:`\epsilon_\mathrm{old}`
    (``emissivity_old``), calculate an adjusted radiation temperature
    :math:`T_\mathrm{new}` that would have been obtained if the emissivity had
    been :math:`\epsilon_\mathrm{new}` (``emissivity_new``), optionally taking
    the reflected ambient radiation temperature :math:`T_\mathrm{ambient}`
    (``T_ambient``) into account:

    .. math::

        T_\mathrm{new} = \sqrt[4]{
            \frac{
                \epsilon_\mathrm{old} \, T ^ 4 -
                \left(1-\epsilon_\mathrm{new}\right) \, T_\mathrm{ambient} ^ 4
                }{
                \epsilon_\mathrm{new}
                }
            }

    Args:
        temperature (numeric): the obtained radiation temperature
        emissivity_new (numeric, optional): the desired new
            emissivity. Defaults to ``1``.
        emissivity_old (numeric, optional): the emissivity used
            to obtain ``temperature``. Defaults to ``1``.
        temperature_ambient (numeric, optional): the ambient radiation
            temperature.  Defaults to ``0``, meaning no influence.
    """
    return (
        (
            (emissivity_old * temperature**4)
            - (1 - emissivity_new) * temperature_ambient**4
        )
        / emissivity_new
    ) ** (1 / 4)
