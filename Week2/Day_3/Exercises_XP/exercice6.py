from datetime import datetime

def minutes_lived(birthdate_str, name):
  
    # Step 1: Convert the string to a datetime object
    birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
    
    # Step 2: Get the current date and time
    now = datetime.now()
    
    # Step 3: Calculate the time difference
    difference = now - birthdate
    
    # Step 4: Convert the difference to minutes
    minutes_lived = difference.total_seconds() / 60
    
    # Step 5: Display the result
    print(f"{name}, you have lived approximately {int(minutes_lived):,} minutes.")

birthdate_input = input("Enter your birthdate (DD/MM/YYYY): ")
name_input = input("Enter your name: ")
minutes_lived(birthdate_input, name_input)
