'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, 
где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой 
и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке, 
соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, 
физике и русскому языку по всем абитуриентам:

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом: 
print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
'''

str = ''
lines = []
average = []
student_average = []

with open('3.4.4.txt', 'rb') as file:
    for line in file:
        lines.append(line.decode('utf-8').rstrip().split(';'))

sum_math = 0
sum_phys = 0
sum_lang = 0
length = len(lines)



for student in lines:
    student_marks = student[1:]
    student_len = len(student_marks)
    student_sum = 0
    for mark in student_marks:
        student_sum += int(mark)
    student_average.append(student_sum / student_len)

    sum_math += int(student[-3])
    sum_phys += int(student[-2])
    sum_lang += int(student[-1])

average.append(sum_math / length)
average.append(sum_phys / length)
average.append(sum_lang / length)

for stud in student_average:
    print(stud, end='\n')
for mark in average:
    print(mark, end=' ')

# average = []
# for line in lines:
#     student = line.split(';')[1:]
#     av = 0
#     for mark in student:
#         av += int(mark)
#     av_mark = av / len(student)
#     average.append(av_mark)
#
# print(average)



