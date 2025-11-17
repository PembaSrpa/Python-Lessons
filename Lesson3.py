import datetime
#greet the user
def greet_user(name):
    print(f"Hello, {name}! Good Afternoon.")
input_name = input("Please enter your name: ")
greet_user(input_name)

#fill the letter template with name and date: letter = Dear <name>,\nYou are selected!\nDate: <date>
def fill(name, date):
    letter = f"Dear {name},\nYou are selected!\nDate: {date}"
    return letter
user_name = input("Enter the recipient's name: ")
letter = fill(user_name, datetime.date.today())
print("\nGenerated Letter:\n",letter)

#detect double spaces in a string
def detect_double_spaces(text):
    if "  " in text:
        print("Double spaces detected.")
    else:
        print("No double spaces detected.")
sample_text = input("Enter a string to check for double spaces: ")
detect_double_spaces(sample_text)

#replace double spaces with single spaces
def replace_double_spaces(text):
    while "  " in text:
        text = text.replace("  ", " ")
    return text
corrected_text = replace_double_spaces(sample_text)
print("Corrected Text:", corrected_text)