from functools import reduce

def list_mult(prev_el, el):
    return prev_el * el

print(reduce(list_mult, [el for el in range(100, 1001) if el % 2 == 0]))