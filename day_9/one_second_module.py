# approach 1
import one_module
import second_module

obj = one_module.Animal()
obj.display()

obj1 = second_module.Bird()
obj1.display()

# approach 2
from one_module import Animal
from second_module import Bird

obj1 = Animal()
obj1.display()

obj2 = Bird()
obj2.display()

