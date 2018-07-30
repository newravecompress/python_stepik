'''
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa﻿
'''


str_a = input()
str_b = input()
count = 0


def find_string(string, substring):
    global count
    start = string.find(substring)
    if start != -1:
        count += 1
        find_string(string[start+1:], substring)


find_string(str_a, str_b)

print(count)


# Решение без рекурсии
s = input()
a = input()

if a not in s:
    print(0)
else:
    ans = 0
    while a in s:
        start = s.find(a)
        s = s[start+1:]
        ans += 1

    print(ans)


# Еще решение
s = input()
t = input()
ans = 0
for i in range(len(s)):
    if s[i:].startswith(t):
        ans += 1

print(ans)


# Еще короче
s = input()
t = input()

print(sum(1 for i in range(len(s)) if s.startswith(t, i)))


# Решение с генератором
s, a = (input() for _ in range(2))

def repl_gen(s, a):
    while a in s:
        start = s.find(a)
        s = s[start+1:]
        yield True

print(0 if a not in s else sum(repl_gen(s, a)))
