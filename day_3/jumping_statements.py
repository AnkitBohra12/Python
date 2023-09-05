# break and continue

# break
for i in range(1,10):
    if i == 5:
        break
    print(i)

print("program exited")

# continue for multiple condition we can use (or)
for i in range(1, 10):
    if i == 3 or i == 5 or i == 7:
        continue
    print(i)

print("program exited")

for i in range(3, 7, 2):
    if i == 5:
        break
    print(i)

