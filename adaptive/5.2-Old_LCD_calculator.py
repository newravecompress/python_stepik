"""
Напишите программу, которая выводит число в стиле LCD калькулятора.

На вход программе подаётся последовательность цифр, которую нужно вывести на экран в специальном стиле 
(см. пример).

Размер всех цифр 4 символа в ширину и 7 символов в высоту. Между цифрами в выводе должен быть один пустой столбец. 
Перед первой цифрой не должно быть пробелов.

Выведенные цифры должны быть обведены рамочкой, в углах которой находится символ x ("икс"), 
горизонтальная линия создаётся из символа - ("дефис"), а вертикальная -- из символа вертикальной черты: |.

Формат ввода:
Строка произвольной длины (минимум один символ), содержащая последовательность цифр.

Формат вывода:
9 строк, содержащих цифры, записанные в указанном в задании формате.

Sample Input:

0123456789
Sample Output:

x-------------------------------------------------x
| --        --   --        --   --   --   --   -- |
||  |    |    |    | |  | |    |       | |  | |  ||
||  |    |    |    | |  | |    |       | |  | |  ||
|           --   --   --   --   --        --   -- |
||  |    | |       |    |    | |  |    | |  |    ||
||  |    | |       |    |    | |  |    | |  |    ||
| --        --   --        --   --        --   -- |
x-------------------------------------------------x
"""


'''
Улучшения:

1. Сделайте размер цифры параметром size. Пусть ширина цифры будет равна в таком случае (size + 2), 
а высота, соответственно, (2 * size + 3). В задании рассмотрен случай с size == 2. 
Ниже приведён пример записи цифры 8 с size == 3:

 --- 
|   |
|   |
|   |
 --- 
|   |
|   |
|   |
 --- 
2. Напишите простой калькулятор, который бы выводил свои действия на экран в таком виде. 
Придумайте самостоятельно свой формат вывода знаков арифметических операций.
'''
