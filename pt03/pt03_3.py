def my_func(num1, num2, num3):
    sum_max = num1 + num2 + num3 - min(num1, num2, num3)
    return sum_max

print(my_func(1, 2, 3))