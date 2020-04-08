# Version 1:
def my_func_1(x, y):
    return x ** y

# Version 2:
def my_func_2(x, y):
    i = 0
    res = 1
    while i < abs(y):
        res = res / x
        i += 1
    return res

print(my_func_1(3, -2))
print(my_func_2(3, -2))