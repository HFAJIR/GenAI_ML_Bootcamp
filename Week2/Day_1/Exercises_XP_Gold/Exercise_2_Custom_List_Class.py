# Exercise 2 : Custom List Class

import random

class MyList:
    def __init__(self, letters):
        self.letters = letters
    # Add a method that returns the reversed list.
    def reverse_list(self):
        return self.letters[::-1]
    # Add a method that returns the sorted list.
    def sort_list(self):
        return sorted(self.letters)
    # Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).
    def generate_random_list(self):
        return [random.randint(0, 100) for _ in range(len(self.letters))]
    
# Example of usage
mylist = MyList(['b', 'a', 'd', 'c', 'e'])
print("Original list:", mylist.letters)
print("Reversed list:", mylist.reverse_list())
print("Sorted list:", mylist.sort_list())
print("Random list:", mylist.generate_random_list())
