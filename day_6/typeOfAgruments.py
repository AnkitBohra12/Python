# 1 - positional arguments and keyword argumnets

def func(i, j):
    print(i, j)


func(10, 20)  # positional arguments
func(i=20, j=10)  # keyword arguments


# example 2 - we can assign default values to the positional arguments

def func(i, j=10):
    print(i, j)


func(100,200)       # default value of j will be replaced by 200
func(100)           # here default value of j will consider so it will print 100 and 10


# Example 3 - keyword argumnets

def greetings(name, greetmsg):
    print(greetmsg + "   " + name)


greetings(name = "john", greetmsg = "Hello")        # if we jumbal keywords if will assign in same place


# Example 4 - combination of positional and keyword parameters

def my_func(a,b,c):
    print(a,b,c)


my_func(10,20,30)       # positional arguments
my_func(a= 10, b= 20, c= 30)     # keyword arguments
my_func(b=20 , a= 10, c= 30)     # keyword arguments

my_func(10,20, c= 30)       # combination of positional and keyword arguments
# my_func(10, b = 20, c)         # this is wrong as positional argument must appear before any keyword argument


# Example 5 - how function can return the mutiple values

def largest(a, b):
    if a > b:
        return a, b
    else:
        return b, a


print(largest(100,20))



