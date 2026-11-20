class Calculator:
    '''Калькулятор с четырьмя базовыми операциями'''
    def calculate(self, a, b, c):
        '''Вернуть результат действия с двумя числами'''
        if c == '+':
            return a+b
        elif c == '-':
            return a-b
        elif c == '*':
            return a*b
        else:
            return a/b
