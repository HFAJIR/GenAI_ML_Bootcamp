
import random

# Initialize counters
wins = 0
losses = 0
rounds = 0

while True:
    # Ask user for a number
    user_input = input("Guess a number between 1 and 9 (or type 'quit' to exit): ")

    # Check if the user wants to quit
    if user_input.lower() == "quit":
        print("Game over!")
        break
     # Validate input
    if not user_input.isdigit() or not (1 <= int(user_input) <= 9):
        print("Please enter a valid number between 1 and 9.")
        continue    

    user_number = int(user_input)
    # Generate random number for the computer
    computer_number = random.randint(1, 9)
    rounds += 1

    if user_number == computer_number:
        wins += 1
        print(f"Congratulations! You guessed it right. The number was {computer_number}.")
    else:
        losses += 1
        print(f"Sorry, the correct number was {computer_number}. Better luck next time!")

    print(f"Rounds played: {rounds}, Wins: {wins}, Losses: {losses}\n")

print(f"Good answer is {computer_number}")
