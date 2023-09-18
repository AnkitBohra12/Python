# import the module from package

# approach 1
import sys                      # pre-defined module of python
sys.path.append("C:/Users/abohra/PycharmProjects/pythonProject/day_9/package1")
# first we have to specify the package location
import module1
import module2

module1.display()
module2.show()

# approach 2            with the help of from keyword

from module1 import *
from module2 import *
display()
show()

