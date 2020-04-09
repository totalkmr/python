from itertools import count, cycle

def infinite_iterator():
    start = int(input('Укажите начальное целое число: '))
    for num in count(start):
        print(num)
    return

def endless_cycle():
    my_list = input('Введите элементы списка через пробел: ').split()
    for el in cycle(my_list):
        print(el)
    return