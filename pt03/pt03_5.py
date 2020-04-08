def my_func():
    my_sum = 0
    try:
        while True:
            my_list = input('Введите числа через пробел: ').split()
            for item in my_list:
                my_sum += int(item)
            print(my_sum)
    except ValueError:
        print('Итоговая сумма введенных чисел: ', my_sum)
    return my_sum

my_func()