import unittest 
import test_calc

class testcalculation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(test_calc.add(10, 5), 15)
        self.assertEqual(test_calc.add(-1, 1), 0)
        self.assertEqual(test_calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(test_calc.subtract(10, 5), 5)
        self.assertEqual(test_calc.subtract(-1, 1), -2)
        self.assertEqual(test_calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(test_calc.multiply(10, 5), 50)
        self.assertEqual(test_calc.multiply(-1, 1), -1)
        self.assertEqual(test_calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(test_calc.divide(10, 5), 2)
        self.assertEqual(test_calc.divide(-1, 1), -1)
        self.assertEqual(test_calc.divide(-1, -1), 1)

if __name__ == "__main__":
    unittest.main()
#Output
#....
#----------------------------------------------------------------------
#Ran 4 tests in 0.000s
#
#OK