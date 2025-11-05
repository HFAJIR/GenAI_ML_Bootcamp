
#🌟 Exercise 2: Cinemax #2

family = {}
total_cost = 0

n = int(input("How many family members? "))

for i in range(n):
    name = input("Enter the name: ")
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age

print(f"Family members: {family}")

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    print(f"{name.capitalize()} has to pay ${price}")
    total_cost += price

print(f"\n The total cost for the family is: ${total_cost}")