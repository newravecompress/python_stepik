"""
Целое положительное число называется простым, если оно имеет ровно два различных делителя, 
то есть делится только на единицу и на само себя.
Например, число 2 является простым, так как делится только на 1 и 2. Также простыми являются, 
например, числа 3, 5, 31, и еще бесконечно много чисел.
Число 4, например, не является простым, так как имеет три делителя – 1, 2, 4. 
Также простым не является число 1, так как оно имеет ровно один делитель – 1.

Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, 
начиная с числа 2.

Пример использования:

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
"""

import itertools


def primes():
    a = 1
    fact = 1
    while True:  # просто пример
        fact *= a
        a += 1
        if (fact + 1) % a == 0:
            yield a


print(list(itertools.takewhile(lambda x: x <= 31, primes())))


# Еще один вариант генератора
def primes():
    k = 2
    while True:
        if all(k % i for i in range(2, int(k ** 0.5) + 1)):
            yield k
        k += 1


def primes():
    c = 1
    while 1:
        c += 1
        if not [1 for i in range(2, c) if not c % i]:
            yield c


# Самое быстрое по скорости и занимаемой памяти решение:
def primes():
    i = 2
    while True:
        is_prime = True
        divisor = 2
        while divisor ** 2 <= i:
            if i % divisor == 0:
                is_prime = False  # non-trivial divisor
                break

            divisor += 1

        if is_prime:
            yield i

        i += 1
