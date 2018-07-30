'''
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

Примечание:
Считать все строки по одной из стандартного потока ввода вы можете, например, так

import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line
'''


import re
import sys

pattern = r'cat'
for line in sys.stdin:
    line = line.rstrip()
    match = re.findall(pattern, line)
    if len(match) > 1:
        print(line)
