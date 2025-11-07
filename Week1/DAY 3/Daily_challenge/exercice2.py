
def affordable_items(items_purchase, wallet):

    # Remove $ and , from all prices and convert them to integers
    cleaned_items = {}
    for item, price in items_purchase.items():
        cleaned_price = int(price.replace("$", "").replace(",", ""))
        cleaned_items[item] = cleaned_price
    print(cleaned_items)

    # Clean the wallet value
    wallet_amount = int(wallet.replace("$", "").replace(",", ""))

    # Determine which items can be afforded
    basket = []

    # Go through each item in the original order (most important first)
    for item, price in cleaned_items.items():
        if wallet_amount >= price:  # If we can afford the item
            basket.append(item)
            wallet_amount -= price  # Subtract its price from the wallet
    if not basket:
        print("Nothing")
    else:
        print(sorted(basket))  # Alphabetical order

items_purchase_1 = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet_1 = "$300"
items_purchase_2 = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet_2 = "$100"
items_purchase_3 = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet_3 = "$1"

print(affordable_items(items_purchase_1,wallet_1))
print(affordable_items(items_purchase_2,wallet_2))
print(affordable_items(items_purchase_3,wallet_3))
