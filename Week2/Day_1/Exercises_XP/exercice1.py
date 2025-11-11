class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Misty", 3)
cat2 = Cat("Whiskers", 5)
cat3 = Cat("Felix", 2)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    # Compare the ages to find the oldest cat
    oldest_cat = cat1  # Start by assuming cat1 is the oldest
    
    if cat2.age > oldest_cat.age:
        oldest_cat = cat2
    
    if cat3.age > oldest_cat.age:
        oldest_cat = cat3
    
    return oldest_cat

# Step 3: Print the oldest cat's details
oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")
