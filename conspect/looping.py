# while
a = 5
while a > 0:
    print(a, end=' ')
    a -= 1

number = 10
while number < 10:
    if number == 5:
        number += 1
        continue
    print(number)
    number += 1
else:
    print('Condition is false')     # Если условие не было выполнено ни разу


i = 0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if (a == 0) and (b == 0):
        break       # досрочное завершение цикла
    if (a == 0) or (b == 0):
        continue    # продолжить со следующей итерации
    print(a * b)
    i += 1


# for
for i in 2,3,5:
    print(i*i)      # 4,9,25

for i in range(10):
    print(i*i)      # 0,1,4...81

# сумма нечетных чисел на интервале с помощью генератора
a, b = (int(i) for i in input().split())
s = 0
if a % 2 == 0:
    a += 1
for i in range (a, b+1, 2):
    s += i
print(s)


students = ['Ivan', 'Masha', 'Sasha', 'Oleg', 'John']
for i in students[1:3]: # также можно проходить по срезам
    print(i)
