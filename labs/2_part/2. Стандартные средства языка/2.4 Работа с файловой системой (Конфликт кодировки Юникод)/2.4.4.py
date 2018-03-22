'''
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab
'''

with open('text.txt') as file, open('new_text.txt', 'w') as new_file:
    lines = file.readlines()
    for line in reversed(lines):
        new_file.write(line)
