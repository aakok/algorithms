import unittest
from majority import majority


class MajorityTestCase(unittest.TestCase):
    def test_regular_input(self):
        self.assertEqual(
            majority([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]), 2
        )

    def test_none_majority_input(self):
        self.assertEqual(
            majority([2, 8, 7, 2, 4, 5, 2, 3, 1, 2, 2]), None
        )

    def test_none_majority_input2(self):
        self.assertEqual(
            majority([2, 8, 7, 9, 4, 5, 2, 3, 1, 2, 2]), None
        )

    def test_all_same_input(self):
        self.assertEqual(
            majority([0, 0, 0, 0, 0, 0]), 0
        )

    def test_all_different_input(self):
        self.assertEqual(
            majority([0, 1, 2, 3, 4, 5]), None
        )

    def test_divide_in_two_half_input(self):
        self.assertEqual(
            majority([1, 1, 1, 3, 3, 3]), None
        )


if __name__ == "__main__":
    unittest.main()
