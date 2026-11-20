def f(a, b, c):
    '''Вернуть результат действия с двумя числами'''
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    else:
        return a/b
