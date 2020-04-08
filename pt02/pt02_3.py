month = int(input('Введите номер месяца (1-12): '))

# list version
if month < 1 or month > 12:
    print('Введено некорректное значение!')
else:
    seasons_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень',
                    'Зима']
    print('[list version] Время года:', seasons_list[month - 1])

# dict version
seasons_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень',
                10: 'Осень', 11: 'Осень', 12: 'Зима'}
print('[dict version] Время года:', seasons_dict.get(month))