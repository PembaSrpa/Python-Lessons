# # create two virtual environments install few packages in first one. How do you create similar environment in second one?
# # To create two virtual environments and install packages in the first one, you can follow these steps:
# # 1. Create the first virtual environment
# python -m venv env1
# # 2. Activate the first virtual environment
# # On Windows
# env1\Scripts\activate
# # On macOS/Linux
# source env1/bin/activate
# # 3. Install packages in the first virtual environment
# pip install package1 package2 package3
# # 4. Freeze the installed packages to a requirements file
# pip freeze > requirements.txt
# # 5. Deactivate the first virtual environment
# deactivate
# # 6. Create the second virtual environment
# python -m venv env2
# # 7. Activate the second virtual environment
# # On Windows
# env2\Scripts\activate
# # On macOS/Linux
# source env2/bin/activate
# # 8. Install the packages from the requirements file into the second virtual environment
# pip install -r requirements.txt
# # 9. Deactivate the second virtual environment when done
# deactivate

#wap to input name, marks and phone number of student and format it to print.
name = input("Enter student's name: ")
marks = input("Enter student's marks: ")
phone_number = input("Enter student's phone number: ")
formatted_output = "Student Name: {}\nMarks: {}\nPhone Number: {}".format(name, marks, phone_number)
print(formatted_output)

# a list contains the multiplication table of 2. wap to convert it to a vertical string of same numbers.
multiplication_table_2 = [2 * i for i in range(1, 11)]
vertical_string = '\n'.join(str(num) for num in multiplication_table_2)
print(vertical_string)

# wap to filter a list of numbers which are divisible by 3 and 5 using lambda function.
numbers = [10, 15, 22, 30, 45, 60, 73, 90]
divisible_by_3_and_5 = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
print(divisible_by_3_and_5)

#wap to find the maximum number from a list using reduce function.
from functools import reduce
max_number = reduce(lambda a, b: a if a > b else b, numbers)
print(max_number)

# explore the flask module and create a web server using flask and python.
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the Flask Web Server!"
if __name__ == '__main__':
    app.run(debug=True)
    