a = int(input("Введите значение a:"))
b = int(input("Введите значение b:"))
while b!= 0:
    a,b = b, a % b
print('НОД:',a)