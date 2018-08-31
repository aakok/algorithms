import unittest
from max_product_two_ints import max_product


class MaxProductTestCase(unittest.TestCase):
    def test_regular_input(self):
        self.assertEqual(
            max_product([-10, -3, 5, 6, -2]), [[-10, -3], [5, 6]]
        )

    def test_regular_input2(self):
        self.assertEqual(
            max_product([-10, -3, 5, 6, -2, -5]), [[-10, -5]]
        )


if __name__ == "__main__":
    unittest.main()
