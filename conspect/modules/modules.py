import conversation         # import the whole module conversation
conversation.say_hello()    # invoke function with prefix 'conversation'

from conversation import say_hello  # import part of module
say_hello()                         # invoke without prefix

import calculator.simple.simple_calc
calculator.simple.simple_calc.compute()     # have to write whole path

from calculator import simple
simple.simple_calc.compute()

from calculator.simple.simple_calc import compute
compute()

from conversation import *     # take all
say_hello()

from conversation import say_hello as hello
hello()
