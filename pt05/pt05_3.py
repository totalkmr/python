with open('pt05_3.txt', 'r', encoding='utf8') as f:
    content = f.readlines()
    sum_profit = 0
    for line in content:
        el = line.strip().split()
        if int(el[1]) < 20000:
            print(f'У сотрудника с фамилией {el[0]} оклад менее 20000 рублей.')
        sum_profit += int(el[1])
    med_profit = sum_profit / len(content)

    print(f'Средний доход сотрудников составляет {med_profit} рублей.')