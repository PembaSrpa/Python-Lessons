#store 7 fruits in a list entered by the user
fruits = []
for i in range(7):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)
print(fruits)

#accept marks of 6 students and display them in a sorted manner
marks = []
for i in range(6):
    mark = float(input(f"Enter marks for student {i+1}: "))
    marks.append(mark)
marks.sort()
print("Sorted marks:", marks)

#check that a tuple cannot be changed
my_tuple = (1, 2, 3)
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)

#sum a list with 4 numbers
numbers = []
for i in range(4):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
total = sum(numbers)
print("Sum of the numbers:", total)

#count the number of zeros in a tuple
my_tuple = (7, 0, 8, 0, 0, 9)
zero_count = my_tuple.count(0)
print("Number of zeros in the tuple:", zero_count)