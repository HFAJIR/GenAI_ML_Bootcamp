
class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        """Retourne True si la personne a 18 ans ou plus"""
        return self.age >= 18
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []  # liste pour stocker les objets Person

    def born(self, first_name, age):
        """Ajouter un nouveau membre à la famille"""
        new_person = Person(first_name, age, self.last_name)
        self.members.append(new_person)

    def check_majority(self, first_name):
        """Vérifie si le membre est majeur"""
        found = False
        for member in self.members:
            if member.first_name == first_name:
                found = True
                if member.is_18():
                    print(f"You are over 18, your parents accept that you will go out with your friends")
                else:
                    print(f"Sorry, you are not allowed to go out with your friends.")
                break
        if not found:
            print(f"No member with the name {first_name} found.")

    def family_presentation(self):
        """Affiche le nom de la famille et les membres"""
        print(f"Family {self.last_name}:")
        for member in self.members:
            print(f"{member.first_name}, {member.age} years old")
# Créer une famille
smith_family = Family("Smith")

# Ajouter des membres
smith_family.born("Alice", 20)
smith_family.born("Bob", 16)

# Vérifier si un membre peut sortir
smith_family.check_majority("Alice")  # majeur
smith_family.check_majority("Bob")    # mineur
smith_family.check_majority("Charlie")# membre inexistant

# Présenter la famille
smith_family.family_presentation()
