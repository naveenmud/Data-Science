# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

print("The robot chose " + computer_choice)

# Run Conditionals
if computer_choice == "r" and user_choice == "r":
    print("It's a tie!")
elif computer_choice == "p" and user_choice == "p":
    print("It's a tie!")
elif computer_choice == "s" and user_choice == "s":
    print("It's a tie!")
elif computer_choice == "r" and user_choice == "s":
    print("You lose!")   
elif computer_choice == "r" and user_choice == "p":
    print("You Win!")
elif computer_choice == "s" and user_choice == "p":
    print("You Lose")
else:
    print("You Win!")