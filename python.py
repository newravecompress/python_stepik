# else и finally:
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Division by zero')
    else:
        print('result is', result)
    finally:
        print('Finally')

divide(2, 1)
divide(2, 0)
divide(2, [])
