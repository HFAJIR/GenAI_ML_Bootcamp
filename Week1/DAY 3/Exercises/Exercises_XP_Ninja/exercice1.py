
manufacturers_str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
manufacturers_list = manufacturers_str.split(", ")
print(f"There are {len(manufacturers_list)} manufacturers in the list.")
manufacturers_list.sort(reverse=True)
#  Print the list in descending (Z-A) order
print("Manufacturers in reverse order (Z-A):")
manufacturers_reverse = sorted(manufacturers_list, reverse=True)
for manufacturer in manufacturers_reverse:
    print(manufacturer)

# Find out how many manufacturers’ names have the letter ‘o’ in them.
count_o = sum(1 for manufacturer in manufacturers_list if 'o' in manufacturer.lower())
print(f"There are {count_o} manufacturers with the letter 'o' in their name.")

# Find out how many manufacturers’ names do not have the letter ‘i’ in them.
count_i = sum(1 for manufacturer in manufacturers_list if 'i' != manufacturer.lower())
print(f"There are {count_i} manufacturers without the letter 'i' in their name.")

# Bonus: Remove duplicates
manufacturers_unique = list(set(manufacturers_list))
print(f"Companies without duplicates: {', '.join(manufacturers_unique)}")
print(f"There are {len(manufacturers_unique)} unique manufacturers.")

# Bonus: Print manufacturers in ascending order (A-Z) with reversed names
manufacturers_reversed = [manufacturer[::-1] for manufacturer in manufacturers_unique]
manufacturers_reversed.sort()
print(f"Manufacturers in ascending order (A-Z) with reversed names: {', '.join(manufacturers_reversed)}") 
