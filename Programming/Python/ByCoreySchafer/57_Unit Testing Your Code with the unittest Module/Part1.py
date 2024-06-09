import unittest 
import test_calc

#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

class testcalculation(unittest.TestCase):
    def test_add(self):
        result = test_calc.add(10, 5)
        self.assertEqual(result, 15)
#type at terminal: python -m unittest Part1.py
#Output
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.000s
#
#OK