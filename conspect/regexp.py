x = 'hello\nworld'
print(x)

# r'string' - сырая строка, выведется как есть
x = r'hello\nworld'
print(x)

import re
# четыре основные функции
print(re.match)     # определяет совпадение шаблону в начале строки, возвращает совпавшую часть
print(re.search)    # находит первую подстроку, соответствующую шаблону
print(re.findall)   # находит все подстроки, соответствующие шаблону
print(re.sub)       # заменяет все вхождения совпадающих подстрок, возвращает получившуюся строку

pattern = r'abc'
string = 'abc'
print(re.match(pattern, string))    # <_sre.SRE_Match object; span=(0, 3), match='abc'>

pattern = r'abcd'
string = 'abcde'
print(re.match(pattern, string))    # <_sre.SRE_Match object; span=(0, 4), match='abcd'>

pattern = r'abc'
string = 'babc'
print(re.search(pattern, string))   # <_sre.SRE_Match object; span=(1, 4), match='abc'>

pattern = r'abc'
string = 'bfggf'
print(re.search(pattern, string))       # None


# метасимволы
pattern = r'a[abc]c'
string = 'abc, aac, acc'
print(re.findall(pattern, string))
print(re.sub(pattern, 'abc', string))


pattern = r' english?'
string = 'Do you speak english?'
print(re.search(pattern, string))  # <_sre.SRE_Match object; span=(12, 20), match=' english'>
# решается экранированием:
pattern = r' english\?'


pattern = r'a[a-d]c'
string = 'abc, aac, acc, adc'
print(re.findall(pattern, string))


# жадность квантификаторов
pattern = r'a[ab]+a'
string = 'abaaba'
print(re.match(pattern, string))    # <_sre.SRE_Match object; span=(0, 6), match='abaaba'>
print(re.findall(pattern, string))  # ['abaaba']

pattern = r'a[ab]+?a'
string = 'abaaba'
print(re.match(pattern, string))    # <_sre.SRE_Match object; span=(0, 6), match='aba'>
print(re.findall(pattern, string))  # ['aba', 'aba']


# Группировки символов
pattern = r'(test)*'
string = 'test'
print(re.match(pattern, string))

pattern = r'abc|(test|text)*'
string = 'abc'
print(re.match(pattern, string))

pattern = r'((abc)|(test|text)*)'
string = 'abc'
match = re.match(pattern, string)
print(match)            # <_sre.SRE_Match object; span=(0, 3), match='abc'>
print(match.groups())   # ('abc', 'abc', None)

pattern = r'((abc)|(test|text)*)'
string = 'testtext'
match = re.match(pattern, string)
print(match)            # <_sre.SRE_Match object; span=(0, 8), match='testtext'>
print(match.groups())   # ('testtext', None, 'text')

pattern = r'Hello (abc|test)'
string = 'Hello abc'
match = re.match(pattern, string)
print(match)            # <_sre.SRE_Match object; span=(0, 9), match='Hello abc'>
print(match.group(0))   # Hello abc - ноль аргумент по умолчанию
print(match.group(1))   # abc

pattern = r'(\w+)-\1'
string = 'test-test'
match = re.match(pattern, string)
print(match)

pattern = r'(\w+)-\1'
string = 'test-test chow-chow'
duplicates = re.sub(pattern, r'\1', string)
print(duplicates)

# Флаги
x = re.match(r'text', 'TEXT', re.IGNORECASE)
print(x)
