'''
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, 
когда с момента исходной даты date пройдет число дней, равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.
'''

import datetime

date_list = input().split(' ')
date = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
plus = int(input())
delta = datetime.timedelta(days=plus)
new_date = date+delta
new_date = new_date.strftime("%Y %m %d").replace(" 0", " ")

print(new_date)
