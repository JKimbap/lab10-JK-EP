# https://github.com/JKimbap/lab10-JK-EP.git
# Partner 1: Jay Kim
# Partner 2: Erika Poirier

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(6, 3), 9)
        self.assertEqual(add(2,-6),-4)
        self.assertEqual(add(-3,0),-3)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(6,3),3)
        self.assertEqual(subtract(99,81),18)
        self.assertEqual(subtract(5,-7),12)
    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertAlmostEqual(mul(2,5),10)
        self.assertAlmostEqual(mul(-6,7), -42)
        self.assertAlmostEqual(mul(0.6,0.7),0.42)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(3,15),5)
        self.assertAlmostEqual(div(3,-15), -5)
        with self.assertRaises(ZeroDivisionError):
            div(0,15)

    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2,8),3)
        self.assertEqual(logarithm(2,32),5)
        self.assertEqual(logarithm(2,256),8)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(-2,5)
    ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5,0)
        with self.assertRaises(ValueError):
            logarithm(-5,10)
        with self.assertRaises(ValueError):
            logarithm(5,-10)
        with self.assertRaises(ValueError):
            logarithm(1,5)
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self):# 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4),5)
        self.assertAlmostEqual(hypotenuse(-3,-4),5)
        self.assertAlmostEqual(hypotenuse(5,12),13)

    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(square_root(0),0)
        self.assertAlmostEqual(square_root(25),5)
        with self.assertRaises(ValueError):
            square_root(-1)
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
