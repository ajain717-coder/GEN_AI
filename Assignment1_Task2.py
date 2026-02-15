# Parallel categories list
categories = [
    "Electronics",
    "Electronics",
    "Accessories",
    "Accessories",
    "Accessories",
    "Electronics"
]

# 1. Create a set of categories
categories_set = set(categories)
print("Categories set:", categories_set)

# 2. Add a new category (duplicate ignored)
categories_set.add("Electronics")
categories_set.add("Office")
print("After adding categories:", categories_set)

# 3. Check if a category exists
check_category = "Office"
print("Is 'Office' in set?", check_category in categories_set)

# Extra (optional): Total unique categories
print("Total unique categories:", len(categories_set))
