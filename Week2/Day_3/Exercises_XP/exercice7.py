
from faker import Faker

# Step 1: Create an empty list to store users
users = []

# Initialize a Faker instance
faker = Faker()

def add_users(number_of_users):
    for _ in range(number_of_users):
        # Create a dictionary for each user
        user = {
            "name": faker.name(),
            "address": faker.address(),
            "language_code": faker.language_code()
        }
        # Append the user dictionary to the users list
        users.append(user)

add_users(5)

# Print the list of users
for i, user in enumerate(users, start=1):
    print(f"User {i}:")
    print(user)
    print("-" * 40)
