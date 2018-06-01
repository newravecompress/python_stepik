"""
Последовательность n>0 целых чисел называется jolly jumper в случае, если значения абсолютных разностей 
последовательных элементов принимают все возможные значения между 1 и n−1.

Например, последовательность 1 -3 -4 -1 1 является jolly jumper последовательностью, так как абсолютные 
разности равны 4 1 3 2, соответственно, а n−1=4.
Будем считать, что последовательность из одного числа является jolly jumper.

Напишите программу, которая проверяет, является ли введённая последовательность jolly jumper.

Формат ввода:

Строка, содержащая 1≤n≤10000 целых чисел, разделённых пробелом.

Формат вывода:
Одна строка, содержащая "Jolly" (без кавычек), если последовательность является jolly jumper и 
"Not jolly" в противном случае.

Sample Input 1:
1 -3 -4 -1 1
Sample Output 1:
Jolly

Sample Input 2:
1 3 5
Sample Output 2:
Not jolly

Sample Input 3:
4
Sample Output 3:
Jolly
"""

sequence = [int(i) for i in input().split()]
diff_list = [i for i in range(1, len(sequence))]

if len(sequence) == 1:
    print('Jolly')
else:
    for i in range(0, len(sequence) - 1):
        dif = abs(sequence[i] - sequence[i + 1])
        if dif in diff_list:
            diff_list.remove(dif)
        else:
            print('Not jolly')
            break
    if not diff_list:
        print('Jolly')


# Короче
nums = tuple(int(i) for i in input().split())

is_jolly = sorted(abs(nums[i] - nums[i-1]) for i in range(1, len(nums))) == list(range(1, len(nums)))

print('Jolly' if is_jolly else 'Not jolly')
