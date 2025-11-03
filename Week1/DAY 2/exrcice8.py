
# Initialize an empty list to store the toppings
toppings = []
# Ask the user for their favorite pizza toppings until they type 'quit'
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    if topping.lower() == 'quit':   # Stop the loop if the user types 'quit'
        break
     # Add the topping to the list
    toppings.append(topping)
    print(f"{topping} has been added to your pizza toppings.")

# After the loop ends, calculate the total price
base_price = 10  # Base price for the pizza
topping_price = 2.5  # Price per topping
total_price = base_price + (len(toppings) * topping_price)
print("\nYour pizza toppings are:")
for t in toppings:
    print("-", t)
print(f"Your total pizza price is: ${total_price:.2f}")