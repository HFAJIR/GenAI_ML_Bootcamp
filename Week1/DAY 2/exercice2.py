# Exercise 2: Modifying a Tuple by Converting to a List
my_tuple = (1, 2, 3, 4)
print("Original tuple:", my_tuple)
# Convert the tuple to a list to modify it
my_list = list(my_tuple)
my_list.extend([5, 6])
# Convert the list back to a tuple
my_tuple = tuple(my_list)
print("Modified tuple:", my_tuple)


# We can do it in another way
my_tuple = (1, 2, 3, 4)
new_tuple = my_tuple + (5, 6)
print("New tuple (after adding numbers):", new_tuple)