import unittest
from equilibrium import equilibrium


class EquilibriumTestCase(unittest.TestCase):
    def test_regular_input(self):
        self.assertEqual(
            equilibrium([0, -3, 5, -4, -2, 3, 1, 0]), [0, 3, 7]
        )

    def test_empty_input(self):
        self.assertEqual(
            equilibrium([]), []
        )

    def test_full_zero_input(self):
        self.assertEqual(
            equilibrium([0, 0, 0, 0]), [0, 1, 2, 3]
        )

    def test_no_balance_input(self):
        self.assertEqual(
            equilibrium([0, 1, -2, 3]), []
        )

    def test_no_balance_input2(self):
        self.assertEqual(
            equilibrium([0, 1, 2, 3]), []
        )

    def test_no_balance_input3(self):
        self.assertEqual(
            equilibrium([0, 1, 2, 3, 4]), []
        )


if __name__ == "__main__":
    unittest.main()
