'''
Недавно мы считали для каждого слова количество его вхождений в строку. 
Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла 
(в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, 
сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое 
(можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.
'''

str = ''

with open('3.4.3.txt', 'r') as file:
    for line in file:
        str += line.strip() + ' '

str.strip()

list = {}
new_list = []

for i in str.lower().split():
    if i in list:
        list[i] += 1
    else:
        list[i] = 1

max_val = 0
max_key = ''
max_pair = {}

for key, val in list.items():
    if val > max_val:
        max_val = val
        max_key = key

for key, val in list.items():
    if val >= max_val and key <= max_key:
        max_pair = {key: val}

print(max_pair)
