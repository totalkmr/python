with open('pt05_2.txt', encoding='utf8') as f:
    content = f.readlines()
    count = len(content)

    print(f'Файл {f.name} содержит {count} строк.')

    i = 0
    for line in content:
        word = line.split()
        i += 1
        print(f'Количество слов в {i} строке равно {len(word)}')