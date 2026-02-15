products = []

for i in range(3):
    name = input("Enter product name: ")
    price = input("Enter price: ")
    products.append((name, price))

with open("products.txt", "w") as f:
    for p in products:
        f.write(p[0] + " | " + p[1] + "\n")

with open("products.txt", "r") as f:
    for line in f:
        print(line.strip())