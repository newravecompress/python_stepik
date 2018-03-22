'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j
равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''

matrix = []

while True:
    string = input()
    if string == 'end':
        break

    row = [int(i) for i in string.split()]
    matrix.append(row)

high = len(matrix)
width = len(matrix[0])

new_matrix = [[0 for i in range(width)] for j in range(high)]

for i in range(high):
    for j in range(width):
        new_matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        if j == width-1 and i == high-1:
            new_matrix[i][j] += matrix[0][j] + matrix[i][0]
        elif j == width-1:
            new_matrix[i][j] += matrix[i+1][j] + matrix[i][0]
        elif i == high-1:
            new_matrix[i][j] += matrix[0][j] + matrix[i][j+1]
        else:
            new_matrix[i][j] += matrix[i+1][j] + matrix[i][j+1]

for row in new_matrix:
    for col in row:
        print(col, end=' ')
    print()
