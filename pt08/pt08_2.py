class MyZeroDivisionError(Exception):

    def check_zero(self, divident=0, division=0):
        try:
            divident = int(input('Введите делимое: '))
            division = int(input('Введите делитель: '))
            return print(f'Результат деления {divident} на {division} равен {divident / division}')

        except ZeroDivisionError:
            print('Деление на ноль!')

        except ValueError:
            print('Введено не число!')

a = MyZeroDivisionError()
a.check_zero()