
"""Instructions
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Using the dictionary above, each key-value pair represents an item and its price - print all the items and their prices in a sentence.
Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
write some code to calculate how much it would cost to buy everything in stock.
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}
"""
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
for item, price in items.items():
    print(f"The price of {item} is ${price}")

print("\n---\n")
    
items = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

# Calculate the total cost to buy everything in stock
list_items = list(item["price"] * item["stock"] for item in items.values())
print(list_items)
total_cost = sum(list_items)
print(f"The total cost to buy everything in stock is ${total_cost}")

print("\n---\n")