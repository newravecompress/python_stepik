'''
В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: 
они говорили каким-то странным набором звуков. 

В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении 
подстановочный шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. 
Биологи раздобыли ключ к шифру и теперь нуждаются в помощи: 

Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. 
Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, 
на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, 
и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. 
Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac
'''

initial = input()
final = input()
string_to_encrypt = input()
string_to_decrypt = input()
map_to = {}
map_from = {}

for i in range(len(initial)):
    map_to[initial[i]] = final[i]
    map_from[final[i]] = initial[i]

encrypted_string = ''
for letter in string_to_encrypt:
    encrypted_string += map_to[letter]

decrypted_string = ''
for letter in string_to_decrypt:
    decrypted_string += map_from[letter]


print(encrypted_string)
print(decrypted_string)


# еще вариант
fr = input()
to = input()
encode_dict = dict(zip(fr, to))
decode_dict = dict(zip(to, fr))

print(''.join([encode_dict[s] for s in input()]))
print(''.join([decode_dict[s] for s in input()]))

