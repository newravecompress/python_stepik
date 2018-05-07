"""
Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:

f(x)=⎧⎩⎨⎪⎪1−(x+2)2,−x2,(x−2)2+1,при x≤−2при −2<x≤2при 2<x
f(x)={1−(x+2)2,при x≤−2−x2,при −2<x≤2(x−2)2+1,при 2<x
Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.
"""


def f(x):
    # put your python code here
    if x <= -2:
        func = 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        func = - x / 2
    else:
        func = (x - 2) ** 2 + 1
    return func


# с помощью словаря:
def f(x):
    d = {
        x <= -2: 1 - (x + 2) ** 2,
        -2 < x <= 2: -x / 2,
        2 < x: (x - 2) ** 2 + 1
    }
    return d[True]