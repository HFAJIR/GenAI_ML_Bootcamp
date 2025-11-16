
import math
import turtle

class Circle:
    def __init__(self, *, radius=None, diameter=None):
  
        if radius is not None:
            self.radius = radius
            self.diameter = radius * 2
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Vous devez fournir soit radius soit diameter.")

    @property
    def area(self):
       
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        raise TypeError("On ne peut ajouter qu’un Circle avec un autre Circle.")

    # Comparaison : >
    def __gt__(self, other):
        return self.radius > other.radius

    # Egalité ==
    def __eq__(self, other):
        return self.radius == other.radius

    # Pour trier les cercles : <
    def __lt__(self, other):
        return self.radius < other.radius

# Exemples d’utilisation
c1 = Circle(radius=5)
c2 = Circle(diameter=40)
c3 = Circle(radius=90)

print(c1)          
print(c2.area)    
print(c1 + c3)     
print(c2 > c1)   
print(c1 == Circle(radius=5))  

circles = [c1, c2, c3]
print(list(sorted(circles))) 

# Visualisation avec turtle
turtle.speed(1)
turtle.color("red")
for circle in circles:
    turtle.penup()
    turtle.goto(0, -circle.radius)
    turtle.pendown()
    turtle.circle(circle.radius)
  
turtle.done()