class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self):
        super().__init__(title='Ручка')

    def draw(self):
        print(f'Использование инструмента {self.title}.')


class Pencil(Stationery):
    def __init__(self):
        super().__init__(title='Карандаш')

    def draw(self):
        print(f'Использование инструмента {self.title}.')


class Handle(Stationery):
    def __init__(self):
        super().__init__(title='Маркер')

    def draw(self):
        print(f'Использование инструмента {self.title}.')


my_stationery = Stationery('Канцелярская принадлежность')
my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()

my_stationery.draw()
my_pen.draw()
my_pencil.draw()
my_handle.draw()