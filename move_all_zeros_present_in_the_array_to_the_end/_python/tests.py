import unittest
from move_zeros import move_zeros


class MoveZerosTestCase(unittest.TestCase):
    def test_regular_input(self):
        array = [6, 0, 8, 2, 3, 0, 4, 0, 1]
        move_zeros(array)
        self.assertEqual(
            array, [6, 8, 2, 3, 4, 1, 0, 0, 0]
        )

    def test_empty_input(self):
        array = []
        move_zeros(array)
        self.assertEqual(
            array, []
        )

    def test_all_zero_input(self):
        array = [0, 0, 0, 0]
        move_zeros(array)
        self.assertEqual(
            array, [0, 0, 0, 0]
        )

    def test_non_zero_input(self):
        array = [1, 2, 3, 4]
        move_zeros(array)
        self.assertEqual(
            array, [1, 2, 3, 4]
        )

    def test_zero_in_the_beginning_input(self):
        array = [0, 0, 1, 2, 3, 4]
        move_zeros(array)
        self.assertEqual(
            array, [1, 2, 3, 4, 0, 0]
        )


if __name__ == "__main__":
    unittest.main()
