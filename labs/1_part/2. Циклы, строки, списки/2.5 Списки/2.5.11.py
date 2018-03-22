'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку
значения, которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
'''
list = [int(i) for i in input().split()]
final = []
list.sort()

for i in range(len(list)-1):
    if list[i] == list[i+1]:
        if list[i] not in final:
            final.append(list[i])

str_final = ''
for el in final:
    str_final += str(el)
    str_final += ' '
print(str_final)

# еще вариант
inl = input().split()
outl = set(n for n in inl if inl.count(n)>1)
print(' '.join(outl))
