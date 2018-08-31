import unittest
from longest_one_seq import longest_one_seq


class LongestOneSeqTestCase(unittest.TestCase):
    def test_regular_input(self):
        self.assertEqual(
            longest_one_seq([0, 0, 1, 0, 1, 1, 1, 0, 1, 1]), 7
        )

    def test_regular_input2(self):
        self.assertEqual(
            longest_one_seq([0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0]), 7
        )

    def test_filled_with_full_ones_input(self):
        self.assertEqual(
            longest_one_seq([1, 1, 1, 1]), -1
        )

    def test_filled_with_full_zeros_input(self):
        self.assertEqual(
            longest_one_seq([0, 0, 0, 0]), 0
        )

    def test_replace_first_input(self):
        self.assertEqual(
            longest_one_seq([0, 1, 1, 1]), 0
        )

    def test_replace_last_input(self):
        self.assertEqual(
            longest_one_seq([1, 1, 1, 0]), 3
        )


if __name__ == "__main__":
    unittest.main()
