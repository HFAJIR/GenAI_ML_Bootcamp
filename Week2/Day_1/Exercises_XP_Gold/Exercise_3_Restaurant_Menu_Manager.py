# Exercise 3 : Restaurant Menu Manager

class MenuManager:
    def __init__(self):
        # Initialisation du menu avec les plats existants
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    # Ajouter un nouveau plat
    def add_item(self, name, price, spice, gluten):
        self.menu.append({"name": name, "price": price, "spice": spice, "gluten": gluten})
        print(f"{name} a été ajouté au menu.")

    # Mettre à jour un plat existant
    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                print(f"{name} a été mis à jour.")
                return
        print(f"Le plat '{name}' n'est pas dans le menu.")

    # Supprimer un plat
    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                self.menu.remove(dish)
                print(f"{name} a été supprimé du menu.")
                print("Menu mis à jour :", self.menu)
                return
        print(f"Le plat '{name}' n'est pas dans le menu.")


# Exemple d'utilisation
if __name__ == "__main__":
    manager = MenuManager()
    
    # Afficher le menu initial
    print("Menu initial :", manager.menu)

    # Ajouter un plat
    manager.add_item("Pizza", 20, "A", True)

    # Mettre à jour un plat
    manager.update_item("Salad", 19, "B", False)

    # Supprimer un plat
    manager.remove_item("Hamburger")
