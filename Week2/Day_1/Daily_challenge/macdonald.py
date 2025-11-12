class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    # Méthode add_animal unique avec kwargs
    def add_animal(self, **kwargs): 
        for animal_type, count in kwargs.items(): 
            if animal_type in self.animals: 
                self.animals[animal_type] += count 
            else: 
                self.animals[animal_type] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_list = self.get_animal_types()
        animals_formatted = []
        for animal in animal_list:
            count = self.animals[animal]
            animals_formatted.append(animal + "s" if count > 1 else animal)

        if len(animals_formatted) > 1:
            animals_str = ", ".join(animals_formatted[:-1]) + " and " + animals_formatted[-1]
        else:
            animals_str = animals_formatted[0]

        return f"{self.name}'s farm has {animals_str}."


# Test
macdonald = Farm("McDonald")
macdonald.add_animal(cow=5, sheep=2, goat=12)
print(macdonald.get_short_info())
print(macdonald.get_info())
