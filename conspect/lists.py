# lists
students = ['Ivan', 'Masha', 'Sasha']
for student in students:
    print('Hello', student, '!')

len(students)           # list length
students[0]             # Ivan
students[2]             # Sasha
students[-1]            # Sasha
students[:2]            # 0,1 element
students[::-1]          # all elements in reverse order

# addition of lists
teachers = ['Oleg', 'Alex']
students + teachers     # Ivan, Masha ... Oleg, Alex
[0,1]*3                 # [0,1,0,1,0,1]

# lists are the mutable objects
students[1] = 'Oleg'        # Ivan, Oleg, Sasha
students.append('Olga')     # adding to the end
students += ['Olga']        # also adding to the end
students.insert(1, 'Olga')  # put in first place
students.remove('Sasha')    # delete first occurrence

# if we want to delete by index, we must use the 'del' function
del(students[1])
del students[0]

# stack
stack = [1, 2, 3]
stack.append(4)
stack.append(5)
stack.pop()     # 5 - returns the last element
stack.pop(1)    # возвращает первый элемент и сокращает список

# que
from collections import deque       # we need to import module
queue = deque([1, 2, 3, 4])
queue.append(5)
queue.append(6)
queue.append(7)
queue                   # returns deque([1, 2, 3, 4, 5, 6, 7])
queue.popleft()         # return 1
val = queue.popleft()   # val will be 2

if 'Ivan' in students:
    print('Ivan is here!')              # Проверка на наличие в списке
if 'Ann' not in students:
    print('Ann is out')

students.index('Sasha')                 # Возврат индекса
ordered_students = sorted(students)     # сортировка, возвращает новый список
students.sort()                         # тоже сортировка, но сортирует текущий список

# Необходимо, чтобы в списке были сравнимые значения
# тогда сортировка и сравнение будет происходить ожидаемым образом
students.reverse()          # в обратном порядке
reversed(students)          # тоже в обратном порядке, но мы получим копию
students[::-1]              # тоже что и выше, сам список не меняется

# списки передаются по ссылке!!!


# генерация списков
a = [0]*5
a = [0 for i in range(5)]
a = [i*i for i in range(5)]
a = [int(i) for i in input().split()]

# генерация двумерных списков
n = 3
a = [[0*n]*n]   # квадратная матрица с нулевыми элементами
a[0][0] = 5     # у всех первых элементов будет стоять 5
# так происходит потому, что мы сгенерировали один список и размножили его, в итоге другие списки
# будут ссылаться на первый
# правильная генерация будет следующей:
a = [[0]*n for i in range(n)]
a = [[0 for j in range(n)] for i in range (n)]

# special function:
list('word')    # make a list from a string

# поиск минимального элемента в списке
list = [int(i) for i in input().split()]
min = list[0]

for i in list:
    if i < min:
        min = i
