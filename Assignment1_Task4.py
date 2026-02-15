# Task 4: Combined Operations

products = ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse", "Monitor"]

categories = [
    "Electronics",
    "Electronics",
    "Accessories",
    "Accessories",
    "Accessories",
    "Electronics"
]
price_dict = {
    "Laptop": 55000,
    "Mobile": 25000,
    "Headphones": 2000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 12000
}
# 1. Create catalog (list of tuples)
catalog = []

for i in range(len(products)):
    product_name = products[i]
    price = price_dict.get(product_name, 0)
    category = categories[i]
    catalog.append((product_name, price, category))

print("Catalog:", catalog)

# 2. Create category_to_products dictionary
category_to_products = {}

for item in catalog:
    category = item[2]
    product_name = item[0]

    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product_name)

print("Category to Products:", category_to_products)

# 3. Print products from category with maximum products
max_count = 0
max_category = ""

for category in category_to_products:
    if len(category_to_products[category]) > max_count:
        max_count = len(category_to_products[category])
        max_category = category

print("Category with maximum products:", max_category)
print("Products:", category_to_products[max_category])