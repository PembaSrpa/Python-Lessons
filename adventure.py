# Adventure Game: Dragon's Realm
import random
from time import sleep

def animate_flower():
    """Prints a flower line by line to create an animation effect."""
    print("\n   ... A magical flower grows for you! ...\n")
    
    flower_art = [
        "      (@) ",
        "   ( .   . )",
        "  (   (O)   )",
        "   ( .   . )",
        "      | |",
        "    _ | | _",
        "   / \| |/ \\",
        "  /   | |   \\",
        "      | |    ",
        "     /   \\   "
    ]
    
    # This loop handles the animation
    for line in flower_art:
        print("    " + line)
        sleep(0.3) # This pause creates the animation effect
    print("\n")

def display_intro(name):
    print()
    print("-" * 40)
    print(f"Hello {name}, welcome to the Dragon's Realm!")
    print("-" * 40)
    print("You are in a land full of dragons. In front of you,")
    print("you see two caves. In one cave, the dragon is friendly")
    print("and will share his treasure with you. The other dragon")
    print("is greedy and hungry, and will eat you on sight.")
    print()

def start_game():
    input("Press enter to start the game")
    name = input("Enter your name: ")
    
    play_again = "yes"
    
    while play_again == "yes" or play_again == "y":
        display_intro(name)
        
        # 1. Choose a cave
        cave = ""
        while cave != "1" and cave != "2":
            cave = input("Which cave will you go into? (1 or 2): ")

        # 2. The Suspense
        print("\nYou approach the cave...")
        sleep(2)
        print("It is dark and spooky...")
        sleep(2)
        print("A large dragon jumps out in front of you! He opens his jaws and...\n")
        sleep(2)

        # 3. The Result
        friendly_cave = random.randint(1, 2)

        if cave == str(friendly_cave):
            print(f"Gives you his treasure, {name}!")
            # CALL THE FLOWER ANIMATION HERE
            animate_flower()
        else:
            print("Gobbles you down in one bite!")
            print("         ______")
            print("        / x  x \\")
            print("        |  --  |")
            print("         \\____/")

        # 4. Play again logic
        print("Do you want to play again? (yes or no)")
        play_again = input().lower()

    print("Thanks for playing!")

# Run the game
start_game()