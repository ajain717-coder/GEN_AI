# 1. Create a list of products
products = ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse", "Monitor"]

# 2. Create a tuple for a sample product
sample_product = ("Laptop", 55000, "Electronics")

# 3. Print 2nd and last product
print("2nd product:", products[1])
print("Last product:", products[-1])

# 4. Append two new products
products.append("Printer")
products.append("Webcam")
print("Updated products list:", products)

# Extra (optional): Convert tuple to list, update price, convert back
temp = list(sample_product)
temp[1] = 52000
sample_product = tuple(temp)
print("Updated sample product:", sample_product)