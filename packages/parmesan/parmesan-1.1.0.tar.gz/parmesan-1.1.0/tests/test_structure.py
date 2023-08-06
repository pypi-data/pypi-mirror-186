# system modules
import unittest

# internal modules
from parmesan.analysis import structure_function, structure

# external modules
import numpy as np
import pandas as pd


class structure_test(unittest.TestCase):
    def test_structure_ndarray(self):

        ns = 7000
        # Test array
        t_arr = pd.date_range(
            start="2021-04-29 10:00:00", periods=ns, end="2021-04-29 10:00:40"
        )  # array
        t1 = np.array(t_arr)  # array
        epoch = t1.astype(np.int64) / 10**9  # epoch time in seconds
        wave = np.sin(2 * np.pi * (epoch - epoch[0]))  # array

        # The structure function of a sine wave with 2*pi*t anglular frequency
        # is totally anti correlated value 2 every 0.5 + integer sec

        sh_arr, D_arr = structure(wave, t_arr)
        self.assertAlmostEqual(max(D_arr), 2.000, places=3)
        self.assertAlmostEqual(sh_arr[np.argmax(D_arr)], 0.50, places=2)

    def test_structure_dataframe(self):

        ns = 7000
        # Test array
        t_arr = pd.date_range(
            start="2021-04-29 10:00:00", periods=ns, end="2021-04-29 10:00:40"
        )  # array
        t1 = np.array(t_arr)  # array
        epoch = t1.astype(np.int64) / 10**9  # epoch time in seconds
        wave = np.sin(2 * np.pi * (epoch - epoch[0]))  # array
        w_df = pd.DataFrame(np.transpose(wave), columns=["wave"], index=t_arr)

        # The structure function of a sine wave with 2*pi*t anglular frequency
        # is totally anti correlated value 2 every 0.5 + integer sec

        D_df = structure(w_df)
        self.assertAlmostEqual(D_df["wave"].max(), 2.000, places=3)
        self.assertAlmostEqual(
            D_df.index[D_df["wave"].argmax()], 0.50, places=2
        )

    def test_structure_serie(self):

        ns = 7000
        # Test array
        t_arr = pd.date_range(
            start="2021-04-29 10:00:00", periods=ns, end="2021-04-29 10:00:40"
        )  # array
        t1 = np.array(t_arr)  # array
        epoch = t1.astype(np.int64) / 10**9  # epoch time in seconds
        wave = np.sin(2 * np.pi * (epoch - epoch[0]))  # array
        w_df = pd.DataFrame(np.transpose(wave), columns=["wave"], index=t_arr)
        w_s = w_df.squeeze()

        # The structure function of a sine wave with 2*pi*t anglular frequency
        # is totally anti correlated value 2 every 0.5 + integer sec

        D_s = structure(w_s)
        self.assertAlmostEqual(D_s.max(), 2.000, places=3)
        self.assertAlmostEqual(D_s.index[D_s.argmax()], 0.50, places=2)
