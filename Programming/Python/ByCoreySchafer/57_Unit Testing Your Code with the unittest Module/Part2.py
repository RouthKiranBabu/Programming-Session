import unittest 
import test_calc

class testcalculation(unittest.TestCase):
    def test_add(self):
        result = test_calc.add(10, 5)
        self.assertEqual(result, 15)
if __name__ == "__main__":
    unittest.main()
#In Command Prompt or terminal type: python Part2.py
#Output
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.000s
#
#OK