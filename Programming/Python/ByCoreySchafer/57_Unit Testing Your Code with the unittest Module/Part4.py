import unittest 
import test_calc

class testcalculation(unittest.TestCase):
    def test_add(self):
        result = test_calc.add(10, 5)
        #Output must be 15 just for test placed 14
        self.assertEqual(result, 14)
if __name__ == "__main__":
    unittest.main()
#In Command Prompt or terminal type: python Part2.py
#Output
#F
#======================================================================
#FAIL: test_add (__main__.testcalculation.test_add)
#----------------------------------------------------------------------
#Traceback (most recent call last):
#  File "C:\Users\kiran\OneDrive\Desktop\ScriptLearn\Learn Python\57_Unit Testing Your Code with the unittest Module\Part4.py", line 7, in test_add
#    self.assertEqual(result, 14)
#AssertionError: 15 != 14
#
#----------------------------------------------------------------------
#Ran 1 test in 0.000s
#
#FAILED (failures=1)