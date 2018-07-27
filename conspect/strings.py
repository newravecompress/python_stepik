# strings
'string1'
"string2"   # Разницы между одинарной или двойной кавычкой нет
'''multiline
string'''
"""multiline
string"""   # многострочные

'abc' + 'cde'   # конкатенация
'abc'*3     # повторение
len('abc')  # длина строки

# сравнения строк в лексикографическом порядке
'abc' == "abc"
'abc' < 'ac'
'abc' > 'ab'

'\n'    # перевод строки
print('String', 'Another string')       # по умолчанию соединяет строки по пробелу
print('First line', '\n\n\n', 'Last line')  # вставит 3 перевода строки между линиями
print('First line', end=" ")    # end - это символ после принта, по-умолчанию \n

# строки
genome = 'ATGC'
genome[0]   # A
genome[-1]  # C
genome[1] = 'c' # ошибка - строки неизменяемы

# for можно использовать для перебора символов строки
for c in genome:
    print(c)

s = 'aTbgdaDCGcc'
p = 'cc'
s.upper()   # к верхнему регистру
s.lower()   # к нижнему регистру
s.find(p)   # где встречается в первый раз
s.find('u') # -1 - нигде не встречается

# для проверки вхождения подстроки лучше использовать if i in string
print('abc' in 'abcba')     # True
print('abce' in 'abcba')    # False

# .find имеет другие аргументы
print('cabcad'[1:].find('abc'))     # 0
print('cabcabcd'.find('abc', 2))    # 4 - поиск начиная с третьего элемента

# .index - аналог .find, но бросает ошибку ValueError, если ничего не найдено
print('abcba'.index('abc'))     # 0
print('abcba'.index('abce'))    # ValueError: substring not found

# поиск в начале
s = 'The man in black fled across the desert'
print(s.startswith('The man in black'))
print(s.startswith(('The man in black', 'The woman', 'The dog')))   # Начинается ли с какой-либо из этих строк

# поиск в конце
s = 'The man in black fled across the desert'
print(s.endswith('desert'))

# количество вхождений подстроки
print('ababa'.count('aba'))   # 1, рассматриваются неперекрывающиеся последовательности

s.replace('a', 'A')     # заменяет ВСЕ вхождения первого символа на второй
s.upper().count('gt'.upper())   # последовательный вызов команд

# У многих функций есть правосторонний аналог
print('abababa'.rfind('aba'))

s = "_*__1, 2, 3, 4__*_"
print(repr(s.rstrip('*_')))
print(repr(s.lstrip('_*')))

numbers = map(str, [1, 2, 3, 4, 5])
print(repr(' '.join(numbers)))      # '1 2 3 4 5'

# все эти операции не изменяют строку
# для изменения строки необходимо сделать присвоение

# slicing
dna = 'ATGGCCTAGCGCTA'
dna[1]      # T
dna[1:4]    # TGG с первого по четвертый, не включая четвертый
dna[:4]     # ATGG с нуля до четвертого
dna[4:]     # CCTAGCGCTA с четвертого до конца
dna[-4:]    # GCTA с четвертого от конца до конца
dna[1:-1]   # TGGCCTAGCGCT от первого до предпоследнего
dna[1:-1:2] # от первого до предпоследнего с шагом 2
dna[::-1]   # все символы в обратном порядке


# Форматирование
capital = 'London is the capital of Great Britain'
template = '{} is the capital of {}'
print(template.format('London', 'Great Britain'))
print(template.format('Vaduz', 'Liechtenstein'))
# Именованные аргументы
template = '{capital} is the capital of {country}'
print(template.format(capital='London', country='Great Britain'))
# форматирование поддерживает доступ к атрибутам
import requests
template = 'Response from {0.url} with code {0.status_code}'
res = requests.get('https://docs.python.org/3.5/')
print(template.format(res))
# а также ограничения длин
from random import random
x = random()
print(x)
print('{:.3}'.format(x))
