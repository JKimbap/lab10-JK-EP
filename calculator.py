"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a*b

def multiply(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Logarithm is undefined for these values.")
    return math.log(b, a)

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Logarithm is undefined for these values.")
    return math.log(b,a)

def exp(a, b):
    return a**b

def exponent(a, b):
    return a**b
