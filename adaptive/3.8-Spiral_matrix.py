"""
Выведите таблицу размером n×n, заполненную целыми числами от 1 до n2 по спирали, 
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере.

Формат ввода:
Одна строка, содержащая одно целое число n, n>0.

Формат вывода:
Таблица из n строк, значения в строках разделены пробелом.

Sample Input:
5

Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""

n = int(input())

# Переменным x и y присваивается начальная координата заполнения матрицы
x = 0
y = 0

# Задаем направления первоначального движения
dx = 0
dy = 1

# Создаем пустую матрицу
arr = [[0] * n for _ in range(n)]

# Выполняем перебор
for i in range(1, n**2+1):
    arr[x][y] = i
    # Создаются временные переменные nx и ny
    # в которых вычисляются новые значения для x и y
    # для этого к старым значенииям прибавляются приращения по текущему направлению
    nx = x + dx
    ny = y + dy

    if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
        # Если индекс не выходит за пределы матрицы и ячейка не заполнена
        # то продолжаем движение в прежнем направлении
        x = nx
        y = ny
    else:
        # а если индекс вышел за пределы, или мы наткнулись на заполенную ячейку,
        # то поворачиваем вектор на 90 градусов
        # тут есть небольшой трюк - если присваивать последовательо, то будут неправильные значения,
        # так как в dy попадет уже измененное значение dx
        dx, dy = dy, -dx
        # и прибавляем полученные новые значения для текущих
        x = x + dx
        y = y + dy

for row in arr:
    for col in row:
        print(col, end=' ')
    print()


# Вариант короче:
n, row, column, dy, dx = int(input()), 0, 0, 0, 1
spiral = [[0] * n for i in range(n)]
for curr in range(n ** 2):
    spiral[row][column] = curr + 1
    if not (-1 < column + dx < n) or not (-1 < row + dy < n) or not (spiral[row + dy][column + dx] == 0):
        dx, dy = -dy, dx
    row, column = row + dy, column + dx
[print(*line) for line in spiral]


"""
Попробуйте решить эту задачу следующими способами:
Заполняя матрицу по спирали, отслеживая направление заполнения.
Не создавая матрицу выводить результат построчно, вычисляя значение в ячейке по её координатам.
"""