class DateError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class Date:
    def __init__(self, my_date):
        self.my_date = my_date
        self.my_date_int = self.date_int(my_date)
        self.date_valid(list(self.my_date_int))

    @classmethod
    def date_int(cls, my_date):
        return [el for el in map(int, my_date.split('-'))]

    @staticmethod
    def date_valid(date_int):
        try:
            if not (0 < date_int[0] <= 31):  # очень приближенно
                raise DateError('День введен неверно!')
        except DateError:
            print('День введен неверно!')

        try:
            if not (0 < date_int[1] <= 12):
                raise DateError('Месяц введен неверно!')
        except DateError:
            print('Месяц введен неверно!')

        try:
            if not (0 < date_int[2] <= 2020):
                raise DateError('Год введен неверно!')
        except DateError:
            print('Год введен неверно!')


date = Date('34-15-1990')