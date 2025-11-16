

import string
import random


all_letters = string.ascii_letters
random_string = ''.join(random.choice(all_letters) for _ in range(5))
x = list(random_string)

print(all_letters)
print("Liste des caractères:", x)