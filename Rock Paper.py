import random

print("Rock, Paper, Scissors")

# Set the possible choices
choices = ["rock", "paper", "scissors"]

# Let the player choose their move
player_choice = input("Enter your move: ").lower()

# Randomly select the computer's move
computer_choice = random.choice(choices).lower()

# Print the results
print("Player chose:", player_choice)
print("Computer chose:", computer_choice)

# Determine the winner
if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print("Player wins!")
elif player_choice == "paper" and computer_choice == "rock":
    print("Player wins!")
elif player_choice == "scissors" and computer_choice == "paper":
    print("Player wins!")
elif player_choice == "scissors" and computer_choice == "rock":
    print("Computer wins!")
elif player_choice == "rock" and computer_choice == "paper":
    print("Computer wins!")
elif player_choice == "paper" and computer_choice == "scissors":
    print("Computer wins!")

# If the player enters a move that is a combination of lower and uppercase letters, such as "pAper", the current
# version of the code will not recognize it as a valid move. This is because the lower() function will only convert
# uppercase letters to lowercase, and will not affect lowercase letters.

# To handle input that is a combination of lower and uppercase letters,
# you can use the lower() function on both the player's input and the list of possible choices, like shown above
