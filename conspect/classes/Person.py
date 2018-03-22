class Person:

    foo = 'bar'

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def greet(self):
        print('Hello there!')

    @staticmethod
    def wave():         # no need to pass the self
        print('*Waving hands feverishly*')
        # print(foo)      # staticmethod doesn't have access to the class attribute

    @classmethod
    def say_foo(cls):   # need to pass the link to a class
        return cls.foo  # classmethod have access to the class attribute

