# create string variable
# ways of creating string variable
s = 'here it is'
t = str("here it is :")

# creating empty string variables
v = str()
x = ''
print(type(v))

# mutable and immutable
# mutable - cannot change the value of variable
# immutable - can change the value of variable
# string are immutable

str1 = 'welcome'
print(id(str1))  # this will return the id of the memory

str1 = str1 + 'to python'
print(str1)
print(id(str1))  # new memory allocated to the variable

# if the value is changed after updation then it is immutable

# Example 3 : + and * with string

a = 'who'
print(a + ' are')  # concatenation/joining
print(a * 2)  # string is printed 2 times

# Slicing

b = 'coming'
print(b[1:3])
print(b[:5])
print(b[2:])

print(b[1:-1])  # -1 remove the last character of the string
print(b[1:-2])  # last 2 char are removed

# ord() and chr()
print(ord('a'))  # ASCII number
print(chr(65))  # tell rhe char  represent ascii number

# max()  min()   len()

print(max('abbbcde'))  # max char of the string
print(min('abc'))  # min char of the string
print(len('abc'))  # tell the length of char

# in, not in operators -- returns true/false check the particular string is present in main string or not

si = "welcome"
print("come" in si)  # true
print("ss" in si)  # false

print("come" not in si)  # false
print("ss" not in si)  # true

# String comparison
print("time" == "tie")  # false
print("free" != "freedom")  # true
print("arrow" > "aron")  # true
print("right" >= "left")  # true
print("yellow" <= "fellow")  # false
print("abc" > "")  # true

# testing strings true/false

q = "welcome to python"
print(s.isalnum())  # false is this string contains any numbers or not

print("welcome".isalpha())  # true if  this string contains alphabets or not
print("2012".isdigit())  # TRUE if string contains some digit then it is true
print("first number".isidentifier())  # FALSE if there are any keywords are not
print(s.islower())  # TRuE if a string is contains any lower case alphabets or not
print(s.isupper())  # FALSE sees if string contain any upper case or not
print(" ".isspace())  # TRUE if string contains space or not

# Searching for substrings

w = "welcome to python"
print(w.endswith("thon"))  # returns true if the string ends with this particular string or parameter
print(w.startswith("py"))  # starting with this string gives true
print(w.find("come"))  # find the particular parameter in the main string or not and tell the position of
# the string
print(w.count("0"))  # returns number of occurrences of substring in the string

# Converting sting

o = "string in PYTHON"
o1 = o.capitalize()  # String in python convert starting alpha into uppercase
print(o1)

o2 = o.title()  # String In Python convert every starting word in uppercase
print(o2)

o3 = o.lower()  # string in python convert all the string into lowecase
print(o3)

o4 = o.swapcase()
print(o4)  # sTRING IN python convert or swap all the uppercase into lower and lower into uppercase

o5 = o.upper()
print(o5)   # convert whole string into uppercase

o6 = o.replace("in", "on")  # instead of in it will replace it with on update into new string
print(o6)


# Reverse a string
# method 1

e = "welcome"
rev_str = ""
for i in e:
    rev_str = i+rev_str
print("reverse string is :", rev_str)

# method 2  by slicing

j = "welcome"
rev_stri = j[::-1]  # j[start:end:-1]
print(rev_stri)     # j[0:7:-1]
