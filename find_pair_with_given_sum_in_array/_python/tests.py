import unittest
from pairs import find_pairs_hash


class CheckPairsTestCase(unittest.TestCase):
    def test_basic_input(self):
        self.assertEqual(find_pairs_hash([8, 7, 2, 5, 3, 1], 10), 2)


if __name__ == "__main__":
    unittest.main()
