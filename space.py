import random
class Cplx:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __str__(self):
        return "({}, {})".format(self.r, self.i)

    def __add__(self, other):
        return Cplx(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return Cplx((self.r * other.r - self.i * other.i),  (self.r * self.i + other.r * other.i))

    def __sub__(self, other):
        return Cplx(self.r - other.r, self.i - other.i)

    def __truediv__(self, other):
        if  other.r ** 2 + other.i ** 2 != 0:
            return Cplx((self.r * other.r + self.i * other.i)/(other.r ** 2 + other.i ** 2), (other.r * self.i - self.r * other.i)/(other.r ** 2 + other.i ** 2))

        else: return 'Делить на нуль нельзя'

a = Cplx(random.randint(-1000,1000),random.randint(-1000,1000))
b = Cplx(random.randint(-1000,1000), random.randint(-1000,1000))

e_add = Cplx(0, 0)                     # Нейтральное по сложению
e_sub = Cplx(1, 0)                     # Нейтральное по умножению
print("Сложение:",a + b)
print("Разность:",a - b)
print("Умножение:",a * b)
print("Деление:",a / b)
