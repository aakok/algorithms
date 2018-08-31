import unittest
from duplicate import duplicate


class DuplicateTestCase(unittest.TestCase):
    def test_regular_input(self):
        self.assertEqual(
            duplicate([1, 2, 3, 4, 4]), 4
        )

    def test_regular_input2(self):
        self.assertEqual(
            duplicate([1, 2, 3, 4, 2]), 2
        )


if __name__ == "__main__":
    unittest.main()
