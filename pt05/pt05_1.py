with open('pt05_1.txt', 'w') as f:
    while True:
        line = input('Введите данные для записи в файл: ')
        f.writelines(line + '\n')
        if not line:
            break