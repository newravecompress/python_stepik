'''
Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки,
которая выводит все позиции, на которых встречается число xx в переданном списке lstlst.

Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует"
(без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
'''

l = [int(i) for i in input().split()]

num = int(input())
num_list = []

for i in range(len(l)):
    if l[i] == num:
        num_list.append(i)

if len(num_list) == 0:
    print('Отсутствует')
else:
    for i in num_list:
        print(str(i), end=' ')

# еще вариант
lst = [int(i) for i in input().split()]
x = int(input())
if x not in lst:
    print('Отсутствует')
else:
    for i in range(len(lst)):
        if lst[i] == x:
            print(i, end=' ')

