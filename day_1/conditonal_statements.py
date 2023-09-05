#conditional statements
#if  if..else   elif

# Example 1 :- the person is eligible for vote or not

age = 23
if age >= 18:
    print("person is eligible for vote")
else:
    print("not eligible for vote")

#Example 2:-

if True:
    print("true condition")
else:
    print("false condition")


#Example 3:-

if 1:
    print("true")
else:
    print("false")

#Example 4:- find number is even or odd

a = 10
if a%2==0:
    print("even")
else:
    print("odd")

#Example 5:- if else in single line (ternary operator)

num=10
print("even") if num % 2 == 0 else print("odd")

#Example 6:- if lese- multiple statement in single line (ternary operator)

b = 2
{print("hello"), print("python")} if b>=10 else {print("hi"), print("java")}

#Example 7:- for the mutiple conditons we can use elif

weekno = 7
if weekno==1:
    print("monday")
elif weekno==2:
    print("tuesday")
elif weekno==3:
    print("wednesday")
elif weekno==4:
    print("thusday")
elif weekno==5:
    print("friday")
elif weekno==6:
    print("saturday")
elif weekno==7:
    print("sunday")
else:
    print("invalid weekno")






