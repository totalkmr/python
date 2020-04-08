revenue = int(input('Введите размер выручки: '))
costs = int(input('Введите размер издержек: '))

if revenue > costs:
    print('Ваша фирма работает с положительным финансовым результатом!')
    profit = revenue - costs
    rent = profit / revenue
    num_empl = int(input('Какова численность сотрудников Вашей фирмы: '))
    profit_empl = profit / num_empl
    print('Прибыль Вашей фирмы в расчете на одного сотрудника составляет:', profit_empl)
else:
    print('Ваша фирма работает в убыток...')