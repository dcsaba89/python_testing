import numpy as np
import unittest

import new.x as x


class MyTestCase(unittest.TestCase):
    # @staticmethod
    def test_ranger(self):
        np.testing.assert_array_equal(x.ranger(100), np.arange(100))
        np.testing.assert_array_equal(x.ranger(50), np.arange(50))
        np.testing.assert_array_equal(x.ranger(10), np.arange(10))
        np.testing.assert_array_equal(x.ranger(1), np.arange(1))
        np.testing.assert_array_equal(x.ranger(0), np.arange(0))

        with self.assertRaises(ValueError):
            x.ranger("X")
