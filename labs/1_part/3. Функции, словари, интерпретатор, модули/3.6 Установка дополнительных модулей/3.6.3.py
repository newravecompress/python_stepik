'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''

import requests

res = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
count = 0

while 'We' not in res.text:
    request = 'https://stepic.org/media/attachments/course67/3.6.3/' + res.text.strip()
    res = requests.get(request)
    count += 1

print(res.text)
print(count)
