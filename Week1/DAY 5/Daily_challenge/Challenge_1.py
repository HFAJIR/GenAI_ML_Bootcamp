
#Challenge 1: Sorting Words Alphabetically
user_input = input("Enter words separated by commas: ")
words_list = user_input.split(',') # Split input string into a list
print("Original list:", words_list)
words_list.sort() # Sort the list alphabetically
print("Sorted list:", words_list)
sorted_string = ','.join(words_list) # Join the sorted list back into a string
print(sorted_string)

