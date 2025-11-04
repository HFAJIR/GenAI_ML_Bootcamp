

# Ask the user for a word
word = input("Enter a word: ")

# Create an empty string to store the new word
new_word = ""

# Loop through each character in the word
for i in range(len(word)):
    # Add the first letter or any letter that is different from the previous one
    if i == 0 or word[i] != word[i - 1]:
        new_word += word[i]

# Display the result
print(new_word)
