# Ask the user for their favorite fruits
favorite_fruits = input("Please enter your favorite fruits (separated by spaces): ")

# Convert the input string into a list
fruits_list = favorite_fruits.split()
print("Your favorite fruits are:", fruits_list)

# Ask for another fruit
new_fruit = input("Enter the name of any fruit: ")

# Check if the fruit is in the list
if new_fruit in fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")