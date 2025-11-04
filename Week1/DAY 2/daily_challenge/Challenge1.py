
# Ask user for inputs
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))
# Generate multiplication table
for i in range(1, length + 1):
    result = number * i
    print(f"{number} x {i} = {result}")
    