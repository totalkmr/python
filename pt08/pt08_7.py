class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return f'{self.re} + {self.im}i' if self.im >= 0 else f'{self.re} - {abs(self.im)}i'

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.im * other.re + self.re * other.im)


complex_1 = ComplexNumber(1, -2)
complex_2 = ComplexNumber(3, 4)

print(complex_1 + complex_2)
print(complex_1 * complex_2)