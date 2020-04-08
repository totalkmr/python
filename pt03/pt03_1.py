def func_division():
    num1 = int(input('Введите 1 число: '))
    num2 = int(input('Введите 2 число: '))
    while num2 == 0:
        num2 = int(input('Деление на 0! Введите 2 число: '))
    return num1 / num2

print('Результат деления двух чисел:', func_division())