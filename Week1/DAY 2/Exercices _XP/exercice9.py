# Ticket Price Calculator and Age Restriction Checker
# Create an empty list to store people (name + age)
people = []

# Ask how many people are in the family or group
num_people = int(input("How many people are in your group? "))

# Loop to get each person's name and age
for i in range(num_people):
    name = input(f"Enter the name of person {i + 1}: ")
    age = int(input(f"Enter the age of {name}: "))
    people.append((name, age))

# Calculate total cost
total_cost = 0
for name, age in people:
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    total_cost += ticket_price

# Display total cost
print(f"\n Total ticket cost for the group: ${total_cost}")

# Restricted movie (ages 16–21 only)
allowed_people = [(name, age) for name, age in people if 16 <= age <= 21]

# Display who can watch
print("\n🎬 People allowed to watch the restricted movie:")
if allowed_people:
    for name, age in allowed_people:
        print(f"- {name} (Age: {age})")
else:
    print(" No one is allowed to watch the restricted movie.")
