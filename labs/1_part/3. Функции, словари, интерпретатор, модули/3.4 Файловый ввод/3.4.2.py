'''
На прошлой неделе мы сжимали строки, используя кодирование повторов.
Теперь нашей задачей будет восстановление исходной строки обратно.

Напишите программу, которая считывает из файла строку, соответствующую тексту,
сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz.
В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка "download your dataset".
Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер.
Запустите вашу программу, используя этот файл в качестве входных данных.
Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.
'''

str = 'Y6r4R7H6W19S1Z3K18f18K8j4X14T10Y17M15k13m8E12D14L18g2B19Z7u9B19I16W17J4W8H10'
list = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
length = len(str)
num_str = ''
final_str = ''

for i in range(length):
    if str[i].lower() in alphabet:
        list.append(str[i])
    else:
        num_str += str[i]
        if i+1 >= length or str[i+1].lower() in alphabet:
            list.append(int(num_str))
            num_str = ''

for i in range(0, len(list), 2):
    final_str += list[i] * list[i+1]

print(final_str)


# еще вариант:
str = 'Y6r4R7H6W19S1Z3K18f18K8j4X14T10Y17M15k13m8E12D14L18g2B19Z7u9B19I16W17J4W8H10'
digits = {'0','1','2','3','4','5','6','7','8','9'}
final_str = ''
cur_char = str[0]
cnt_char = "0"

for char in str:
    if char not in digits:
        final_str += cur_char * int(cnt_char)
        cur_char = char
        cnt_char = "0"
    else:
        cnt_char += char

final_str += cur_char * int(cnt_char)
