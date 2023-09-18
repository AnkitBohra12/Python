# 1 - creating set

myset = {"apple", "banana", "orange"}
print(myset)  # it not print the data into same order that's y we called it as unordered

# 2 - accessing items/values from set / we can access through loop
myset = {"apple", "banana", "orange"}
for i in myset:
    print(i)

# 3 - value exist in set or not
myset = {"apple", "banana", "orange"}  # banana is present in the set or not
print("banana" in myset)

# 4 - adding new item in a set
# add() - we can add only single item at a time        update() - for multiple items in a time
myset = {"apple", "banana", "orange"}
myset.add("cherry")
print(myset)

myset = {"apple", "banana", "orange"}
myset.update(["mango", "grapes"])  # its a list inside update function
print(myset)

# 5 - find number of item in a set by len function
myset = {"apple", "banana", "orange"}
print(len(myset))

# 6 - how to remove the item from the set
# remove() function     discard()
myset = {"apple", "banana", "orange"}
myset.remove("apple")  # if try to remove unlisted value from the set it will throw error "key error"
print(myset)

myset = {"apple", "banana", "orange"}
myset.discard("banana")
print(myset)  # discard will not give any error if we try to print unlisted value form the set

# 7 - clear all items form set
myset = {"apple", "banana", "orange"}
myset.clear()
print(myset)  # this will return empty set  / it will just clear the set values

# del myset         # for deleting the set which will throw an error
# print(myset)


# 8 - joining two sets
# here union is a function which will help us to joint two sets
myset = {"apple", "banana", "orange"}
myset1 = {"a", "b", "o"}
myset2 = myset.union(myset1)
print(myset2)

# using  update() function we can join two sets
myset = {"apple", "banana", "orange"}
myset1 = {"a", "b", "o"}
myset.update(myset1)
print(myset)
