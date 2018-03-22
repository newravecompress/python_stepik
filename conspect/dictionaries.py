# dictionaries

d = {'a': 239, 10: 100}  # dictionary, or associated array

print(d['a'])
print(d[10])

# in, not in - just like in another

d['John'] = 25      # добавляем значение
d.keys()            # returns an object with keys
list(d.keys())      # now returns a list of keys
d.values()          # returns an object of values
list(d.values())    # ... list of values

'Derek' in d        # False

d['Mike']       # if there is not a key, then will be an error
d.get('Mike')   # in this case there will not be an error, it returns None
del d['Mike']

# словари изменяемы
# элементы не имеют порядка
# все ключи различны
# ключи неизменяемы

new_ages = dict(Derek=30, Katie=29, Brian=5)    # function to create a dictionary

# перебор элементов
d = {'C': 14, 'A': 12, 'T': 9, 'G': 18}

for key in d:
    print(key, end=' ')  # G C A T

for key in d.keys():
    print(key, end=' ')  # G C A T

for value in d.values():
    print(value, end=' ')  # 18, 14, 12, 9

for key, value in d.items():
    print(key, value, end='; ')  # G 18; C 14; A 12; T 9;

list = [1, 3, 4, 5, 6, 7]
for idx, val in list:
    print(idx, val)     # TypeError: 'int' object is not iterable

for idx, val in enumerate(list):    # make a dictionary from a list
    print(idx, val)

