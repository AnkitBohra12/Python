# 1 - creating a dictionary
mydic = {101: "x", 102: "y", 103: "z"}      # accepts all kinds of data
print(mydic)


# 2 - access the item in a dictionary
# using key
mydic = {
    "brand" : "Hyudai",
    "model" : "i10",
    "year" : 2021
}
print(mydic["brand"])        # key works as an index here
print(mydic["model"])

# by using get() function
mydic = {
    "brand" : "Hyudai",
    "model" : "i10",
    "year" : 2021
}
x = mydic.get("year")
print(x)
print(mydic.get("model"))


# 3 - how can we change the values in a dictionary
mydic = {
    "brand" : "Hyudai",
    "model" : "i10",
    "year" : 2021
}
mydic["year"] = 2022
print(mydic)

# 4 - reading items from dictionary using loop
mydic = {
    "brand" : "Hyudai",
    "model" : "i10",
    "year" : 2021
}
for i in mydic:
    print(i)        # this will print only keys from dic

for i in mydic:
    print(mydic[i])     # this will only print values / here we're getting index

for i in mydic.values():      # this will only print values / here we're getting direct values
    print(i)

for x, y in mydic.items():       # this will print key:value both by using items() function
    print(x, y)

# 5 - check key exist in dictionary or not
mydic = {
    "brand" : "Hyudai",
    "model" : "i10",
    "year" : 2021
}
if "model" in mydic:
    print("exist")
else:
    print("not exist")

print("model" in mydic)         # simple check without if statement

# 6 - find number of items in dictionary
mydic = {
    "brand" : "Hyudai",
    "model" : "i10",
    "year" : 2021
}
print(len(mydic))

# 7 - adding items to dictionary
mydic = {
    "brand" : "Hyudai",
    "model" : "i10",
    "year" : 2021
}
mydic["color"] = "red"          # added new item in dic
print(mydic)


# 8 - remove the item from dictionary
mydic = {
    "brand" : "Hyudai",
    "model" : "i10",
    "year" : 2021
}
# by using pop() function
mydic.pop("year")
print(mydic)

# by del keyword
del mydic["brand"]
print(mydic)

#del mydic           # completely delete the dic this will get he name error
#print(mydic)

mydic.clear()           # clear all elements in from the dic
print(mydic)            # {}


# 9 - copy one dic to another
mydic = {
    "brand" : "Hyudai",
    "model" : "i10",
    "year" : 2021
}
# without using copy function
mydic1 = mydic
print(mydic1)

# using copy() function
a = mydic1.copy()
print(a)

