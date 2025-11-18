# Find the greatest of 4 numbers entered by the user
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))
greatest = num1
if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3
if num4 > greatest:
    greatest = num4
print("The greatest number is:", greatest)

# find out whether a student has passed or failed, if it requires at least 40% total and at least 33% in each subject to pass. Assume there are 3 subjects and take marks as input from the user.
marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]
total_marks = sum(marks)
if total_marks / 3 >= 40 and all(mark >= 33 for mark in marks):
    print("The student has passed.")
else:
    print("The student has failed.")

# Detect spam comments in a blog based on certain keywords like "make money", "buy now", "click this", "subscribe this".
comment = input("Enter the blog comment: ").lower()
spam_keywords = ["make money", "buy now", "click this", "subscribe this"]
if any(keyword in comment for keyword in spam_keywords):
    print("This comment is detected as spam.")
else:
    print("This comment is not spam.")
    
#Find if a username contains less than 10 characters.
username = input("Enter a username: ")
if len(username) < 10:
    print("The username contains less than 10 characters.")
else:
    print("The username contains 10 or more characters.")
    
# Find whether a given name is present in a list of names.
names_list = ["Alice", "Bob", "Charlie", "David"]
name_to_check = input("Enter a name to check: ")
if name_to_check in names_list:
    print(f"{name_to_check} is present in the list.")
else:
    print(f"{name_to_check} is not present in the list.")

# Calculate the grade of a student based on marks obtained in 5 subjects (assume each subject is out of 100). The grading criteria are as follows:
# 90% and above: A
# 80% to 89%: B
# 70% to 79%: C
# 60% to 69%: D
# Below 60%: F
marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]
average_marks = sum(marks) / 5
if average_marks >= 90:
    grade = 'A'
elif average_marks >= 80:
    grade = 'B'
elif average_marks >= 70:
    grade = 'C'
elif average_marks >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"The student's grade is: {grade}")

