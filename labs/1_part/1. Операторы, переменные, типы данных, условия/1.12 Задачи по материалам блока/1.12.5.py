'''
Напишите программу, которая получает на вход три целых числа, по одному числу в строке,
и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.
'''

a = int(input())
b = int(input())
c = int(input())

if a > b:
    max = a
    min = b
else:
    max = b
    min = a

if max < c:
    mid = max
    max = c
elif c > min:
    mid = c
else:
    mid = min
    min = c

print(max)
print(min)
print(mid)


# еще вариант
l = [int(input()) for _ in range(3)]

l.sort()
print(l[2])
print(l[0])
print(l[1])
