GREETING = "Hello, "
_GREETING = "Hello, "   # Скрытие имени при импортировании через *

class BadName(Exception):
    pass

def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name + " is inappropriate name")

print('Is executable!')

# Указание имен, импортируемых через *
__all__ = ["BadName", "greet"]
