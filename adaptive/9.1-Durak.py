"""
A durak deck contains 36 cards. Each card has a suit of either 
clubs, diamonds, hearts, or spades (denoted C, D, H, S). 
Each card also has a value of either 6 through 10, jack, queen, king, or ace 
(denoted 6, 7, 8, 9, 10, J, Q, K, A). For scoring purposes card values are ordered as above,
with 6 having the lowest and ace the highest value.

Напишите программу, которая определяет, бьёт ли одна карта другую.
Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
Если карты разных мастей и нет козырных, то никто не побеждает.

Формат ввода:
На первой строке через пробел указываются две карты в формате <значение><масть>, 
а на следующей строке указывается козырная масть.

Формат вывода:
Программа должна вывести слово 
First, если первая карта бьёт вторую, 
Second, если вторая карта бьёт первую,
Error, если ни одна из карт не может побить другую.

Sample Input 1:
AH JH
D
Sample Output 1:
First

Sample Input 2:
AH JS
S
Sample Output 2:
Second

Sample Input 3:
7C 10H
S
Sample Output 3:
Error
"""

cards = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

first, second = input().split()
trump = input()

if first[-1] == second[-1]:
    if cards.index(first[:-1]) > cards.index(second[:-1]):
        print('First')
    elif cards.index(first[:-1]) < cards.index(second[:-1]):
        print('Second')
    else:
        print('Error')
elif first[-1] == trump:
    print('First')
elif second[-1] == trump:
    print('Second')
else:
    print('Error')


# Еще

(card1, card2), trump = input().split(), input()

s1, s2 = card1[-1], card2[-1]
d1, d2 = '678910JQKA'.index(card1[:-1]), '678910JQKA'.index(card2[:-1])

if s1 == s2:
    who = 0 if d1 > d2 else 2 if d1 < d2 else 1
else:
    who = 0 if s1 == trump else 2 if s2 == trump else 1
print(["First", "Error", "Second"][who])


