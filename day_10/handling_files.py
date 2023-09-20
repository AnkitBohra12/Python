# Example 1:- write the data

file = open("C:\demo\myfile.txt", 'w')
file.write("This is my first statement...\n")
file.write("This is my second statement...\n")
file.write("This is my third statement...\n")
file.write("This is my fourth statement...\n")
file.write("This is my fifth statement...\n")
file.close()
print("program completed")

# Example 2 :- reading data from text file

file = open("C:\demo\myfile.txt", 'r')
#print(file.read())
print(file.readline())
file.close()

# Example 3 :- append the new lines in the text file

file = open("C:\demo\myfile.txt", 'a')
file.write("this is my sixth statement...\n")
file.write("this is my seventh statement...")
file.close()
print("program is completed")

