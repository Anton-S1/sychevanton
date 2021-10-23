import math
eps = float(input('Введите точность:'))
x = float(input('Введите x:'))
n = 0
an = x
summ = 0
while math.fabs(an) > eps :
   summ += an
   an*= -x * x / ((2. * n + 1.) * (2. * n + 2.))
   n += 1
print('Сумма равна:',summ,)
