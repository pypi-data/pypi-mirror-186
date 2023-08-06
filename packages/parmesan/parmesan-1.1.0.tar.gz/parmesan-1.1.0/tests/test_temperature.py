# system modules
import itertools
import unittest

# internal modules
from parmesan.units import units
from parmesan.gas import temperature

# external modules
import numpy as np


class TemperatureTest(unittest.TestCase):
    def test_virtual_temperature_same_without_humidity(self):
        for T in units.Quantity(np.arange(5, 30, 5), "celsius"):
            self.assertEqual(
                temperature.virtual_temperature(
                    temperature=T,
                    pressure=units("1000 hPa"),
                    relative_humidity=0,
                ),
                T,
            )
            self.assertEqual(
                temperature.virtual_temperature(
                    temperature=T,
                    mixing_ratio=0,
                ),
                T,
            )
            self.assertEqual(
                temperature.virtual_temperature(
                    temperature=T,
                    specific_humidity=0,
                ),
                T,
            )
            self.assertEqual(
                temperature.virtual_temperature(
                    temperature=T,
                    pressure=units("1000 hPa"),
                    water_vapour_pressure=units("0 hPa"),
                ),
                T,
            )

    def test_virtual_temperature_is_larger(self):
        for T, percentage in itertools.product(
            units.Quantity(np.arange(5, 30, 5), "celsius"),
            np.arange(10, 101, 10) * units.percent,
        ):
            with self.subTest(temperature=T, relative_humidity=percentage):
                self.assertGreater(
                    temperature.virtual_temperature(
                        temperature=T,
                        pressure=units("1023 hPa"),
                        relative_humidity=percentage,
                    ),
                    T,
                )
            with self.subTest(temperature=T, mixing_ratio=percentage):
                self.assertGreater(
                    temperature.virtual_temperature(
                        temperature=T, mixing_ratio=percentage
                    ),
                    T,
                )

    @staticmethod
    def Tv_from_mixing_ratio_rule_of_thumb_608(temperature, mixing_ratio):
        """
        https://en.wikipedia.org/w/index.php?title=Virtual_temperature&oldid=1099169099#Variations
        """
        return temperature.to("kelvin") * (1 + 0.608 * mixing_ratio)

    @staticmethod
    def Tv_from_mixing_ratio_rule_of_thumb_celsius(temperature, mixing_ratio):
        """
        https://en.wikipedia.org/w/index.php?title=Virtual_temperature&oldid=1099169099#Variations
        """
        return units.Quantity(
            temperature.to("celsius").m + mixing_ratio.to("g/kg").m / 6,
            "celsius",
        )

    def test_virtual_temperature_rule_of_thumb_608(self):
        for T, percentage in itertools.product(
            units.Quantity(np.arange(5, 30, 5), "celsius"),
            np.arange(0, 5, 1) * units.percent,
        ):
            with self.subTest(temperature=T, mixing_ratio=percentage):
                self.assertAlmostEqual(
                    temperature.virtual_temperature(
                        temperature=T, mixing_ratio=percentage
                    ).to("celsius"),
                    self.Tv_from_mixing_ratio_rule_of_thumb_608(
                        temperature=T, mixing_ratio=percentage
                    ).to("celsius"),
                    places=0,
                )

    def test_virtual_temperature_rule_of_thumb_celsius(self):
        for T, percentage in itertools.product(
            units.Quantity(np.arange(5, 30, 5), "celsius"),
            np.arange(0, 5, 1) * units.percent,
        ):
            with self.subTest(temperature=T, mixing_ratio=percentage):
                self.assertAlmostEqual(
                    temperature.virtual_temperature(
                        temperature=T, mixing_ratio=percentage
                    ).to("celsius"),
                    self.Tv_from_mixing_ratio_rule_of_thumb_celsius(
                        temperature=T, mixing_ratio=percentage
                    ).to("celsius"),
                    places=0,
                )
