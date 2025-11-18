import random

# List of possible words
wordslist = [
    'correction', 'childish', 'beach', 'python', 'assertive',
    'interference', 'complete', 'share', 'credit card', 'rush', 'south'
]

# Choose a random word
word = random.choice(wordslist).lower()

# Create the initial display: * for each letter, but keep spaces
display = ['*' if char != ' ' else ' ' for char in word]

# To store the letters already guessed
guessed_letters = set()

# The 6 hangman body parts
hangman_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg"]
mistakes = 0

print("Welcome to the Hangman Game!")
print("Word to guess:", ''.join(display))

while mistakes < 6 and '*' in display:
    guess = input("\nGuess a letter: ").lower()

    # Check if the user entered ONE single letter
    if len(guess) != 1 or not guess.isalpha():
        print(" You must enter ONE single letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print(" You already used this letter:", guess)
        continue

    guessed_letters.add(guess)

    # Check if the letter is in the word
    if guess in word:
        print(" Good guess!")
        for i, char in enumerate(word):
            if char == guess:
                display[i] = guess
    else:
        print(" Wrong guess!")
        print(" Adding:", hangman_parts[mistakes])
        mistakes += 1

    print("Word:", ''.join(display))
    print("Guessed letters:", ', '.join(sorted(guessed_letters)))
    print("Mistakes:", mistakes, "/ 6")

# End of the game
if '*' not in display:
    print("\n Congratulations! You found the word:", word)
else:
    print("\n You lost! The word was:", word)
    print("Better luck next time!")