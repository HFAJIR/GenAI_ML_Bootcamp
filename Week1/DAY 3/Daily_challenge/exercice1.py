# This program takes a word as input and creates a dictionary

letter_indices = {}

while True:    # 1. User Input:
    word = input("Please enter a word (or type 'quit' to exit): ")
    if word == "quit":
        print("Exiting the program.")
        break
    # Iterate through each character with its index
    print(word)
    for index, letter in enumerate(word):
        # If the letter already exists as a key, append the new index
        if letter in letter_indices:
            letter_indices[letter].append(index)
        else:
            letter_indices[letter] = [index]
    print(letter_indices)
    letter_indices.clear()  # Clear the dictionary for the next input