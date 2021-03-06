'''
В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали
для него программу, по которой робот, когда заходит в комнату, считает количество программистов в ней и
произносит его вслух: "n программистов".

Для того, чтобы это звучало правильно, для каждого nn нужно использовать верное окончание слова.

Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное),
выводящее это число в консоль вместе с правильным образом изменённым словом "программист", для того,
чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.

В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи,
как минимум до 1000 человек.

Дополнительный комментарий к условию:
Обратите внимание, что задача не так проста, как кажется на первый взгляд.
Если ваше решение не проходит какой-то тест, это значит, что вы не рассмотрели какой-то из случаев входных данных
(число программистов 0≤n≤10000≤n≤1000). Обязательно проверяйте свои решения на дополнительных значениях,
а не только на тех, что приведены в условии задания.

Так как задание повышенной сложности, вручную код решений проверяться не будет.
Если вы столкнулись с ошибкой в первых четырёх тестах, проверьте, что вы используете только русские
символы для ответа. В остальных случаях ищите ошибку в логике работы программы.
'''

# put your python code here
a = int(input())
word = 'программист'

b = a % 100
if 11 <= b <= 19:
    ending = 'ов'
else:
    c = b % 10
    if c == 1:
        ending = ''
    elif c == 2 or c == 3 or c == 4:
        ending = 'а'
    else:
        ending = 'ов'

print(str(a) + ' ' + word + ending)


# еще вариант
a = int(input())

mapping = {
    1: '',
    2: 'а',
    3: 'а',
    4: 'а',
    5: 'ов',
    6: 'ов',
    7: 'ов',
    8: 'ов',
    9: 'ов',
    0: 'ов',
}
exception = (11, 12, 13, 14)
if a % 100 in exception:
    print(a, 'программистов')
else:
    print(a, 'программист' + mapping[a % 10])
