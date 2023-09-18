# 1 - create a function / define a function / creation or declaration
def myfun():  # declaration of function
    print("hello")


myfun()  # calling the function


# 2 - we can give parameter to the function
def myfun(name):
    print("hello", name)


myfun("Ankit")  # calling function by using single parameter


# 3 - multiple parameter / function take arg and return value 
def myfun(a, b):
    return a + b


sum = myfun(10, 20)
print(sum)
print(myfun(200, 100))


# 4 - different type of function does not take arguments not return any value (none)
def myfun():
    return


print(myfun())

def myfun():
    i = 10


print(myfun())



