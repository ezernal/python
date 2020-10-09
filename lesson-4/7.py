from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)
ten = fact()
for i in ten:
    print(i)