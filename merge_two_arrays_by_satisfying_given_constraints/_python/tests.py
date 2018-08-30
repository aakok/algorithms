import unittest
from merge_arrays_under_condition import merge


class TestMergeUnderCondition(unittest.TestCase):
    def test_regular_input(self):
        arr1 = [0, 2, 0, 3, 0, 5, 6, 0, 0]
        arr2 = [1, 8, 9, 10, 15]
        merge(arr1, arr2)
        self.assertEqual(arr1, [1, 2, 3, 5, 6, 8, 9, 10, 15])

    def test_non_empty_start_input(self):
        arr1 = [2, 0, 0, 3, 0, 5, 6, 0, 0]
        arr2 = [1, 8, 9, 10, 15]
        merge(arr1, arr2)
        self.assertEqual(arr1, [1, 2, 3, 5, 6, 8, 9, 10, 15])

    def test_non_empty_last_input(self):
        arr1 = [2, 0, 0, 3, 0, 5, 6, 0, 9]
        arr2 = [1, 8, 10, 15]
        merge(arr1, arr2)
        self.assertEqual(arr1, [1, 2, 3, 5, 6, 8, 9, 10, 15])

    def test_fist_all_empty_input(self):
        arr1 = [0, 0, 0, 0, 2, 3, 5, 6, 9]
        arr2 = [1, 8, 10, 15]
        merge(arr1, arr2)
        self.assertEqual(arr1, [1, 2, 3, 5, 6, 8, 9, 10, 15])

    def test_last_all_empty_input(self):
        arr1 = [2, 3, 5, 6, 9, 0, 0, 0, 0]
        arr2 = [1, 8, 10, 15]
        merge(arr1, arr2)
        self.assertEqual(arr1, [1, 2, 3, 5, 6, 8, 9, 10, 15])

    def test_consecutive_input(self):
        arr1 = [1, 0, 3, 0, 5, 0, 7, 0, 9]
        arr2 = [2, 4, 6, 8]
        merge(arr1, arr2)
        self.assertEqual(arr1, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_consecutive_input_switched(self):
        arr1 = [0, 1, 0, 3, 0, 5, 0, 7, 0, 9]
        arr2 = [-1, 2, 4, 6, 8]
        merge(arr1, arr2)
        self.assertEqual(arr1, [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()
