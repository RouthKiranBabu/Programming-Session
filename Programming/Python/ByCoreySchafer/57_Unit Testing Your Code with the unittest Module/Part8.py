import unittest 
import test_calc_new

class testcalculation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(test_calc_new.add(10, 5), 15)
        self.assertEqual(test_calc_new.add(-1, 1), 0)
        self.assertEqual(test_calc_new.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(test_calc_new.subtract(10, 5), 5)
        self.assertEqual(test_calc_new.subtract(-1, 1), -2)
        self.assertEqual(test_calc_new.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(test_calc_new.multiply(10, 5), 50)
        self.assertEqual(test_calc_new.multiply(-1, 1), -1)
        self.assertEqual(test_calc_new.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(test_calc_new.divide(10, 5), 2)
        self.assertEqual(test_calc_new.divide(-1, 1), -1)
        self.assertEqual(test_calc_new.divide(-1, -1), 1)
        self.assertEqual(test_calc_new.divide(5, 2), 2.5)

if __name__ == "__main__":
    unittest.main()
#Output
#.F..
#======================================================================
#FAIL: test_divide (__main__.testcalculation.test_divide)
#----------------------------------------------------------------------
#Traceback (most recent call last):
#  File "c:\Users\kiran\OneDrive\Desktop\ScriptLearn\Learn Python\57_Unit Testing Your Code with the unittest Module\Part8.py", line 24, in test_divide
#    self.assertEqual(test_calc_new.divide(5, 2), 2.5)
#AssertionError: 2 != 2.5
#
#----------------------------------------------------------------------
#Ran 4 tests in 0.000s
#
#FAILED (failures=1)