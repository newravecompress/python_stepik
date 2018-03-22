# чтение и запись в файл


inf = open('file.txt', 'r')     # open('file.txt') - можно и так
s1 = inf.readline()
s2 = inf.readline()     # readline - чтение по одной строке
inf.close()             # закрытие файла


with open('text.txt') as inf:       # спец конструкция для работы с файлами
    s1 = inf.readline()
    s2 = inf.readline()             # закрывать не надо - для этого есть with


# полезные функции:
s = inf.readline().strip()          # удаление пробельных символов


import os
os.path.join('.', 'dirname', 'filename.txt')    # './dirname/filename.txt' - в линуксе, в винде будет \


with open('input.txt') as inf:      # еще одна конструкция, последовательное чтение по строкам
    for line in inf:
        line = line.strip()
        print(line)

with open('lorem.txt') as lorem_file:
    lines = lorem_file.readlines()      # list returns
    print(lines)

with open('lorem.txt') as lorem_file:
    contents = lorem_file.read()        # string returns
    print(contents)


# Запись в файл

ouf = open('file.txt', 'w')
ouf.write('Some text \n')
ouf.write(str(25))          # необходимо, чтобы записываемое значение было строчного типа
ouf.close()

with open('text.txt', 'w') as ouf:
    ouf.write('Some text \n')
    ouf.write(str(25))
