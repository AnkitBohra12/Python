num1 = input("Enter first number :")  #input is the function in which we can take input from the user
num2 = input("Enter second number:") # Datatypw will be string
print(type(num1))  #type is the function to check the datatype of a variable

#    Type conversion
#approach 1 converting the datatype
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

print(type(num2))
print(num1+num2)

#approach 2 converting the datatype into print statement
num1 = input("Enter first number :")
num2 = input("Enter second number :")
print(int(num1)+int(num2))