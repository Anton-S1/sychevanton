N = int(input())
from module_2 import get_prime_factors
def is_prime(N):  # Проверим через деление до корня n
    if N < 2:
        return False
    for i in range(2, int(N ** 0.5 + 1)):
        if N % i == 0:
            return False
    else:
        return True

if is_prime(N) == False:
    print(get_prime_factors(N))
else:
    print("Не разложимо")