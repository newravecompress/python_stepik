# арифметические операции
10 / 2      # 5.0 - после деления всегда будет float
2 * 5.0     # 10.0  тоже самое
17 / 3      # 5.6666666..
17 // 3     # 5 - целочисленное деление
42 % 8      # 2, остаток от целочисленного деления
# Деление на ноль запрещено!
249 // 10   # 24
249 % 10    # 9
2 ** 4      # 16 - возведение в степень
+--+42      # синтаксически верная запись

0.3 + 0.5   # 0.8
# у чисел с плавающей точкой присутствует погрешность
0.3 + 0.3 + 0.3 # 0.8999999...
9 ** 0.5        # 3.0 - при взятии корня возвращается float
9.0 ** 2        # 81.0  вернет float
5e-1            # 0.5
int(2.3)        # 2 - отбрасывается дробная составляющая
int(2.6)        # 2 - отбрасывается дробная составляющая
float(5)        # 5.0
9**19 - int(float(9**19)) # 89
7.0 % 2         # 1.0 - тип сохраняется
7 % 2           # 1
# определение типа
type(7)         # int
type(7.0)       # float

# += -= *= /= //= %= **= # поддерживаемые операторы