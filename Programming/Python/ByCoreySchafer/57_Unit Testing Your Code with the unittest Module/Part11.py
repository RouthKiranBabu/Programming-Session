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
        self.assertEqual(test_calc.divide(5, 2), 2.5)

        #So it does not raises the value error
        self.assertRaises(ValueError, test_calc.divide, 10, 2)

if __name__ == "__main__":
    unittest.main()
#Output
#.F..
#======================================================================
#FAIL: test_divide (__main__.testcalculation.test_divide)
#----------------------------------------------------------------------
#Traceback (most recent call last):
#  File "c:\Users\kiran\OneDrive\Desktop\ScriptLearn\Learn Python\57_Unit Testing Your Code with the unittest Module\Part11.py", line 26, in test_divide
#    self.assertRaises(ValueError, test_calc.divide, 10, 2)
#AssertionError: ValueError not raised by divide
#
#----------------------------------------------------------------------
#Ran 4 tests in 0.000s
#
#FAILED (failures=1)