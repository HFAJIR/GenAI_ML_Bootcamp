while True:
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

    try_again = input("Do you want to try again? (yes/no): ").lower()
    if try_again != "yes":
        print("Goodbye!")
        break
