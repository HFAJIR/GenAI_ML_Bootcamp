
import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        # Initialiser la liste d'items
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0
        # Calcul du nombre total de pages
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # Navigation
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page {page_num} out of range. Total pages: {self.total_pages}")
        self.current_idx = page_num - 1
        return self  # pour le method chaining

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # Affichage personnalisé
    def __str__(self):
        return "\n".join(self.get_visible_items())
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

# Test ValueError
try:
    p.go_to_page(10)
except ValueError as e:
    print(e)
# Page 10 out of range. Total pages: 7

try:
    p.go_to_page(0)
except ValueError as e:
    print(e)
# Page 0 out of range. Total pages: 7

# Bonus: method chaining
print(p.first_page().next_page().next_page().next_page().get_visible_items())

# Affichage personnalisé
print(p)
