import unittest 
import test_calc_modify

class testcalculation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(test_calc_modify.add(10, 5), 15)
        self.assertEqual(test_calc_modify.add(-1, 1), 0)
        self.assertEqual(test_calc_modify.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(test_calc_modify.subtract(10, 5), 5)
        self.assertEqual(test_calc_modify.subtract(-1, 1), -2)
        self.assertEqual(test_calc_modify.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(test_calc_modify.multiply(10, 5), 50)
        self.assertEqual(test_calc_modify.multiply(-1, 1), -1)
        self.assertEqual(test_calc_modify.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(test_calc_modify.divide(10, 5), 2)
        self.assertEqual(test_calc_modify.divide(-1, 1), -1)
        self.assertEqual(test_calc_modify.divide(-1, -1), 1)

if __name__ == "__main__":
    unittest.main()
#Output
#..F.
#======================================================================
#FAIL: test_multiply (__main__.testcalculation.test_multiply)
#----------------------------------------------------------------------
#Traceback (most recent call last):
#  File "c:\Users\kiran\OneDrive\Desktop\ScriptLearn\Learn Python\57_Unit Testing Your Code with the unittest Module\Part6.py", line 16, in test_multiply
#    self.assertEqual(test_calc_modify.multiply(10, 5), 50)
#AssertionError: 100000 != 50
#
#----------------------------------------------------------------------
#Ran 4 tests in 0.001s
#
#FAILED (failures=1)