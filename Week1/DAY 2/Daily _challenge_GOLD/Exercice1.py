from datetime import datetime

# Ask the user for their birthdate
birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")

# Convert the string to a real date
birthdate = datetime.strptime(birthdate_str,"%d/%m/%Y")

# Get today's date
today = datetime.now()

# Calculate age
age = today.year - birthdate.year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

# Get the last digit of the age (number of candles)
candles = age % 10
candles_str = "i" * candles

# Check if the user was born in a leap year
year = birthdate.year
is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

# Print the birthday cake
print(f"      ___{candles_str}___")
print("      |:H:a:p:p:y:|")
print("    __|___________|__")
print("   |^^^^^^^^^^^^^^^^^|")
print("   |:B:i:r:t:h:d:a:y:|")
print("   |                 |")
print("   ~~~~~~~~~~~~~~~~~~~\n")

# Bonus: print a second cake if born in a leap year
if is_leap:
    print(f"       ___{candles_str}___")
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~\n")