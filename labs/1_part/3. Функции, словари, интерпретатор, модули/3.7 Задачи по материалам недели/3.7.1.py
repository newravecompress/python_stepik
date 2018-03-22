'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча 
и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.
'''

count = int(input())
clubs = {}

for i in range(count):
    game = input().split(';')

    for i in range(0, len(game), 2):
        if game[i] not in clubs:
            clubs[game[i]] = {'game': 1, 'win': 0, 'tie': 0, 'defeat': 0, 'scores': 0}
        else:
            clubs[game[i]]['game'] += 1

    if int(game[1]) > int(game[3]):
        clubs[game[0]]['win'] += 1
        clubs[game[0]]['scores'] += 3
        clubs[game[2]]['defeat'] += 1
    elif int(game[1]) == int(game[3]):
        clubs[game[0]]['tie'] += 1
        clubs[game[0]]['scores'] += 1
        clubs[game[2]]['tie'] += 1
        clubs[game[2]]['scores'] += 1
    else:
        clubs[game[2]]['win'] += 1
        clubs[game[2]]['scores'] += 3
        clubs[game[0]]['defeat'] += 1


for key, val in clubs.items():
    print(key + ':', end='')
    for val2 in val.values():
        print(val2, end=' ')
    print()




