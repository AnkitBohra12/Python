# Example 2:- importing modules from 2 different packages

# Approach 1
import sys
sys.path.append("C:/Users/abohra/PycharmProjects/pythonProject/day_9/pack1")        # path of pack1
sys.path.append("C:/Users/abohra/PycharmProjects/pythonProject/day_9/pack1/pack2")   # in the path we have to specify
# pack2

import module1
import module2

module1.display()
module2.show()


# Approach 2

import sys
sys.path.append("C:/Users/abohra/PycharmProjects/pythonProject/day_9/pack1")        # path of pack1
sys.path.append("C:/Users/abohra/PycharmProjects/pythonProject/day_9/pack1/pack2")  # path of pack2

from module1 import *
from module2 import*

display()
show()

