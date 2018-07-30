"""
Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba",
после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s﻿.

Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a,
либо же определить, что это невозможно.

Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a.
Если после применения любого числа операций в строке s останутся вхождения строки a, выведите Impossible.

Sample Input 1:
ababa
a
b

Sample Output 1:
1

Sample Input 2:
ababa
b
a

Sample Output 2:
1

Sample Input 3:
ababa
c
c

Sample Output 3:
0

Sample Input 4:
ababac
c
c

Sample Output 4:
Impossible
"""


orig_string = input()
str_a = input()
str_b = input()
count = 0

def str_replace(string, str_a, str_b):
    global count
    if str_a in string:
        if str_a in str_b:
            print('Impossible')
        else:
            new_string = string.replace(str_a, str_b)
            count += 1
            str_replace(new_string, str_a, str_b)
    else:
        print(count)

str_replace(orig_string, str_a, str_b)

# Решение без рекурсии
s = input()
a = input()
b = input()

if a not in s:
    print(0)
elif a in b:
    print("Impossible")
else:
    ans = 0
    while a in s:
        s = s.replace(a, b)
        ans += 1

    print(ans)


# Решение с генератором
s, a, b = (input() for _ in range(3))

def repl_gen(s, a, b):
    while a in s:
        s = s.replace(a, b)
        yield True

print('Impossible' if a in b and a in s else sum(repl_gen(s, a, b)))
