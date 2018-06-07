"""
Реализуйте программу, которая будет вычислять количество различных объектов в списке.
Два объекта a и b считаются различными, если a is b равно False.

Вашей программе доступна переменная с названием objects, которая ссылается на список, 
содержащий не более 100 объектов. Выведите количество различных объектов в этом списке.

Формат ожидаемой программы:

ans = 0
for obj in objects: # доступная переменная objects
    ans += 1

print(ans)

Примечание:
Количеством различных объектов называется максимальный размер множества объектов, 
в котором любые два объекта являются различными.

Рассмотрим пример:
objects = [1, 2, 1, 2, 3] # будем считать, что одинаковые числа соответствуют одинаковым объектам, 
а различные – различным

Тогда все различные объекты являют собой множество {1, 2, 3}﻿. 
Таким образом, количество различных объектов равно трём.
"""

objects = [1, 2, 1, 2, 3]

print(len(set(id(i) for i in objects)))
