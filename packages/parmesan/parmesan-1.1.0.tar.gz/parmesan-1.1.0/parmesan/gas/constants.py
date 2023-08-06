# system modules

# internal modules
from parmesan.units import units

# external modules

__doc__ = """

.. note::

    The gas constants in this module were taken from `this Wikipedia page
    <https://de.wikipedia.org/wiki/Gaskonstante>`_, last access 14.12.2020.

"""

AVOGADRO_CONSTANT = 6.02214076e23 / units.mol
"""
Avogadro constant

Taken from https://physics.nist.gov/cgi-bin/cuu/Value?na (15.12.2020).
"""

BOLTZMANN_CONSTANT = 1.380649e-23 * units.joule / units.kelvin
"""
Boltzmann Constant

Taken from https://physics.nist.gov/cgi-bin/cuu/Value?k (15.12.2020).
"""

# Gas constants
GAS_CONSTANT_UNIVERSAL = AVOGADRO_CONSTANT * BOLTZMANN_CONSTANT
"""
universal gas constant
"""

MOLAR_MASS_WATER_VAPOUR = (18.02 * units.gram).to("kg") / units.mol
"""
molar mass of water vapour
"""


GAS_CONSTANT_WATER_VAPOUR = GAS_CONSTANT_UNIVERSAL / MOLAR_MASS_WATER_VAPOUR
"""
specific gas constant of water vapour
"""

MOLAR_MASS_DRY_AIR = (28.96 * units.gram).to("kg") / units.mol
"""
molar mass of dry air
"""

GAS_CONSTANT_DRY_AIR = GAS_CONSTANT_UNIVERSAL / MOLAR_MASS_DRY_AIR
"""
specific gas constant of dry air
"""

MOLAR_MASS_CO2 = (44.01 * units.gram).to("kg") / units.mol
"""
molar mass of carbon dioxide
"""

GAS_CONSTANT_CO2 = GAS_CONSTANT_UNIVERSAL / MOLAR_MASS_CO2
"""
specific gas constant of carbon dioxide
"""

SPECIFIC_ISOBARIC_HEAT_CAPACITY_DRY_AIR = (
    (1005 * units.joule).to("joule") / units.kg / units.kelvin
)
"""
specific isobaric heat capacity of dry air

Taken from https://de.wikipedia.org/wiki/Spezifische_W%C3%A4rmekapazit%C3%A4t
(16.12.2020).
"""

EARTH_ACCELERATION = 9.81 * units.meter / units.second**2
"""
earth acceleration

Taken from https://de.wikipedia.org/wiki/Schwerefeld#Erdbeschleunigung
(17.12.2020).
"""
