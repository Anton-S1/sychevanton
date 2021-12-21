import math
import random
n = int(input("Введите число для проверки: "))


def calculateJacobian(a, n):  # Вычисление значения символа Якоби 
    if (a == 0):
        return 0

    ans = 1

    if (a < 0):
        a = -a

        if (n % 4 == 3):
            ans = -ans

    if (a == 1):
        return ans

    while (a):

        if (a < 0):
            a = -a

            if (n % 4 == 3):
                ans = -ans

        while (a % 2 == 0):

            a = a // 2

            if (n % 8 == 3 or n % 8 == 5):
                ans = -ans

        a, n = n, a

        if (a % 4 == 3 and n % 4 == 3):
            ans = -ans

        a = a % n

        if (a > n // 2):
            a = a - n

    if (n == 1):
        return ans

    return 0
def modulo(base, exponent, mod):
    x = 1

    y = base

    while (exponent > 0):

        if (exponent % 2 == 1):
            x = (x * y) % mod

        y = (y * y) % mod

        exponent = exponent // 2

    return x % mod

def check(n):
    for i in range(1, 100):
        if n % 2 == 0:
           return False
        a = random.randint(2, n - 1)
        f = math.gcd(n, a)
        if f > 1:
            return False
        calculateJacobian(a, n)

        jacobian = (n + calculateJacobian(a, n)) % n

        mod = modulo(a, (n - 1) / 2, n)

        if (jacobian == 0 or mod != jacobian):
            return False
        else:
            return True
print(check(n))
