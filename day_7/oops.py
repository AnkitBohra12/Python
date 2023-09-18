# 1 - how to create a class

class myClass:
    def myfunc(self):  # function created inside the class called method by default every method takes one
        # argument called self cuz it belong to that particular class
        pass  # pass = none

    def display(self, name):
        print(name)


m1 = myClass()  # actual object / create obj / static
m1.myfunc()  # access class from obj / calling methods
m1.display("john")  # instance method means through object


# Example 2 :-

class myClass:
    def m1(self):  # instance method we can invoke through object only
        print("this is instance method...")

    @staticmethod  # annotation  / this method is used as a static method these method are common
    # method along multiple objects
    def m2(self, number):  # static method we can invoke directly by the class itself
        print(self, number)


# self parameter is work differently in instance and static method
# in instance the self keyword refer to the class
# but here in static it will take it as an argument


mc = myClass()
mc.m1()
mc.m2(10, 20)  # we shouldn't call a static method through an object it not a standard process cuz static method
# we can invoke directly from the class name itself
myClass.m2(30, 40)  # invoking through the class name (static method)


# Example 3 :- class variables

class MyClass:
    a, b = 10, 20  # class variable / created inside the class

    def add(self):
        print(self.a + self.b)  # if i want to access the class variable inside the method we have to use self
        # keyword

    def mul(self):
        print(self.a * self.b)


mc = MyClass()
mc.add()
mc.mul()

# Example 4 :- combination of class variable, global and local variable

i, j = 15, 25  # global variable


class myClass:
    a, b = 10, 20  # class variable

    def add(self, x, y):  # local variable (x,y)
        print(x + y)
        print(self.a + self.b)  # a, b are class variable
        print(i + j)  # i,j are global variable


mc = myClass()
mc.add(100, 200)  # accessing local variable or method by class

# Example 5 :- using all the variables as same name

a, b = 15, 25


class myClass:
    a, b = 10, 20

    def add(self, a, b):
        print(a + b)
        print(self.a + self.b)
        print(globals()['a'] + globals()['b'])  # accessing same name global variable by using global func


mc = myClass()
mc.add(40, 50)


# Example 6 :- how to create multiple objects for one single class

class myClass:
    def display(self, name):
        print("this is display method...")
        print(name)


# two different objects

obj1 = myClass()
obj1.display("john")

obj2 = myClass()
obj2.display("scott")


# Example 7 :- Create a constructor / how to use a constructor

class mylass:
    def __int__(self):
        print("this is constructor..")

    def rm(self):
        print("this is method..")


m = mylass()  # should invoke automatically
m.rm()


# Example 8 :- constructor with arguments

class myclass:
    name = "john"

    def __init__(self, name):       # constructor expecting one argument
        print(name)
        print(self.name)        # all the class variable we can access through self keyword


#mc = myClass("david")           # passing parameters to the constructor


# Example :- Req = constructor: eid, ename, sal   # display(): print eid, ename

class emp:
    def __int__(self,eid, ename, sal):
        self.eid = eid               # class variable
        self.ename= ename
        self.sal = sal                 # converting local into class variable
    def display(self):
        print(self.eid,self.ename, self.sal)
    def __str__(self):              #string type of data only
        return(self.ename)


e1 = emp(101, "john", 2400)
e1.display()


