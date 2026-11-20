from classs import Calculator
calc = Calculator()

while True:
    try:
        a = int(input('Введите первое число: '))
    except ValueError:
        print('Нужно было ввести число!')
        break
    c = str(input('Введите знак операции: '))
    try:
        b = int(input('Введите второе число: '))
    except ValueError:
        print('Нужно было ввести число!')
        break
    if c == '/' and b == 0:
        print('На ноль делить нельзя!')
    elif c in ('+', '-', '*', '/'):
        print('Ответ:', calc.calculate(a, b, c))
    else:
        print('Введены неверные значения!')
    prod = str(input('Продолжить? '))
    if prod.strip().lower() == 'нет':
        break
