

name = input("Enter your name:")

while True:
    # Check if the name is valid: no digits + at least 3 letters
    if not name.isdigit() and len(name) >= 3:
        print("thank you")
        break
    else:
        name = input("give the correct name:")

