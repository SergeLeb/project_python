class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'сумма z1 и z2 равна ')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * self.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'

z1 = ComplexNumber(1, -2)
z2 = ComplexNumber(3, 4)
print(z1)
print(z1 + z2)
print(z1 * z2)

