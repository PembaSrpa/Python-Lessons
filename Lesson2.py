#add two numbers
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
print("The sum of {} and {} is {}".format(a, b, a + b))

#find a remainder when a number is divided by 2
c = float(input("Enter a number to divide by 2: "))
remainder = c % 2
print("The remainder when {} is divided by 2 is {}".format(c, remainder))

#check the type of variable
d = (input("Enter a variable to check the type of: "))
#input is always string
print("The type of the variable {} is : {}".format(d,type(d)))

#check which is greater using comparison operator
e = 34
f = 80
if e > f:
    print("Between {} and {}, {} is greater".format(e, f, e))
else:
    print("Between {} and {}, {} is greater".format(e, f, f))
    
#find the average
g = float(input("Enter a number: "))
h = float(input("Enter another number: "))
avg = (g + h) / 2
print("The average of {} and {} is {}".format(g, h, avg))

#calculate square of a number
i = float(input("Enter a number: "))
sq = i ** 2
print("The square of {} is {}".format(i, sq))