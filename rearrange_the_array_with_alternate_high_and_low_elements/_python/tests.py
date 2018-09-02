import unittest
from rearrange import rearrange


class RearrangeTestCase(unittest.TestCase):
    def test_regular_input1(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        result = [1, 3, 2, 5, 4, 7, 6]
        rearrange(array)
        self.assertEqual(
            array, result
        )

    def test_regular_input2(self):
        array = [9, 6, 8, 3, 7]
        result = [6, 9, 3, 8, 7]
        rearrange(array)
        self.assertEqual(
            array, result
        )

    def test_regular_input3(self):
        array = [6, 9, 2, 5, 1, 4]
        result = [6, 9, 2, 5, 1, 4]
        rearrange(array)
        self.assertEqual(
            array, result
        )

    def test_reverse_input(self):
        array = [7, 6, 5, 4, 3, 2, 1]
        result = [6, 7, 4, 5, 2, 3, 1]
        rearrange(array)
        self.assertEqual(
            array, result
        )

    def test_complex_input(self):
        array = [21, 24, 124, 12, 412, 425, 43, 64, 56, 58, 67, 453, 32, 523, 454, 6, 175, 5643, 5, 452, 3473, 4, 356, 3]
        rearrange(array)
        for i in range(1, array.__len__(), +2):
            self.assertGreater(
                array[i], array[i-1]
            )
            if i+1 < array.__len__():
                self.assertGreater(
                    array[i], array[i+1]
                )

    def test_complex_input2(self):
        array = [21, 24, 124, 12, 412, 425, 43, 64, 56, 58, 67, 453, 32, 523, 454, 6, 175, 5643, 5, 452, 3473, 4, 356]
        rearrange(array)
        for i in range(1, array.__len__(), +2):
            self.assertGreater(
                array[i], array[i-1]
            )
            if i+1 < array.__len__():
                self.assertGreater(
                    array[i], array[i+1]
                )


if __name__ == "__main__":
    unittest.main()
