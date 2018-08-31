import unittest
from consecutive import consecutive_sub_array


class ConsecutiveSubArrayTestCase(unittest.TestCase):
    def test_regular_input(self):
        self.assertEqual(
            consecutive_sub_array([2, 0, 2, 1, 4, 3, 1, 0]),
            [0, 2, 1, 4, 3]
        )


if __name__ == "__main__":
    unittest.main()
