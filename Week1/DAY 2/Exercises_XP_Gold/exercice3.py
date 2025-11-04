# Check the index

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Ask user for their name
user_name = input("Enter your name: ").lower()

# Create a lowercase version of the list for comparison
lower_names = [name.lower() for name in names]

# Check if the lowercase user input exists in the lowercase list
if user_name in lower_names:
    index = lower_names.index(user_name)
    print(f"Your name '{names[index]}' is found at index: {index}")
else:
    print("Your name is not found in the list.")
