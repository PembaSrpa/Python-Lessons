# function to find the greatest of 3 numbers
def greatest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(greatest_of_three(10, 20, 15))

# function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(celsius_to_fahrenheit(25))

# how do you prevent a python print statement from printing a new line at the end?
print("Hello, World!", end=' ')
print("This is on the same line.")

# function to calculate sum of first n natural numbers
def sum_of_natural_numbers(n):
    return n * (n + 1) // 2
print(sum_of_natural_numbers(10))

# function to print star pattern
def star_pattern(n):
    for i in range(1, n + 1):
        print('* ' * i)
star_pattern(5)

# inches to centimeters conversion
def inches_to_centimeters(inches):
    centimeters = inches * 2.54
    return centimeters
print(inches_to_centimeters(10))

# function to remove a given word from a list and stop it at the same time
def remove_word_from_list(word_list, word_to_remove):
    while word_to_remove in word_list:
        word_list.remove(word_to_remove)
    return word_list
words = ['apple', 'banana', 'orange', 'banana', 'grape']
print(remove_word_from_list(words, 'banana'))

# function to print multiplication table of a given number
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
multiplication_table(5)

# function to calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))