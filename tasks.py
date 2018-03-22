'''
сапер!!!
'''
n, m, k = (int(i) for i in input().split())         # получаем на вход параметры поля
a = [[0 for j in range(m)] for i in range(n)]       # формируем пустое поле
for i in range(k):                                  # количество мин
    row, col = (int(i) - 1 for i in input().split())    # получаем координаты мин
    a[row][col] = -1                                # вставляем мины в таблицу

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # проверим что ячейка не вышла за пределы поля
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:     # если рядом мина, увеличим
                        a[i][j] += 1
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()



