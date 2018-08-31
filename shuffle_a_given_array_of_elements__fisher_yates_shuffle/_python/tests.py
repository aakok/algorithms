import copy
import unittest
from shuffle import shuffle


class ShuffleTestCase(unittest.TestCase):
    def test_shuffle_length(self):
        array = [1, 2, 3, 4, 5, 6]
        array_cp = copy.copy(array)
        shuffle(array)
        self.assertEqual(array.__len__(), array_cp.__len__())

    def test_shuffle_content(self):
        array = [1, 2, 3, 4, 5, 6, 12, 23, 1412, 1, 32, 23, 5, 6, 6, 234, 23, 456, 678]
        array_cp = copy.copy(array)
        shuffle(array)
        for i in array_cp:
            self.assertIn(i, array)
        for j in array:
            self.assertIn(j, array_cp)


if __name__ == "__main__":
    unittest.main()
