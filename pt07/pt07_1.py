class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        return f'\n'.join(f'\t'.join(str(el) for el in row) for row in self.matr) + f'\n'

    def __add__(self, other):
        sum_matrix = [[self.matr[row][column] + other.matr[row][column] for column in range(len(self.matr[0]))]
                      for row in range(len(self.matr))]
        return Matrix(sum_matrix)


matrix_1 = Matrix([[1, 2, 3, 4],
                   [4, 5, 6, 7],
                   [8, 9, 10, 11],
                   [12, 13, 14, 15]])

matrix_2 = Matrix([[16, 17, 18, 19],
                   [20, 21, 22, 23],
                   [24, 25, 26, 27],
                   [28, 29, 30, 31]])

matrix_3 = Matrix([[32, 33, 34, 35],
                   [36, 37, 38, 39],
                   [40, 41, 42, 43],
                   [44, 45, 46, 47]])

print(matrix_1)
print(matrix_2)
print(matrix_3)
print(matrix_1 + matrix_2 + matrix_3)