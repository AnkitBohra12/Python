# HOW TO ACCESS SAME FUNCTION IN TWO MODULES
# approach 1
import animal
import bird

animal.fly()
animal.color()

bird.fly()
bird.color()

# approach 2                # solution is to import the module and then call the function
from animal import *
fly()
color()

from bird import*           # latest import will be invoked

fly()
color()

