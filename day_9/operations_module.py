# how to call the function form one module to another module
# approach 1
import calculator_module

calculator_module.add(100, 200)
calculator_module.mul(10, 20)

# approach 2
from calculator_module import add, mul

add(100, 200)
mul(10, 20)

# approach 3
from calculator_module import *
add(100, 200)
mul(10, 20)
