x = input().split()
print(x)
n, k = map(int, x)      # map принимает два аргумента - функцию и последовательность
print(n + k)

# map - итератор
map_obj = map(int, input().split())
print(map_obj)      # <map object at 0x005249D0>
n = next(map_obj)
k = next(map_obj)

# Общее правило: если слева несколько переменных, а справа - последовательность, то интерпретатор попытается
# 'распаковать' значения в переменные. Если значений больше или меньше, чем переменных - будет ошибка
# ValueError: too many values to unpack

# То же самое можно сделать с помощью генератора
n, k = (int(i) for i in input().split())
print(n + k)

# Фильтр
xs = (int(i) for i in input().split())
print(xs)       # <generator object <genexpr> at 0x00729270>
def even(x):
    return x % 2 == 0

evens = filter(even, xs)
print(evens)    # <filter object at 0x006E49D0>
for i in evens:
    print(i)

# Можно сразу обернуть в list
evens = list(filter(even, xs))

# То же самое с помощью лямбд
evens = list(filter(lambda x: x % 2 == 0, xs))


x = [
    ('Guido', 'Van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]

def length(name):
    return len(' '.join(name))

name_lengths = [length(name) for name in x]
print(name_lengths)

x.sort(key=length)
print(x)

# То же самое с помощью лямбд
x.sort(key=lambda name: len(' '.join(name)))


# функции-операторы
import operator as op

print(op.add(4, 5))
print(op.mul(4, 5))
print(op.contains([1, 2, 3], 4))

# Получение элементов
x = [1, 2, 3]
f = op.itemgetter(1)    # f(x) == x[1]
print(f(x))     # 2

y = {'a': 1, 'b': 2, 'c': 3}
f = op.itemgetter('b')    # f(x) == x[1]
print(f(y))     # 2

# Получение атрибутов объектов
f = op.attrgetter('sort')   # Получить метод sort у объекта
print(f([]))

x = [
    ('Guido', 'Van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]
x.sort(key=lambda x: x[-1])
# эквивалентно
x.sort(key=op.itemgetter(-1))
print(x)

# Другие функции
from functools import partial

x = int('1101', base=2)
print(x)

int2 = partial(int, base=2)
x = int2('110101010')
print(x)

# универсальная функция сортировки по последнему элементу
sort_by_last = partial(list.sort, key=op.itemgetter(-1))
print(x)
sort_by_last(x)
print(x)
x = ['dafa', 'asdfagf', 'djfgdsijgh']
sort_by_last(x)     # отработает для любого списка
print(x)

