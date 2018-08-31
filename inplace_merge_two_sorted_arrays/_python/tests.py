import unittest
from inplace_merge import inplace_merge


class InplaceMergeTestCase(unittest.TestCase):
    def test_regular_input(self):
        self.assertEqual(inplace_merge([1, 4, 7, 8, 10], [2, 3, 9]), ([1, 2, 3, 4, 7], [8, 9, 10]))

    def test_regular_input2(self):
        self.assertEqual(
            inplace_merge(
                [1, 1, 2, 2, 3, 3, 4, 4, 6, 12, 12, 323],
                [1, 3, 4, 4, 6, 7, 12, 15, 23, 23, 25, 34, 34, 42, 42, 42, 45, 45, 54, 56, 86, 132, 234, 234, 234, 412,
                 422, 523, 4122, 4213]
            ),
            (
                [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4],
                [6, 6, 7, 12, 12, 12, 15, 23, 23, 25, 34, 34, 42, 42, 42, 45, 45, 54, 56, 86, 132, 234, 234, 234, 323, 412,
                 422, 523, 4122, 4213]
            )
        )

    def test_negative_number_input(self):
        self.assertEqual(
            inplace_merge([-10, -3, 0], [-9, -1, 4, 5]),
            ([-10, -9, -3], [-1, 0, 4, 5])
        )


if "__main__" == __name__:
    unittest.main()
