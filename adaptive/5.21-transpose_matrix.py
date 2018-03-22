'''
Напишите программу, которая принимает на вход матрицу, выполняет её транспонирование и выводит результат.

Формат ввода:
В первой строке указываются два целых числа n и m, количество строк и столбцов, соответственно.
Далее следуют n строк, содержащих по m целых чисел, разделённых пробелом.

Формат вывода:
Программа должна вывести m строк содержимого транспонированной матрицы. Элементы матрицы стоит разделять пробелом.

Sample Input 1:
2 3
1 2 3
4 5 6
Sample Output 1:
1 4
2 5
3 6

Sample Input 2:
2 2
1 2
3 4
Sample Output 2:
1 3
2 4
'''

"""мое решение"""
# n, m = (int(i) for i in input().split())
# matrix = [input().split()[:m] for i in range(n)]
# transpose = [[0 for j in range(n)] for i in range(m)]
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         transpose[j][i] = matrix[i][j]
#
#
# for i in transpose:
#     for j in i:
#         print(j, end=' ')
#     print()


"""другие"""
n, m = (int(i) for i in input().split())
for t in zip(*[input().split() for _ in range(n)]):
    print(*t)


