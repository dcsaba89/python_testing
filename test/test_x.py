import numpy as np
import unittest

import New.x as x


class TestNew(unittest.TestCase):
    # @staticmethod
    def test_ranger(self):
        np.testing.assert_array_equal(x.ranger(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        np.testing.assert_array_equal(x.ranger(1), [0])
        np.testing.assert_array_equal(x.ranger(0), [])

        np.testing.assert_array_equal(x.ranger('10'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        np.testing.assert_array_equal(x.ranger('1'), [0])
        np.testing.assert_array_equal(x.ranger('0'), [])

        with self.assertRaises(ValueError):
            x.ranger("X")

        with self.assertRaises(ValueError):
            x.ranger(-8)

        with self.assertRaises(ValueError):
            x.ranger(0.5)

