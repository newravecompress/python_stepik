# множества

s = set()       # пустое множество
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   # orange, banana, pear, apple - дубли удалены, порядок изменен
'orange' in basket      # True
'python' in basket      # False


element = 'fruit'
s.add(element)      # добавление
s.remove(element)   # удаление, если нет - будет ошибка
s.discard(element)  # удаление, если нет - ошибки не возникнет
s.clear()           # очистка множества
# for in - так же как и со всеми
