# 1 - global variable and local variable
global_var = 20  # global crated outside the function


def func():
    local_var = 10  # created insided the function
    print(local_var)
    print(global_var)  # global variable can be access inside the function


func()

# print(local_var)        # not able to access cuz the local_var within the function


# 2
xy = 100


def cool():
    xy = 200
    print(xy)  # will print local variable


print(xy)  # printing global variable

cool()

# 3 - Using global variable in local variable and update value
xy = 100


def cool():
    global xy
    xy = 200
    print(xy)  # will print local variable


cool()
print(xy)

# 4 -
x = 100


def copy():
    global x
    x = 500
    print(x)


# copy()
print(x)  # will get the old value 100 cuz the function is not called


# 5 - we can create out the function and inside the function but we have to use global keyword

def co():
    global x
    x = 100
    print(x)


co()
