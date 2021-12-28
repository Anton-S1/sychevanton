import random
n = random.randint(-1, 1)
class Operation:
    def sum(self, x, y):
        print(abs(x + y))

    def neg(self, x, y):
        print(x - y * (-1)**n)

    def multiplication(self, x, y):
        print(x ** y)

    def division(self, x, y):
        if y == 0:
            return "Деление на нуль"
        print((x / y).imag)

    def degree(self, x, y):
        print(pow(x + y, 0 ))

x = complex(random.randint(-10, 10), random.randint(-10, 11))
y = complex(random.randint(-18, 14), random.randint(-15, 12))
obj1 = Operation()
obj1.sum(x, y)
obj1.neg(x, y)
obj1.multiplication(x, y)
obj1.division(x, y)
obj1.degree(x, y)