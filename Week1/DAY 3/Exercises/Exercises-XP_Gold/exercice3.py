# Create a dictionary with birthdays
birthdays = {
    "Hamza": "1990/05/15",
    "Amine": "1985/08/25",
    "Khalid": "1992/12/30",
    "Anas": "1988/03/10",
    "Anwar": "1995/07/22"
}

print("Welcome! You can look up or add birthdays of people!")

# --- Ajouter de nouveaux anniversaires ---
while True:
    new_name = input("Enter a person's name to add (or type 'quit' to finish): ").capitalize()
    if new_name in birthdays:
        print(f"{new_name} is already in the list with birthday on {birthdays[new_name]}.\n")
        continue
    if new_name.lower() == "quit":
        break
    new_birthday = input(f"Enter {new_name}'s birthday (YYYY/MM/DD): ")
    birthdays[new_name] = new_birthday
    print(f"{new_name}'s birthday has been added!\n")

# --- Afficher la liste mise à jour ---
print("\nHere are the people in the list:")
for person in birthdays.keys():
    print(f"- {person}")

# --- Rechercher un anniversaire ---
name = input("\nPlease enter a person's name to look up: ").capitalize()
birthday = birthdays.get(name)

if birthday:
    print(f"{name}'s birthday is on {birthday}.")
else:
    print(f"Sorry, I don't have information on {name}'s birthday.")
