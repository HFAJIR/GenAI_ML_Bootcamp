# 1. Create a set with my favorite numbers
my_fav_numbers = {5, 6, 11, 25, 7, 3}
# 2. Add two more favorite numbers to the set
my_fav_numbers.add(9)
my_fav_numbers.add(15)
# 3. Print the set of favorite numbers
print("My favorite numbers are:", my_fav_numbers)
# 4. Remove one favorite number from the set
my_fav_numbers.remove(3)
# 5. Print the set after removal
print("My favorite numbers after removal are:", my_fav_numbers)
# 6. Create another set with a friend's favorite numbers and combine both sets
friend_fav_numbers = {2, 4, 8, 10, 12}  
print("My friend's favorite numbers are:", friend_fav_numbers)
# Combine both sets
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# 7. Print the combined set of favorite numbers
print("Our favorite numbers are:", our_fav_numbers)