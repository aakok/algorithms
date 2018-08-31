import unittest
from max_len_sum_sub_array import max_len_sum_sub_array


class MaxLenSumSubArrayTestCase(unittest.TestCase):
    def test_regular_input(self):
        self.assertEqual(
            max_len_sum_sub_array([5, 6, -5, 5, 3, 5, 3, -2, 0], 8),
            [-5, 5, 3, 5]
        )


if __name__ == "__main__":
    unittest.main()
