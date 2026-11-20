from func import *

a = int(input('Введите первое число: '))
c = str(input('Введите знак операции: '))
b = int(input('Введите второе число: '))
print('Ответ:', end = ' ')
if c== '+':
    print(summa(a,b))
elif c= '-':
    print(raznost(a,b))
elif c== '*':
    print(proizvedenie(a,b))
elif c == '/':
    print(delenie(a,b))
else:
    print('Введены неверные значения!')
