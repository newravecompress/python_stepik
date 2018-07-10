import exceptions
import fib

print(exceptions.greet("Student"))

# частичный импорт
from exceptions import BadName, greet

print(BadName)

# использование алиаса:
from exceptions import BadName, greet as my_greet
import exceptions as exc
print(exc)

def greet():
    print("Greetings!")

greet()

print(my_greet("Student!"))

# Импортирование всех имен как они есть:
from exceptions import *
