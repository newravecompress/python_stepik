'''
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
'''

def modify_list(l):
    # put your python code here
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


def modify_list2(l):
    # Здесь нам нужно обратиться к самому списку, поэтому делаем [:]
    # Если просто присваивать, то будет создан новый список
    l[:] = [i//2 for i in l if i % 2 == 0]
