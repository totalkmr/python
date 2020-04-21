class Cell:
    def __init__(self, num_cell):
        self.num_cell = num_cell

    def __add__(self, other):
        return Cell(self.num_cell + other.num_cell)

    def __sub__(self, other):
        return Cell(self.num_cell - other.num_cell) if (self.num_cell - other.num_cell) > 0 else print('Беда-беда..')

    def __mul__(self, other):
        return Cell(self.num_cell * other.num_cell)

    def __truediv__(self, other):
        return Cell(round(self.num_cell / other.num_cell))

    def make_order(self, len_row):
        rows = ''
        for el in range(self.num_cell // len_row):
            rows += f'{"*" * len_row} \n'
        rows += f'{"*" * (self.num_cell % len_row)} \n'
        return rows


cell_1 = Cell(80)
cell_2 = Cell(30)
cell_3 = Cell(10)

print((cell_1 * cell_2).num_cell)
print((cell_1 / cell_2).num_cell)
print((cell_1 - cell_2).num_cell)
print((cell_1 / cell_2 + cell_3).num_cell)
print(cell_1.make_order(15))
print(cell_2.make_order(9))