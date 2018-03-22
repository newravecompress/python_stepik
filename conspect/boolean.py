# Boolean type
False(0)
True(1)
# or, and, not
# < > <= >= == !=
a = int(input())
print(10 <= a < 100)    # совмещенное условие
a, b, c = False, True, False    # присвоение через перечисление
# not > and > or
not a and b or c        # True
# Порядок выполнения операций: арифметические - сравнения - логические
x = 5
y = 10
y > x * x or y >= 2 * x and x < y   # True

a = True
b = False
a and b or not a and not b          # False


