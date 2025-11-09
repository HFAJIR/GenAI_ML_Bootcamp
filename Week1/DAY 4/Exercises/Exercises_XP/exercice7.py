
import random

def get_random_temp_1():
    """Return a random float between -10 and 40 degrees Celsius."""
    return round(random.uniform(-10, 40), 1)

def main_1():
    """Main function to display temperature and provide advice."""
    temperature = get_random_temp_1()
    
    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temperature < 16:
        print("Quite chilly! Don't forget your coat.")
    elif 16 <= temperature < 23:
        print("Nice weather.")
    elif 24 <= temperature < 32:
        print("A bit warm, stay hydrated.")
    else :
        print("It's really hot! Stay cool.")
 
# Part 2: Temperature based on month

def get_random_temp_2(month=None):
    if month in [12, 1, 2]:  # Winter
        return round(random.uniform(-10, 10), 1)
    elif month in [3, 4, 5]:  # Spring
        return round(random.uniform(0, 20), 1)
    elif month in [6, 7, 8]:  # Summer
        return round(random.uniform(15, 40), 1)
    elif month in [9, 10, 11]:  # Autumn
        return round(random.uniform(5, 25), 1)
    else:
        return None  


def main_2():
    month = int(input("Enter the month number (1-12): "))
    temperature = get_random_temp_2(month)
    
    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temperature < 16:
        print("Quite chilly! Don't forget your coat.")
    elif 16 <= temperature < 23:
        print("Nice weather.")
    elif 24 <= temperature < 32:
        print("A bit warm, stay hydrated.")
    elif 32 <= temperature <= 40:
        print("It's really hot! Stay cool.")
 

main_1()
print("\n")
main_2()
