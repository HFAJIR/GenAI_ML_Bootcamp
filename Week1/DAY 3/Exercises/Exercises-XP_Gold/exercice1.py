


# Create a dictionary with birthdays
birthdays = {
    "Hamza": "1990/05/15",
    "amine": "1985/08/25",
    "khalid": "1992/12/30",
    "anas": "1988/03/10",
    "anwar": "1995/07/22"
}

# Welcome message
print("Welcome! You can look up the birthdays of the people in the list!")
# Ask the user for a name
name = input("Please enter a person's name: ")
# Get the birthday
birthday = birthdays.get(name)
# Print the birthday
if birthday:
    print(f"{name}'s birthday is on {birthday}.")
else:
    print(f"Sorry, I don't have information on {name}'s birthday.")
