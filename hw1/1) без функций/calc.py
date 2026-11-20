a = int(input('Введите первое число: '))
d = str(input('Введите знак операции: '))
b = int(input('Введите второе число: '))

print('Ответ:', end=' ')
if d == '+':
    print(a + b)
elif d == '-':
    print(a - b)
elif d == '*':
    print(a * b)
elif d == '/':
    print(a / b)
else:
    print('Введены неверные значения!')
