# Example 1:-

print("this is starting point of program")
print("this is starting point of program")
print("this is starting point of program")
try:
    print(x)  # when user try to input some wrong infomation/ it will occur whenever will provide some invalid input
except:
    print("Exception occured")

print("this is end of the program")
print("this is end of the program")
print("this is end of the program")

# Example 2 :-
print("this is starting point of the program...")
print(" program in progress")
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Exception occurred..... handled.....")
print("program completed")

# Example 3:- Multiple except blocks - try, except else, finally

try:
    num1, num2 = 10, 0
    result = num1 / num2
    print("result is :", result)
except ZeroDivisionError:                              # these 3 blocks are exception then these block are execute
    print("thrown ZeroDivisionError exception")
except SyntaxError:
    print("thrown syntax-error exception")
except:
    print("exception handled....")
else:                                                   # executes only exception not occurred
    print("No exception are occurred....")
finally:                                                # always execute
    print("always execute")


# Example 4 :- raising our own exceptions

def enternum(num):
    if num<0:
        raise ValueError("only integers are allowed")
    if num%2==0:
        print("even")
    else:
        print("odd")


print("checking number is even or odd by calling function")
num = -1
try:
    enternum(num)
except ValueError:
    print("value error exception occurred and handled...")
print("program completed")