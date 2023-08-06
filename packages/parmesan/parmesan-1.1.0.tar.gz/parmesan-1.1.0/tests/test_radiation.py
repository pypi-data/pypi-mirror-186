# system modules
import unittest

# internal modules
from parmesan.units import units
from parmesan import radiation

# external modules
import numpy as np


class RadiationTest(unittest.TestCase):
    def test_blackbody_radiation(self):
        self.assertAlmostEqual(
            radiation.blackbody_radiation(temperature=1 * units.kelvin),
            radiation.constants.STEFAN_BOLTZMANN_CONSTANT
            * units("kelvin ^ 4"),
        )

    def test_emissivity_adjustment_no_change(self):
        self.assertAlmostEqual(
            radiation.adjust_radiation_temperature_to_other_emissivity(
                temperature=units.Quantity(30, "celsius"),
                emissivity_new=1,
                emissivity_old=1,
                temperature_ambient=0,
            ),
            units.Quantity(30, "celsius"),
        )
