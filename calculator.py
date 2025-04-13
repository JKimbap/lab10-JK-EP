"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    if a < 0:
        raise ValueError("Can not find square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a, b):
    a + b

def subtract(a, b):
    a - b

def multiply(a, b):
    a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Can not divide by a zero.")
    return b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Logarithm is undefined for these values.")
    return math.log(b,a)# use math library/raise ValueError

def exponent(a, b):
    a**b
