'''
Простейшая система проверки орфографии основана на использовании списка известных слов. 
Каждое слово в проверяемом тексте ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.

Напишем подобную систему.

Через стандартный ввод подаётся следующая структура: 
первой строкой — количество dd записей в списке известных слов, 
после передаётся  dd строк с одним словарным словом на строку, 
затем — количество ll строк текста, после чего — ll строк текста.

Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. 
Регистр слов не учитывается. 
Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.
'''

count_words = int(input())
words_list = []
for i in range(count_words):
    words_list.append(input().lower())

count_strings = int(input())
strings_list = []
for j in range(count_strings):
    for k in input().split(' '):
        strings_list.append(k)

final_words = set()
for word in strings_list:
    if word.lower() not in words_list:
        final_words.add(word)


for final in final_words:
    print(final)


# еще вариант
d = int(input())
words = set([input().lower() for _ in range(d)])
l = int(input())
to_check = set()

for i in range(l):
    to_check.update(input().lower().split())

to_check.difference_update(words)
print(*to_check, sep='\n')
