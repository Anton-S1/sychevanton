import random
n = int(input("Введите число для проверки: "))
def ferma(n):
    if n > 2:
        for i in range(25):
            a = random.randint(2, n - 1)
            if pow(a, n-1, n) != 1:
                return False
    return True
print(ferma(n))
print("\n")

def is_prime(n):  # Проверим через деление до корня n
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    else:
        return True
print("Проверка через деление до корня:",is_prime(n))
