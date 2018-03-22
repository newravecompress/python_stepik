from Person import Person

me = Person('Derek', 'Jensen', 30)

print(me.first)
print(me.last)
print(me.age)
me.greet()

print(me.foo)
print(Person.foo)
Person.wave()
print(Person.say_foo())
