squared = []
for n in range(11):
    squared.append(n ** 2)

print(squared)

char_count = {'a': 5, 'b': 7, 'A': 5, 't': 8, 'B': 10}

char_frequency = dict()
for key, value in char_count.items():
    if key.lower() in char_frequency:
        char_frequency[key.lower()] += value
    else:
        char_frequency[key.lower()] = value

print(char_frequency)


# list comprehensions
squared = [n ** 2 for n in range(11)]
print(squared)

squared = [n ** 2 for n in range(11) if n % 2 is 0]     # additional statement
print(squared)

z = [(x, y) for x in range(3) for y in range(3) if y >= x]
print(z)

z = ((x, y) for x in range(3) for y in range(3) if y >= x)  # В круглых скобках будет генератор
print(z)
print(next(z))
print(next(z))

# dictionary comprehensions
char_frequency = {
    key.lower(): char_count.get(key.lower(), 0) + char_count.get(key.upper(), 0)
    for key in char_count.keys()
}
print(char_frequency)

