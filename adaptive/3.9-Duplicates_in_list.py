"""
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку
значения, которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

Sample Input:
4 8 0 3 4 2 0 3

Sample Output:
0 3 4
"""

# list = [int(i) for i in input().split()]
# final = []
# list.sort()
#
# for i in range(len(list) - 1):
#     if list[i] == list[i + 1]:
#         if list[i] not in final:
#             final.append(list[i])
#
# str_final = ''
# for el in final:
#     str_final += str(el)
#     str_final += ' '
# print(str_final)
#
#
# # еще вариант
# inl = input().split()
# outl = set(n for n in inl if inl.count(n) > 1)
# print(' '.join(outl))


'''
Попробуйте решить эту задачу следующими способами:
1. Отсортировать список и найти дубликаты.
2. Использовать класс collections.Counter.
3. Использовать множества.
'''

# 3. Использовать множества.
from collections import *

inl = input().split()
c = Counter(inl)
for key, cnt in c.items():
    if cnt > 1:
        print(key)



