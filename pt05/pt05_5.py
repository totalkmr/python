with open('pt05_5.txt', 'w+', encoding='utf8') as f:
    f.write(input('Введите через пробел числа для записи в файл: '))
    f.seek(0)
    print(f'Сумма чисел в файле равна {sum(map(int, f.readline().split()))}.')