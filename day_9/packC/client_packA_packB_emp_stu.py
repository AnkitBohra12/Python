import sys
sys.path.append("C:/Users/abohra/PycharmProjects/pythonProject/day_9/packA")
sys.path.append("C:/Users/abohra/PycharmProjects/pythonProject/day_9/packB")

# Approach 1
#import emp
#empobj = emp.Employee(100,"john", 100000)
#empobj.displayemp()

#import stu
#stuobj = stu.Student(100, "scott", 42)
#stuobj.displaystu()

# Approach 2

from emp import *
empobj = Employee(101,"john",50000)
empobj.displayemp()
#from stu import Student
