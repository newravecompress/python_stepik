def sweet(x):
    return (x * 2) ** 2

print(list(map(sweet, range(5))))

print(list(map(lambda x: (x * 2) ** 2, range(5))))


