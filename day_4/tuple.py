# 1 - creating tuple
my_tuple = ("a", "b", "c")
print(my_tuple)
my_tuple = ()      # empty tuple

# 2 - access tuple items
my_tuple1 = ("a", "b", "c")
print(my_tuple1[1])
print(my_tuple1[-1])

# 3 - range of indexes
my_tuple2 = ("a", "b", "c", "d", "e")
print(my_tuple2[2:4])
print(my_tuple2[-4:-1])

# 4- changing the tuple values   / can't modify existing values/ can't append new value/ can't insert new value/
# can't remove a value it doesn't allow you to change value cuz its immutable but there is a workaround /
# indirect way/ we can change the tuple into the list type obj then modify list and then convert into tuple

mytuple = ("a", "b", "c", "d", "e")
mylist = list(mytuple)
mylist[0] = "x"

mytuple = tuple(mylist)   # tuple function to convert list into tuple
print(mytuple)

# 5 - reading tuple items using loop
tple = ("a", "b", "c", "d", "e")
for i in tple:
    print(i)

# 6 - check if the item exist into the tuple
ple = ("a", "b", "c", "d", "e")
if "b" in ple:
    print("yes b is there in the tuple")
else:
    print("no there is not any b exist in the tuple")

# 7 - tuple length = counting items in a tuple
le = ("a", "b", "c", "d", "e")
print(len(le))

# 8 - copying one tuple items into another
e = ("a", "b", "c", "d", "e")
f = e
print(f)

# 9 - combining the two tuples
tu = ("a", "b", "c", "d", "e")
tu1 = ("f", "g")
tu2 = tu+tu1
print(tu2)

# 10 - checking if two tuples are equal or not
tu = ("a", "b", "c", "d", "e")
tu1 = (1, 2)
if tu == tu1:
    print("they are equal")
else:
    print("not equal")
