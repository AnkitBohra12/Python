# 1 - how to create a list

mylist = [1, 2, 3, 4, 5, 6]  # which contains multiple values
mylist1 = ["one", "two", "three"]
mylist2 = ["one", 1]
mylist3 = list()  # empty list

print(mylist)

# 2 - how to access  the item from the list

ist = ['one', 'two', 'three']  # index start from the 0
print(ist[1])
print(ist[-1])  # returns the last value from the list

#  3 - range of indexes

o = ["m", 'n', "o", "p", "q"]
print(o[2:4])
print(o[-4:-1])

# 4 - change the item value

p = ["m", 'n', "o", "p", "q"]
print(p)
p[0] = "a"  # replaced with a (changing value in the list by index number)
print(p)

# 5 - read the list items using loop statement

q = ["r", "t", "p", "m"]
for i in q:
    print(i)

# 6 - check if the item is existed in the list or not

y = ["apple", "banana", "grape", "orange"]
if "apple" in y:
    print("yes item is present")
else:
    print("not present")

# 7 - list length (counting number of items in a list)

u = ["apple", "banana", "grape", "orange"]
print(len(u))  # length function (len)

# 8 - add new item in the list
# two functions are available append() and insert()

z = ["apple", "banana", "grape", "orange", "cherry"]
z.insert(3, "owo")  # insert a value in the middle or some particular position in the list
print(z)

# 9 - remove item for the list
# functions are there pop()
b = ["apple", "banana", "grape", "orange"]
b.pop(1)
print(b)

# delete the item form the list by del keyword
t = ["apple", "banana", "grape", "orange"]
del t[3]
print(t)

# by using clear() function
w = ["apple", "banana", "grape", "orange"]
w.clear()  # it will clear the all items / will print empty list variable will be available
print(w)

# 10 - copy one list to another
# list() function
few = ["apple", "banana", "grape", "orange"]
few2 = list(few)  # both the list are having same values
print(few2)

# copy() function
ow = ["apple", "banana", "grape", "orange"]
ow1 = ow.copy()  # another value
print(ow1)

# 11- how to combine/ join the two list
# using + operator
wo = ["a", "b", "c"]
wo1 = [1, 2, 3]
wo2 = wo+wo1            # concatenation
print(wo2)

# using looping statement
wow = ["a", "b", "c"]
wow1 = [1, 2, 3]
for i in wow1:
    wow.append(i)
print(wow)

# using extend function
wo = ["a", "b", "c"]
wo1 = [1, 2, 3]
wo.extend(wo1)
print(wo)
