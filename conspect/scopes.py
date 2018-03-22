# области видимости
ok_status = True
vowels = ['a', 'u', 'i', 'e', 'o', 'y']

def check(word):
    global ok_status
    for vowel in vowels:
        if vowel in word:
            return True
    ok_status = False
    return False

print(check('ababab'))  # True
print(ok_status)        # True
print(check('www'))     # False
print(ok_status)        # False


# если обернуть весь этот код:
def f():
    ok_status = True
    vowels = ['a', 'u', 'i', 'e', 'o', 'y']

    def check(word):
        global ok_status
        for vowel in vowels:
            if vowel in word:
                return True
        ok_status = False
        return False

    print(check('ababab'))  # True
    print(ok_status)        # True
    print(check('www'))     # False
    print(ok_status)        # True - ok_status is not global

f()
print(ok_status)    # False - global ok_status

# решение - использовать ключевое слово nonlocal
def f():
    ok_status = True
    vowels = ['a', 'u', 'i', 'e', 'o', 'y']

    def check(word):
        nonlocal ok_status      # nonlocal - ближайшее пространство до global
        for vowel in vowels:
            if vowel in word:
                return True
        ok_status = False
        return False

    print(check('ababab'))  # True
    print(ok_status)        # True
    print(check('www'))     # False
    print(ok_status)        # False

f()
print(ok_status)    # NameError

