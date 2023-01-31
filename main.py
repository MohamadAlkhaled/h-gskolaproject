import os
import math

def func1(a,b) -> str:
    return math.floor(a + b)

def func2(s) -> str:
    s= s.capitalize()
    if s.endswith('.'):
        return s
    else:
        return s + '.'