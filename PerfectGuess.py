import random

def perfect_guess():
    num = random.randint(1, 100)  # Generates a random number between 1 and 100
    attempts = 0  # Counter to track the number of guesses
    guessed_correctly = False

    print("Welcome, Player!")
    
    while not guessed_correctly:
        # Ask for the user's guess
        try:
            g = int(input("Take a guess between 1 and 100: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1  # Increment the number of attempts

        if g == num:
            print(f"You got it! The number was {num}.")
            print(f"It took you {attempts} guesses to find the number.")
            guessed_correctly = True  # Exit the loop
        elif g > num:
            print("Take a smaller guess.")
        else:
            print("Take a bigger guess.")

if __name__ == "__main__":
    perfect_guess()
