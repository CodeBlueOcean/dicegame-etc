# Needed to create random numbers to simulate dice roll
import random

# Initialise player scores to 0  
high_score = 0

# Modifying global variables in local scope
def dice_game():
    global high_score

# Repeat everything in this block 10 times 
    while True:
        dice1_value = random.randint(1,6)
        dice2_value = random.randint(1,6)
        total = dice1_value + dice2_value
# Display the initial values
        print("Current High Score:", high_score)
        print("1)   Roll Dice")
        print("2)   Leave Game")
        choice = input("Enter your choice: ")
# Selection:
        if choice == "1":
                print("\nYou roll a...", dice1_value,"\n")
                print("You roll a...", dice2_value,"\n")
                print("You have rolled a total of:", total,"\n")
        if total > high_score:
                print("New high score!\n")
                high_score = total
        elif choice == "2":
            print("Maybe next time!")
            break
        else:
                print("Incorrect selection! You must select '1' or '2'.\n")
dice_game()
