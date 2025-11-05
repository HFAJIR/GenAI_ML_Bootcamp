
#🌟 Exercise 2 : Advanced Data Manipulation and Analysis

sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

#Total Sales Calculation:
total_sales = {}
for sale in sales_data:
    product = sale["product"]
    revenue = sale["price"] * sale["quantity"]
    if product in total_sales:
        total_sales[product] += revenue
    else:
        total_sales[product] = revenue

print("Total Sales per Product:", total_sales)

#Customer Spending Profile:

customer_spending = {}
for sale in sales_data:
    customer_id = sale["customer_id"]
    amount_spent = sale["price"] * sale["quantity"]
    if customer_id in customer_spending:
        customer_spending[customer_id] += amount_spent
    else:
        customer_spending[customer_id] = amount_spent
print("Customer Spending Profile:", customer_spending)

#Sales Data Enhancement:

for sale in sales_data:
    sale["total_price"] = sale["price"] * sale["quantity"]
print("Enhanced Sales Data:", sales_data)

#High-Value Transactions:

high_value_transactions = sorted(
    [sale for sale in sales_data if sale["total_price"] > 500],
    key=lambda x: x["total_price"],
    reverse=True
)
print("High-Value Transactions:", high_value_transactions)

#Customer Loyalty Identification:
purchase_count = {}

for sale in sales_data:
    customer = sale["customer_id"]
    purchase_count[customer] = purchase_count.get(customer, 0) + 1

loyal_customers = [cust for cust, count in purchase_count.items() if count > 1]

print("\n🤝 Loyal Customers (more than one purchase):", loyal_customers)

#Bonus: Insights and Analysis:

#Calculate the average transaction value for each product category.

average_transaction_value = {}
transaction_counts = {}

for sale in sales_data:
    product = sale["product"]
    total = sale["total_price"]
    average_transaction_value[product] = average_transaction_value.get(product, 0) + total
    print(average_transaction_value)
    transaction_counts[product] = transaction_counts.get(product, 0) + 1
    print(transaction_counts)

for product in average_transaction_value:
    average_transaction_value[product] = round(average_transaction_value[product] / transaction_counts[product], 2)

print("\n Average Transaction Value per Product:")
for p, avg in average_transaction_value.items():
    print(f" - {p}: ${avg}")

# Most popular product (based on quantity sold)
product_quantity = {}
for sale in sales_data:
    product = sale["product"]
    quantity = sale["quantity"]
    product_quantity[product] = product_quantity.get(product, 0) + quantity

most_popular_product = max(product_quantity, key=product_quantity.get)

print(f"\n Most Popular Product: {most_popular_product} (Total Quantity Sold: {product_quantity[most_popular_product]})")
#Provide insights into how these analyses could inform the company’s marketing strategies.
print("\n Marketing Insights:")
print(" - Focus marketing efforts on loyal customers to increase retention.")
print(" - Promote high-value products to maximize revenue.")
print(" - Utilize customer spending profiles to tailor marketing campaigns.")

git commit -m "Completed Exercise 2: Advanced Data Manipulation and Analysis"
git push origin main