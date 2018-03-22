# У объектов есть 3 обязательх характеристики: идентификатор
x = [1, 2, 3]
print(id(x))
print(id([1, 2, 3]))    # у этих объектов будут разные ИД

# присваивание - это запоминание в имени переменной идентификатора объекта

# с помощью is можно проверить, ссылаются ли две переменные на один объект:
x = [1, 2, 3]
y = x
y is x          # True
y is [1, 2, 3]  # False

# Следующая характеристика объекта - его тип
x = [1, 2, 3]
type(x)     # output is "<class 'list'>"
type(4)     # output is "<class 'int'>"
type(type(x))   # output is "<class 'type'>"
# тип не может быть изменен после создания объекта (как и идентификатор)

# значение списка - упорядоченное множество ссылок на объекты
# в отличае от кортежа мы можем поменять последовательность ссылок
# всего 3 стандартных изменяемых типа - list, dict, set

# интерпретатор не всегда создает новый объект из примитива:
a = b = c = 1   # единица - это один и тот же объект

# но при работе с изменяемыми типами - всегда создается новый
x = []
y = []
x is y  # False


# Классы

class MyClass:
    a = 10

    def func(self):
        print('Hello')

print(MyClass.a)
print(MyClass.func)
# атрибут - это имя внутри пространства имен

x = MyClass()
print(type(x))  # class 'MyClass'
print(type(MyClass))    # class 'type'


class Counter:
    pass


x = Counter()   # x - экземпляр класса
x.count = 0     # создали новый атрибут внутри объекта экземпляра
x.count += 1    # переменная создалась внутри пространства имен объекта

print(x.count)


class Counter:
    def __init__(self):
        self.count = 0


x = Counter()
print(x.count)
x.count += 1


class Counter1:
    def __init__(self, start=0):
        self.count = start

x = Counter1(10)        # 10
y = Counter1()          # 0


class Counter2:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1

    def reset(self):
        self.count = 0


x = Counter2()
x.inc()
print(x.count)
Counter2.inc(x)     # эквивалентно вызову x.inc()
print(x.count)
x.reset()
print(x.count)


# Наследование
class MyList(list):
    def even_length(self):
        return len(self) % 2 == 0

x = MyList()
x.extend([1, 2, 3, 4, 5])
print(x.even_length())      # False
x.append(6)
print(x.even_length())      # True


# иерархия классов
class D: pass
class E: pass
class B(D, E): pass
class C: pass
class A(B, C): pass

issubclass(A, A)    # True
issubclass(C, D)    # False
issubclass(A, D)    # True
issubclass(C, object)   # True
issubclass(object, C)   # False

x = A()
isinstance(x, A)    # True
isinstance(x, B)    # True
isinstance(x, object)   # True
isinstance(x, str)  # False

print(A.mro())


# Примеси
class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0


class MyList(list, EvenLengthMixin):
    pass

class MyDict(dict, EvenLengthMixin):
    pass

print(MyList.mro())
x = MyList([1, 2, 3])
print(x.even_length())  # False
x.append(4)
print(x.even_length())  # True

y = MyDict()
y['key'] = 'value'
y['another_key'] = 'another_value'
print(y.even_length())  # True

class MyList(list, EvenLengthMixin):
    def pop(self):
        x = super(MyList, self).pop()
        # MyList - класс, родителей которого хотим проверить,
        # self - объект, которому будет принадлежать метод
        # эквивалентно list.pop(self)
        print('Last value is:', x)
        return x

ml = MyList([1, 3, 5, 6])
z = ml.pop()    # Last value is 6
print(z)    # 6
print(ml)   # [1, 3, 5]


