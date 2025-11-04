
# Ask the user for 7 words and store them in a list
words = []
print("Please enter 7 words:")
for i in range(7):
    word = input(f"Word {i+1}: ")
    words.append(word)

# Ask user for a single character
letter  = input("Enter a single character to search for: ")

# Loop through the words and find the letter

print(f"\nSearch results for the letter '{letter}':")
print("=" * 35)

for i, word in enumerate(words):
    if letter in word:
        index = word.index(letter)
        print(f"Word {i+1}: '{word}' - '{letter}' found at position {index}")
    else:
        print(f"Word {i+1}: '{word}' - '{letter}' not found in this word")