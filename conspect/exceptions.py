try:
    x = [1, 2, 'string', 7]
    x.sort()
    print(x)
except TypeError:
    print('TypeError :(')

print('I can catch!')


def f(x, y):
    try:
        return x/y
    except TypeError:
        print('TypeError')
    except ZeroDivisionError:
        print('ZeroDivisionError')

print(f(5, 0))

# Альтернативный вариант:
try:
    print(f(5, 0))
except ZeroDivisionError:
    print('ZeroDivisionError')

# Несколько исключений можно комбинировать в кортеже:
def f(x, y):
    try:
        return x/y
    except (TypeError, ZeroDivisionError):
        print('TypeError or ZeroDivisionError')

print(f(5, 0))

# Получение дополнительной информации об ошибке:
def f(x, y):
    try:
        return x/y
    except (TypeError, ZeroDivisionError) as E:
        print(type(E))
        print(E)
        print(E.args)

print(f(5, 0))
print(f(5, []))

# Можно не указывать конкретно тип ошибки:
def f(x, y):
    try:
        return x/y
    except Exception:   # для обработки любого исключения лучше указать Exception
        print('Error')

print(f(5, 0))
print(f(5, []))

# Можно посмотреть иерархию исключений:
print(ZeroDivisionError.mro())
# ZeroDivisionError, ArithmeticError, Exception, BaseException, Object

try:
    15/0
except ArithmeticError:     # isinstance(e, ArithmeticError) == True
    print('Arithmetic error :(')


# else, finally:
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Division by zero')
    else:
        print('result is', result)
    finally:
        print('Finally')

divide(2, 1)
divide(2, 0)
divide(2, [])

# Генерация исключений
# Создание своего класса исключения
class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return 'Hello, ' + name
    else:
        raise BadName(name + ' is inappropriate name')

print(greet('Anthony'))
print(greet('anton'))
# ValueError используется как правило когда значение не подходит по каким-то причинам

while True:
    try:
        name = input('Please enter your name')
        greeting = greet(name)
        print(greeting)
    except BadName:
        print('Please try again')
    else:
        break



