print('y = a*x**2 + b*x +c')

a = float(input("Значение А = "))
b = float(input("Занчение B = "))
c = float(input("Значение С = "))

d = b ** 2 - 4 * a * c
print('Дискриминант =', d)
x1 = (-b + (d ** (0.5))) / (2 * a)
x2 = (-b - (d ** (0.5))) / (2 * a)
if d > 0:
    print('x1 =', x1, 'x2 =', x2)
elif d == 0:
    x = -b / (2 * a)
    print('x = ', x)
else:
    x1_2= -b / (2 * a)
    l = (abs(d) ** (0.5)) / (2 * a)
    print('Рівняння має комплексні корені, x1_2 =', x1_2, '+/-', l, "I")



try:
    a = input('Введиите число : ')
    print(list(reversed(a)))
except:
    print('Введено не число')



