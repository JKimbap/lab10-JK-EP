"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/JKimbap/lab10-JK-EP.git
# Partner 1: Jay Kim
# Partner 2: Erika Poirier

import math

def square_root(a):
    if a < 0:
        raise ValueError("Can not find square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a*b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Logarithm is undefined for these values.")
    return math.log(b,a)

def exp(a, b):
    return a**b
