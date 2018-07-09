'''
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:


class B(A):
    pass


Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С


Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных

В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов.
В i-й строке указано от каких классов наследуется i-й класс.
Обратите внимание, что класс может ни от кого не наследоваться.
Гарантируется, что класс не наследуется сам от себя (прямо или косвенно),
что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных

Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.
'''

tree = {}


def is_parent(parent, heir):
    global tree
    result = ''
    if parent in tree[heir]:
        result = True
    elif tree[heir] == ['object']:
        result = False
    else:
        for value in tree[heir]:
            if is_parent(parent, value):
                result = True
                break
            else:
                result = False
    return result


for i in range(int(input())):
    class_str = input().strip()
    if ':' in class_str:
        classes = class_str.split(' : ')
        tree[classes[0]] = [val for val in classes[1].split()]
    else:
        tree[class_str] = ['object']


for j in range(int(input())):
    classes = input().split()
    if classes[0] == classes[1]:
        print('Yes')
    elif is_parent(classes[0], classes[1]):
        print('Yes')
    else:
        print('No')


# Другое решение:
n = int(input())

parents = {}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]

def is_parent(child, parent):
    return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))

q = int(input())
for _ in range(q):
    a, b = input().split()
    print("Yes" if is_parent(b, a) else "No")


# Еще короче:
def isP(pr, ch):
    return ch == pr or any(map(lambda pl: isP(pr, pl), p[ch]))
p = {}
for j in range(2):
    for c in [input().split() for i in range(int(input()))]:
        if j: print(['No', 'Yes'][isP(*c)])
        else: p[c[0]] = c[2:]
