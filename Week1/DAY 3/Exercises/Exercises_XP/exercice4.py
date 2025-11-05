
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Using dictionary comprehension
char_to_index = {character: i for i, character in enumerate(users)}
print(char_to_index)

# 2. Using dictionary comprehension
index_to_char = {i: character for i, character in enumerate(users)}
print(index_to_char)

# 3. Using dictionary comprehension with sorted list
sorted_char_to_index = {character: i for i, character in enumerate(sorted(users))}
print(sorted_char_to_index)
