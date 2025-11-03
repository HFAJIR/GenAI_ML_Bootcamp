
# Initial list
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# 1. Remove "Banana" from the list
basket.remove("Banana")
print("Basket after removing Banana:", basket)
# 2. Remove "Blueberries" from the list
basket.remove("Blueberries")
print("Basket after removing Blueberries:", basket)
# 3. Add "Kiwi" to the end of the list
basket.append("Kiwi")
print("Basket after adding Kiwi:", basket)  
# 4. Add "Apples" to the beginning of the list
basket.insert(0, "Apples")
print("Basket after adding Apples at the beginning:", basket)
# 5. Count how many times "Apples" is in the list
apple_count = basket.count("Apples")
print("Number of times 'Apples' appears in the list:", apple_count)
# 6. Clear the entire list
basket.clear()
print("Final state of the basket:", basket)

