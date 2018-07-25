from random import random


class RandomIterator:
    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration


# Функция-генератор
def random_generator(k):
    # Интерпретатор смотрит все тело функции целиком, и если видит yield - значит это генератор,
    # и значит работает по-другому
    for i in range(k):
        yield random()

gen = random_generator(3)
# gen - объект генератора, он знает целиком все тело функции, и исполнение тела функции начнется лишь тогда,
# когда мы попросим следующий элемент. В этот момент он начнет исполнять тело функции до первого ключевого
# слова yield. После этого он вернет значение наружу, туда, где мы вызвали функцию next()
# В момент yield'а запоминается состояние функции, чтобы в следующий раз начать с этого момента
# в момент, когда мы не найдем yield, генератор бросит StopIteration
print(type(gen))
print(gen)
# таким образом, генератор аналогичен конструкции RandomIterator
for i in gen:
    print(i)


# Самый простой пример:
def simple_gen():
    print('Checkpoint 1')
    yield 1
    print('Checkpoint 2')
    yield 2
    print('Checkpoint 3')

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))    # Checkpoint 3, StopIteration

# В генератор можно вставить return, это будет равносильно вызову StopIteration
# Если вернуть что-то конкретное, то это станет сообщением внутри StopIteration:

def simple_gen():
    print('Checkpoint 1')
    yield 1
    print('Checkpoint 2')
    return 'No more elements'
    yield 2
    print('Checkpoint 3')

gen = simple_gen()
print(next(gen))
print(next(gen))    # Checkpoint 3, StopIteration: No more elements
print(next(gen))



def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibon(100))

def fibon_g(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(fibon_g(100))

for x in fibon_g(100):
    print(x)
