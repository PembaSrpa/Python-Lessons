# write program to open these files 1.txt, 2.txt, 3.txt and if any of these files is not found, a message without exiting the program should be displayed prompting the same.
file_names = ['1.txt', '2.txt', '3.txt']
for file_name in file_names:
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Contents of {file_name}:\n{content}\n")
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.\n")

# print the 3rd, 5th and 7th element from a list of 10 elements using enumerate
elements = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
indices_to_print = [2, 4, 6]  # 3rd, 5th, and 7th elements (0-based index)
for index, element in enumerate(elements):
    if index in indices_to_print:
        print(f"Element at index {index + 1}: {element}")   

# write a list comprehension to print a list which contains the multiplication table of user input number
user_input = int(input("Enter a number to generate its multiplication table: "))
multiplication_table = [user_input * i for i in range(1, 11)]
print(f"Multiplication table of {user_input}: {multiplication_table}")

# write a program to display a/b where a and b are integers. If b is zero, display infinite by handling the ZeroDivisionError.
try:
    a = int(input("Enter numerator (a): "))
    b = int(input("Enter denominator (b): "))
    result = a / b
    print(f"The result of {a} / {b} is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is infinite.")
    
#store the multiplication tables generated in the previous program in a file named tables.txt
with open('tables.txt', 'w') as file:
    file.write(f"Multiplication table of {user_input}: {multiplication_table}")