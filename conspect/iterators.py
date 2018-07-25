lst = [1, 2, 3, 4, 5]
book = {
    'title': 'The Langoliers',
    'author': 'Stephen King',
    'year_published': 1990
}
string = 'Hello world'

iterator = iter(book)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) // StopIteration

for i in book:
    print(i)

# Эквивалент цикла for .. in:
it = iter(book)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break


# Итераторы внутри собственных классов:
class RandomIterator:
    pass

x = RandomIterator()
print(next(x))      # TypeError 'RandomIterator' object is not an iterator
# Для того, чтобы стать итерируемым, объекту необходим метод __next__

from random import random

class RandomIterator:
    def __next__(self):
        return random()

x = RandomIterator()
# Каждый раз при запуске будем получать случайные значения из диапазона 0:1
print(next(x))      # next(x) -> x.__next__() x -- iterator
# Если запустим в цикле, то он будет бесконечным, потому что мы не определили StopIteration


class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0      # Число уже перечисленных элементов

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration()


x = RandomIterator(3)
# Каждый раз при запуске будем получать случайные значения из диапазона 0:1
print(next(x))      # next(x) -> x.__next__() x -- iterator
print(next(x))
print(next(x))
print(next(x))      # StopIteration

iter(x)     # TypeError: 'RandomIterator' object is not iterable
# Мы не сможем проитерироваться по объекту внутри for до тех пор, пока не будет объявлен метод __iter__


class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0      # Число уже перечисленных элементов

    # Этот метод должен возвращать экземпляр итератора
    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration()


for i in RandomIterator(10):
    print(i)

# Таким образом, для того, чтобы объект являлся итератором, у него должен быть объявлен метод __next__,
# а для того, чтобы по нему можно было проитерироваться, должен быть объявлен метод __iter__, который возвращает
# экземпляр итератора, то есть self


class DoubleElementListIterator:
    # объект-итератор
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration


class MyList(list):
    # Метод __iter__ уже определен в классе List
    def __iter__(self):
        return DoubleElementListIterator(self)

for pair in MyList([1, 2, 3, 4]):
    print(pair)

