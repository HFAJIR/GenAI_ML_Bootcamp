# Exercise 1 : Geometry
import math
from math import pi

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius  

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

    def definition(self):
        print(f"Un cercle de rayon {self.radius} est l'ensemble des points situés à égale distance d'un point central.")

# Exemple d'utilisation
c1 = Circle()          # rayon par défaut 1.0
print("Périmètre :", c1.perimeter())
print("Aire :", c1.area())
c1.definition()

c2 = Circle(3)         # changer le rayon à 3
print("\nPérimètre :", c2.perimeter())
print("Aire :", c2.area())
c2.definition()
