'''
Поле для игры сапёр представляет собой сетку размером n×m. В ячейке сетки может находиться 
или отсутствовать мина. 

Напишите программу, которая выводит "решённое" поле, т.е. для каждой ячейки, не являющейся миной, 
указывается число мин, находящихся в соседних ячейках (учитывая диагональные направления)

Формат ввода:
На первой строке указываются два натуральных числа 1≤n,m≤100, после чего в n строках содержится описание поля 
в виде последовательности точек '.' и звёздочек '*', где точка означает пустую ячейку, а звёздочка − ячейку с миной.

Формат вывода:
n строк поля, в каждой ячейке которого будет либо число от 0 до 8, либо мина (обозначенная символом "*"), 
при этом число означает количество мин в соседних ячейках поля.

Sample Input:
4 4
..*.
**..
..*.
....

Sample Output:
23*1
**32
23*1
0111
'''


n, m = (int(i) for i in input().split())
a = [[0 if j == '.' else j for j in input()[:m]] for i in range(n)]

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # проверим что ячейка не вышла за пределы поля
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == '*':     # если рядом мина, увеличим
                        a[i][j] += 1
for i in range(n):
    for j in range(m):
        print(a[i][j], end='')
    print()


# Чужой вариант:
n, m = [int(x) for x in input().split()]
stars = [(i, j) for i in range(n) for j, c in enumerate(input()) if c == '*']

for i in range(n):
    for j in range(m):
        if (i, j) in stars:
            print('*', end='')
        else:
            print(sum(1 for x in (i-1, i, i+1) for y in (j-1, j, j+1) if (x, y) in stars), end='')
    print()