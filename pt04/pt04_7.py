from itertools import count
from math import factorial

def fibo_gen():
    for num in count(1):
        yield factorial(num)
num_gen = 0
for el in fibo_gen():
    if num_gen < 15:
        print(el)
        num_gen += 1
    else:
        break