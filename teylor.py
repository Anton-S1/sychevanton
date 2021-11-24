#  Программа считает значение е^x через ряд Тейлора
x = int(input("Введите значение x:"))
ITERATIONS = 30
def e(x):
    x_pow = 1
    multiplier = 1
    partial_sum = 1
    for n in range(1, ITERATIONS):
        x_pow *= x ** 1
        multiplier *= 1 / (1 * n)
        partial_sum += x_pow * multiplier
    return partial_sum

print(e(x))