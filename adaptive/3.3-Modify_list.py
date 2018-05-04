"""
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка,
например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
"""
'''
Попробуйте решить эту задачу следующими способами:
1. Используя метод pop (необходимо правильным образом построить итерацию по списку).
2. Используя механизм slice и генераторы списков
'''

lst = [1, 2, 3, 4, 5, 6]

# 1. Используя метод pop (необходимо правильным образом построить итерацию по списку).
def modify_list(l):
    i = 0
    length = len(l)
    while i < length:
        if l[i] % 2 == 1:
            del l[i]
            i -= 1
            length -= 1
        else:
            l[i] = int(l[i]/2)
        i += 1


# 2. Используя механизм slice и генераторы списков
def modify_list2(l):
    # Здесь нам нужно обратиться к самому списку, поэтому делаем [:]
    # Если просто присваивать, то будет создан новый список
    # Копия не должна создаваться. Когда мы пишем l[i:j] = iterable_thing, то имеем в виду:
    # взять из списка элементы с i по j и заменить их на iterable_thing.
    # Опуская i и j, мы берём все элементы от первого до последнего. Mutable Sequence Types
    l[:] = [i//2 for i in l if i % 2 == 0]

modify_list2(lst)
