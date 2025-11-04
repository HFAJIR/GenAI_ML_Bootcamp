# Create an empty list to store all numbers
all_numbers = []

while True:
    # Ask the user for comma-separated numbers
    user_input = input("Enter numbers separated by commas (or type 'quit' to exit): ")

    # Check if the user wants to quit
    if user_input.lower() == "quit":
        break

    # Split and clean spaces
    num_list = [num.strip() for num in user_input.split(',')]

    # Add these numbers to the main list
    all_numbers.extend(num_list)

# Create a tuple from the full list
num_tuple = tuple(all_numbers)

# Display the final results
print(all_numbers)
print(num_tuple)
