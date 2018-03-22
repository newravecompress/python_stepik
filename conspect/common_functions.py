# input and output
input()                 # read a string
input('Введите данные')
print('some output')    # output to the console
int('45')               # 45
int('  45 ')            # 45
str(912)

a = 5
b = 10
print(a, b)                                 # output through the space
print('First line', '\n\n\n', 'Last line')  # вставит 3 перевода строки между линиями
print('First line', end = ' ')              # end - это символ после принта, по-умолчанию \n
print('Second line')

len('string')  # returns a length of an iterable object

sorted(['Ivan', 'Masha', 'Sasha'])  # returns the list of sorted elements

# type definitions
type(7)  # int
type(7.0)  # float

# range возвращает последовательность чисел
range(5)  # 0,1,2,3,4 - все числа от нуля до 5 с шагом 1, не включая 5
range(2, 5)  # 2,3,4
range(2, 20, 4)  # 2,6,10,14,18 - третий аргумент - шаг

list('word')  # make a list from a string
