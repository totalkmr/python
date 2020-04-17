class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}.')

    def get_total_income(self):
        print(f'Доход сотрудника с учетом премии: {sum(self._income.values())} руб.')


p_ivanov = Position('Петр', 'Иванов', 'Инженер', 100000, 50000)
p_ivanov.get_full_name()
p_ivanov.get_total_income()
print(f'Сотрудник {p_ivanov.name} {p_ivanov.surname} занимает должность {p_ivanov.position} c должностным окладом '
      f'в размере {p_ivanov._income.get("wage")} руб. и премией за основные результаты хозяйственной деятельности '
      f'в размере {p_ivanov._income.get("bonus")} руб.')