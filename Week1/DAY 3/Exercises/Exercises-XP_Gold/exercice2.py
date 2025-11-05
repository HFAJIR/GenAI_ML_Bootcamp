#🌟 Exercise 3 : Birthday Dictionary
# Create a dictionary with birthdays
birthdays = {
    "Hamza": "1990/05/15",
    "Amine": "1985/08/25",
    "Khalid": "1992/12/30",
    "Anas": "1988/03/10",
    "Anwar": "1995/07/22"
}
# Welcome message
print("Welcome! You can look up the birthdays of the people in the list!")
# Print all names in the dictionary
print("Here are the people in the list:")
for person in birthdays.keys():
    print(f"- {person}")
# Ask the user for a name
name = input("Please enter a person's name: ")
# Get the birthday
birthday = birthdays.get(name)
# Print the birthday
if birthday:
    print(f"{name}'s birthday is on {birthday}.")
else:
    print(f"Sorry, I don't have information on {name}'s birthday.")
