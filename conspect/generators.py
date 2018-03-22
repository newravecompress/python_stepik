def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibon(100))

def fibon_g(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(fibon_g(100))

for x in fibon_g(100):
    print(x)
