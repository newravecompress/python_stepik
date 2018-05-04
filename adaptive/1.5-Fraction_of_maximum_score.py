"""
Напишите программу, которая вычисляет долю студентов, получивших оценку A.

Используется пятибальная система оценивания с оценками A, B, C, D, F.

Формат ввода:
Строка, в которой через пробел записаны оценки студентов. Оценок всегда не меньше одной.

Формат вывода:
Дробное число с ровно двумя знаками после запятой.

Sample Input 1:
F B A A B C A D
Sample Output 1:
0.38

Sample Input 2:
B C B
Sample Output 2:
0.00

Sample Input 3:
A D
Sample Output 3:
0.50
"""

marks = input().split()
cnt = 0
for i in marks:
    if i == 'A':
        cnt += 1

print('{:.2f}'.format(cnt / len(marks)))

# Более короткий вариант:
sp = input().split()
print('{:.2f}'.format(sp.count('A') / len(sp)))

'''
Попробуйте решить эту задачу следующими способами:

1. Используя метод count строки.
2. Через итерацию циклом for по символам введённой строки.
3. Разбив строку на последовательность оценок и воспользовавшись классом collections.Counter.
'''

# 1. Используя метод count строки.
sp = input()
print('{:.2f}'.format(sp.count('A') / (len(sp) // 2 + 1)))

# 2. Через итерацию циклом for по символам введённой строки.
marks = input()

cnt = 0
for i in marks:
    if i == 'A':
        cnt += 1

print('{:.2f}'.format(cnt / (len(marks) // 2 + 1)))

# 3. Разбив строку на последовательность оценок и воспользовавшись классом collections.Counter.
from collections import *

sp = input()
marks = Counter(sp)
print('{:.2f}'.format(marks['A'] / (len(sp) // 2 + 1)))
