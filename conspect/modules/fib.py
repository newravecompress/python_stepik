print(__name__)     # имя модуля

def fib(k):
    if k == 0 or k == 1:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)

# Если вызываем из глобального пространства имен - выполнить функцию для числа 31
# execute only if run as a script
if __name__ == "__main__":
    print(__name__)
    print(fib(31))
