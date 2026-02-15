# Task 3: Product Pricing

# 1. Create price dictionary
price_dict = {
    "Laptop": 55000,
    "Mobile": 25000,
    "Headphones": 2000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 12000
}

# 2a. Add a new product
price_dict["Printer"] = 9000

# 2b. Update price of an existing product
price_dict["Mobile"] = 24000

# 2c. Remove a product by name
product_to_remove = "Tablet"
if product_to_remove in price_dict:
    del price_dict[product_to_remove]
else:
    print(product_to_remove, "not found in price list")

# 3. Print average price
total_price = 0
count = 0

for price in price_dict.values():
    total_price += price
    count += 1

average_price = total_price / count
print("Average price:", average_price)

# Extra (optional): Max and Min priced products
max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("Highest priced product:", max_product, price_dict[max_product])
print("Lowest priced product:", min_product, price_dict[min_product])
