
# Create a string of all the letters in the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Define vowels
vowels = "aeiou"

print("Alphabet Classification:")
print("-" * 25)
for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")
print("-" * 25)