
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        # Calcul de la "force" de chaque chien
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            winner = self.name
        elif self_power < other_power:
            winner = other_dog.name
        else:
            winner = "It's a tie"

        return f"The winner is: {winner}"
dog1 = Dog("Rex", 5, 20)      # nom, âge, poids
dog2 = Dog("Buddy", 3, 15)
dog3 = Dog("Max", 4, 25)

# Test du bark
print(dog1.bark())   
print(dog2.bark())   
# Test du run_speed
print(dog1.run_speed())  
print(dog3.run_speed())

# Test du fight
print(dog1.fight(dog2))  
print(dog3.fight(dog1))  

