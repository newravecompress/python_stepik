# функции


def min2(a, b):
    if a <= b:
        return a
    else:
        return b

# функция тоже является объектом
type(min2)      # class 'function'
id(min2)
# если return не объявлен, или он пустой, то вернется None
x = print(4)
print(x)    # None
# None в памяти всегда один, однозначно проверить можно с помощью is
x is None   # True


# функция должна быть объявлена до первого вызова
# могут быть без параметров, с произвольным числом параметров, с параметрами по умолчаниюю
# пример произвольного числа аргументов

def min(*a):
    m = a[0]
    for x in a:
        if x < m:
            m = x
    return m

min(5)
min(5, 3)
min(5, 3, 6, 10)
min([5, 3, 6, 10])


# значение параметров по умолчанию
def my_range(start, stop, step=1):
    res = []
    x = start
    if step > 0:
        while x < stop:
            res.append(x)
            x += step
    elif step < 0:
        while x > stop:
            res.append(x)
            x += step
    return res

print(my_range(2, 5))       # [2, 3, 4]
print(my_range(2, 15, 3))   # [2, 5, 8, 11, 14]
print(my_range(15, 2, -3))  # [15, 12, 9, 6, 3]


# именование переменных
print(my_range(stop=20, start=5))   # таким образом можно вызывать функцию с параметрами в произвольном порядке

# если вызываем функцию с хотя бы одной именованной переменной, то все остальные нужно именовать
# (именованные переменные только после позиционных)
my_range(start=2, 5, 1)     # работать не будет
my_range(2, 5, step=2)      # а так - будет


# локальные и глобальные переменные
def append_zero(xs):
    xs.append(0)

a = []
append_zero(a)      # теперь там будет ноль, потому что списки передаются по значениию

def append_zero(xs):
    xs.append(0)
    xs = [100]

a = []
append_zero(a)      # по-прежнему ноль
# происходит следующее: переменная а связывается со списком в памяти, в функции с этим списком связывается
# переменная xs и с помощью нее функция добавляет ноль в список
# но позже переменная xs привязывается к другому списку, но переменная а по-прежнему связана с первым

def print_value():
    print(a)
    a = 10
    print(a)

a = 5
print_value()       # возникнет ошибка, переменная вызывается до объявления
# переменная не будет искаться среди глобальных
# общее правило - если переменная изменяется внутри функции, то она является локальной
# переменная либо локальная, либо глобальная

def printab(a, b):
    print(a)
    print(b)

lst = [1, 2]
printab(*lst)       # printab(lst[0], lst[1])

args = {'a':10, 'b':20}
printab(**args)     # printab(key1 = args[key1], key2 = args[key2])

# Passing an unspecified number of arguments
def printab(a, b, *args):
    print('Positional argument a', a)
    print('Positional argument b', b)
    print('Additional arguments:')
    for arg in args:
        print(arg)

printab(1, 2, 3, 4, 5)      # порядок передачи переменных сохранился

def printab(a, b, **kwargs):
    print('Positional argument a', a)
    print('Positional argument b', b)
    print('Additional arguments:')
    for key in kwargs:
        print(key, kwargs[key])

printab(1, 2, c = 3, d = 4, jimmi = 5)
printab(1, c = 3, d = 4, jimmi = 5, b = 20)     # nothing will change

# common
# def function_name([positional_args,
#                  [positional_args_with_default,
#                  [*pos_args_name,
#                  [keyword_only_args,
#                  [**kw_args_name]]]]]):
# example:
def printab(a, b=10, *args, c=10, d, **kwargs):
    print(a, b, c, d)

printab(15, d=15)

# recursion
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

y = fib(5)
print(y)


