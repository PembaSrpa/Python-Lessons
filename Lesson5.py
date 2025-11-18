#create a dictionary to store student names and their grades
students_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eva": 88
}
print("Dictionary:", students_grades)

#input 8 numbers from the user and display all the unique numbers
user_numbers = []
for i in range(8):
    number = int(input(f"Enter number {i+1}: "))
    user_numbers.append(number)
unique_numbers = set(user_numbers)
print("Unique numbers:", unique_numbers)

#Create an empty dictionary and allow 4 friends to enter their favorite colors and store them in the dictionary. Use the friend's name as the key and the color as the value. Finally, display the dictionary. Assume that the names are unique.
favorite_colors = {}
for i in range(4):
    name = input(f"Enter the name of friend {i+1}: ")
    color = input(f"Enter {name}'s favorite color: ")
    favorite_colors[name] = color
print("Favorite colors dictionary:", favorite_colors)

# What if 2 friends have the same name?
# In this case, we can store a list of colors for each name.
favorite_colors_duplicate_names = {}
for i in range(4):
    name = input(f"Enter the name of friend {i+1}: ")
    color = input(f"Enter {name}'s favorite color: ")
    if name in favorite_colors_duplicate_names:
        favorite_colors_duplicate_names[name].append(color)
    else:
        favorite_colors_duplicate_names[name] = [color]
print("Favorite colors dictionary (handles duplicate names):", favorite_colors_duplicate_names)

# What if 2 friends have the same favorite color?
# In this case, we can store a list of names for each color.
favorite_colors_duplicate_colors = {}
for i in range(4):
    name = input(f"Enter the name of friend {i+1}: ")
    color = input(f"Enter {name}'s favorite color: ")
    if color in favorite_colors_duplicate_colors:
        favorite_colors_duplicate_colors[color].append(name)
    else:
        favorite_colors_duplicate_colors[color] = [name]
print("Favorite colors dictionary (handles duplicate colors):", favorite_colors_duplicate_colors)

#change the values inside the list in set s={8, 7, 12, "Ram", [4, 5, 6]}
s = {8, 7, 12, "Ram", (4, 5, 6)}  # Changed list to tuple to make it hashable
print("Set before modification:", s)
# To modify the tuple, we need to remove it and add a new one
s.remove((4, 5, 6))
s.add((10, 11, 12))  # New tuple with modified values
print("Set after modification:", s)