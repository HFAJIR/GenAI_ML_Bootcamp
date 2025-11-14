
from exercice2 import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        # Appel du constructeur de la classe parente Dog
        super().__init__(name, age, weight)
        self.trained = False  # par défaut, le chien n'est pas encore entraîné

    def train(self):
        # Fait aboyer le chien et le rend entraîné
        print(self.bark())
        self.trained = True

    def play(self, *args):
        # Affiche tous les noms des chiens qui jouent ensemble
        all_names = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(all_names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet!")

dog1 = PetDog("Fido", 2, 10)
dog2 = PetDog("Buddy", 3, 15)
dog3 = PetDog("Max", 4, 20)

# Tester train()
dog1.train()  # Fido aboit et devient entraîné

# Tester play(*args)
dog1.play(dog2, dog3)  # Affiche "Fido, Buddy, Max all play together"

# Tester do_a_trick()
dog1.do_a_trick()  # Affiche un trick aléatoire car Fido est entraîné
dog2.do_a_trick()  # Affiche "Buddy is not trained yet!" car pas encore entraîné
