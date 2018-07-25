# чтение и запись в файл

inf = open('file.txt', 'r')
s1 = inf.readline()
s2 = inf.readline()     # readline - чтение по одной строке
inf.close()             # закрытие файла

inf = open('file.txt')    # по умолчанию режим 'r', для чтения файл должен существовать
s1 = inf.read()     # Получить все содержимое файла
s2 = inf.read(5)    # Получить первые пять символов
print(s1)
print(repr(s1))     # Вывод символов "как есть", то есть перенос строки - это \n
inf.close()

inf = open('file.txt', 'r')
x = inf.read()
x = x.splitlines()
print(repr(x))  # ['First line', 'Second line', 'Third line']
inf.close()

f = open('file.txt')
for line in f:          # Проитерироваться по строкам
    print(repr(line))
x = f.read()
print(repr(x))      # После окончания итераций будет возвращаться пустая строка
f.close()


with open('text.txt') as inf:       # спец конструкция для работы с файлами
    s1 = inf.readline()
    s2 = inf.readline()             # закрывать не надо - для этого есть with
    # полезные функции:
    s = inf.readline().strip()      # удаление пробельных символов
    s = inf.readline().lstrip()     # Удаление слева
    s = inf.readline().rstrip()     # Удаление справа


with open('input.txt') as inf:      # еще одна конструкция, последовательное чтение по строкам
    for line in inf:
        line = line.strip()
        print(line)

with open('lorem.txt') as lorem_file:
    lines = lorem_file.readlines()      # list returns
    print(lines)


# Запись в файл

ouf = open('file.txt', 'w')
ouf.write('Some text \n')
ouf.write(str(25))          # необходимо, чтобы записываемое значение было строчного типа
ouf.close()

with open('text.txt', 'w') as ouf:
    ouf.write('Some text \n')
    ouf.write(str(25))

with open('text.txt', 'w') as ouf:
    lines = ['first', 'second', 'third']
    contents = '\n'.join(lines)     # Запись с разбивкой по строкам
    ouf.write(contents)

# with позволяет работать сразу с несколькими файлами
with open('test.txt') as f, open('test2.txt', 'w') as w:
    for line in f:
        w.write(line)


import os
os.path.join('.', 'dirname', 'filename.txt')    # './dirname/filename.txt' - в линуксе, в винде будет \
print(os.listdir())                 # listdir - получить список текущих директорий
print(os.listdir('.idea'))          # с аргументами - получить список директорий по адресу
print(os.getcwd())                  # Получить текущую директорию
print(os.path.exists('files.py'))   # Узнать существует ли
print(os.path.isfile('files.py'))   # Узнать файл
print(os.path.isdir('test'))        # Узнать директорию
print(os.path.abspath('file.py'))   # Путь до указанного файла
os.chdir('.idea')                   # Сменить директорию

# Перебор директорий и файлов
for current_dir, dirs, files in os.walk('.'):
    print(current_dir, dirs, files)

# Копирование файлов и директорий
import shutil
shutil.copy('tests/test.txt', 'tests/test2.txt')
shutil.copytree('tests', 'tests2')

