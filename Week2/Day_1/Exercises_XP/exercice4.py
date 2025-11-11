
# Step 1: Define the Zoo Class
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    
    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)
                print(f"Added {animal} to {self.name}")
            else:
                print(f"{animal} is already in the zoo!")
    
    def get_animals(self):
        if not self.animals:
            print(f"{self.name} has no animals yet.")
        else:
            print(f"Animals in {self.name}: {', '.join(self.animals)}")
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"Sold {animal_sold} from {self.name}")
        else:
            print(f"{animal_sold} is not in {self.name}")
    
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        groups = {}
        
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)
        
        return groups
    
    def get_groups(self):
        groups = self.sort_animals()
        if not groups:
            print("No animals to group.")
            return
        
        print("Animal groups:")
        for letter, animal_list in groups.items():
            print(f"{letter}: {animal_list}")

# Step 2: Create a Zoo Object
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Call the Zoo Methods
print("=== Adding Animals ===")
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.add_animal("Zebra")
brooklyn_safari.add_animal("Lion")

print("\n=== All Animals ===")
brooklyn_safari.get_animals()

print("\n=== Selling an Animal ===")
brooklyn_safari.sell_animal("Bear")

print("\n=== Animals After Sale ===")
brooklyn_safari.get_animals()

print("\n=== Animal Groups ===")
brooklyn_safari.get_groups()

# Bonus: Testing the *args functionality
print("\n=== Bonus: Adding Multiple Animals ===")
brooklyn_safari.add_animal("Elephant", "Eagle", "Antelope")
brooklyn_safari.get_animals()

print("\n=== Updated Animal Groups ===")
brooklyn_safari.get_groups()