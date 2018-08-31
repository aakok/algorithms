import unittest
from sum_zero import sum_zero_sub_arr


class SumZeroSubArrTestCase(unittest.TestCase):
    def test_regular_input(self):
        self.assertEqual(sum_zero_sub_arr([4, 2, -3, -1, 0, 4]), [(2, 6), (4, 5)])

    def test_regular_input2(self):
        self.assertEqual(
            sum_zero_sub_arr([3, 4, -7, 3, 1, 3, 1, -4, -2, -2]),
            [(0, 3), (0, 10), (1, 4), (2, 6), (3, 10), (5, 8)]
        )


if __name__ == "__main__":
    unittest.main()
