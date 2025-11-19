import math

# multiplication table using for loop

for i in range(1, 11):
    print(f"Multiplication Table for {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Print a blank line after each table  

# greet all the names in the list using for loop

names = ["Alice", "Bob", "Charlie", "Diana"]
for name in names:
    print(f"Hello, {name}!")
    
# multiplication table using while loop

num = 1
while num <= 10:
    print(f"Multiplication Table for {num}:")
    multiplier = 1
    while multiplier <= 10:
        print(f"{num} x {multiplier} = {num * multiplier}")
        multiplier += 1
    print()  # Print a blank line after each table
    num += 1

# prime or not

n = int(input("Enter a number to check if it's prime: "))

if n < 2:
    print(f"{n} is not a prime number.")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            break
    else:
        print(f"{n} is a prime number.")

# find the sum of first n natural numbers using while loop

n = int(input("Enter a positive integer to sum up to: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(f"Sum of the first {n} natural numbers is {total}.")

# factorial using for loop

n = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}.")

# star pattern
for i in range(1, 6):
    print("*" * i)

# multiplication table of n(input) in reversed order using for loop

n = int(input("Enter a number to display its multiplication table in reversed order: "))
print(f"Multiplication Table for {n} in reversed order:")
for j in range(10, 0, -1):
    print(f"{n} x {j} = {n * j}")