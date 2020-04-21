from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @abstractmethod
    def cloth_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)

    def cloth_consumption(self):
        return self.size / 6.5 + 0.5

    @property
    def coat_size(self):
        return f'Размер пальто, для расчета расхода ткани: ' \
               f'{self.size}'


class Jacket(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)

    def cloth_consumption(self):
        return 2 * self.height + 0.3

    @property
    def jacket_height(self):
        return f'Ростовка костюма, для расчета расхода ткани: ' \
               f'{self.height}'


coat = Coat(52, 1.84)
jacket = Jacket(52, 1.84)

print(coat.cloth_consumption())
print(jacket.cloth_consumption())
print(coat.coat_size)
print(jacket.jacket_height)