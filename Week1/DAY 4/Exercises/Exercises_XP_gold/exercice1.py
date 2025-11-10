from datetime import datetime

def get_age(year: int, month: int, day: int):
    """Return age in years."""
    today = datetime.now() # Get the current date and time
    birth_date = datetime(year, month, day) # Create a datetime object for the birth date

    age = today.year - year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1 # Subtract 1 if birthday hasn't occurred yet this year
    return age


def can_retire(gender, date_of_birth):
    """Determine retirement eligibility with real current date."""
    try:
        year, month, day = map(int, date_of_birth.split('/')) # Split and convert to integers
    except ValueError:
        print("Invalid date format. Please use 'yyyy/mm/dd'.")
        return False
    
    age = get_age(year, month, day)

    retirement_age_men = 67
    retirement_age_women = 62

    if gender == 'm':
        return age >= retirement_age_men  #True if age is greater than or equal to
    elif gender == 'f':
        return age >= retirement_age_women #
    else:
        print("Invalid gender. Please use 'm' or 'f'.")
        return False


# -------- Main program --------
gender = input("Enter your gender (m/f): ").lower().strip()
date_of_birth = input("Enter your date of birth (yyyy/mm/dd): ").strip()

if can_retire(gender, date_of_birth):
    print(" You are eligible for retirement.")
else:
    print(" You are not eligible for retirement yet.")
