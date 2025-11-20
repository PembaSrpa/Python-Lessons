import os
import random

#read the text from a given file 'poems.txt' and find out whether the word 'twinkle' is present in the text or not.
with open('poems.txt', 'r') as file:
    content = file.read()
    if 'twinkle' in content:
        print("The word 'twinkle' is present in the file.")
    else:
        print("The word 'twinkle' is not present in the file.")

#the game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hiscore.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the hi-score whenever game() breaks the hi-score.
def game():
    """
    Simple number-guessing game. Returns an integer score (higher is better).
    You have 5 attempts to guess a number between 1 and 20.
    Scoring: correct on attempt 1 => 100, attempt 2 => 85, attempt 3 => 70, attempt 4 => 55, attempt 5 => 40.
    Failing to guess returns 0.
    """
    number = random.randint(1, 20)
    max_attempts = 5
    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts} — guess the number (1-20): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if guess == number:
            print("Correct!")
            score = max(0, 100 - (attempt - 1) * 15)
            return score
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")
    print(f"Out of attempts. The number was {number}.")
    return 0

#the game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hiscore.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the hi-score whenever game() breaks the hi-score.
hiscore_file = 'Hiscore.txt'

# read previous hi-score
if os.path.exists(hiscore_file):
    with open(hiscore_file, 'r') as f:
        data = f.read().strip()
    try:
        hi_score = int(data) if data else 0
    except ValueError:
        hi_score = 0
else:
    hi_score = 0

# play and get score
score = game()

# update if beaten
if score > hi_score:
    with open(hiscore_file, 'w') as f:
        f.write(str(score))
    print(f"New high score: {score}")
else:
    print(f"Score: {score}. High score remains: {hi_score}")
    
#Wap to generate multiplication table from 2-20 and write them to a file named 'multiplication_table.txt'.
with open('multiplication_table.txt', 'w') as f:
    for i in range(2, 21):
        f.write(f"Multiplication Table for {i}:\n")
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i * j}\n")
        f.write("\n")  # Add a newline for better readability between tables

#a file contains a word "Donkey" multiple times. You need to replace this word with "#######" and save it to the same file.
with open('donkey.txt', 'r') as file:
    content = file.read()
    content = content.replace('Donkey', '#######')
with open('donkey.txt', 'w') as file:
    file.write(content)
print("Replaced 'Donkey' with '#######' in donkey.txt")

#Wap to make a copy of a text file "poems.txt"
with open('poems.txt', 'r') as source:
    content = source.read()
with open('poems_copy.txt', 'w') as destination:
    destination.write(content)
print("Copy of poems.txt created as poems_copy.txt")

#wap to find out whether file is identical and matches the content of another file
with open('poems.txt', 'r') as file:
    content = file.read()
with open('poems_copy.txt', 'r') as file2:
    content2 = file2.read()

if content == content2:
    print("poems.txt and poems_copy.txt are identical.")
else:
    print("poems.txt and poems_copy.txt differ.")

#wipe out the contents of a file using python
with open('file_to_wipe.txt', 'w') as file:
    file.write('')
print("Contents of 'file_to_wipe.txt' have been wiped out.")

#wap to rename a file
src = 'rename.txt'
dst = 'renamed.txt'
if os.path.exists(src):
    os.rename(src, dst)
    print(f"Renamed '{src}' to '{dst}'.")
else:
    print(f"Source file '{src}' does not exist.")
