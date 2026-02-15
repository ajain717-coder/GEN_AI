prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount = float(input("Enter discount percentage: "))

total_items = 0
total_discounted_price = 0

with open("discount_report.txt", "w") as f:

    f.write("Product | Original Price | Discounted Price\n")

    for product in prices:
        original = prices[product]
        discounted = original - (original * discount / 100)

        f.write(product + " | " +
                str(original) + " | " +
                str(round(discounted, 2)) + "\n")

        total_items += 1
        total_discounted_price += discounted

    average_price = total_discounted_price / total_items

    f.write("\n")
    f.write("Total Items: " + str(total_items) + "\n")
    f.write("Average Discounted Price: " + str(round(average_price, 2)) + "\n")


with open("discount_report.txt", "r") as f:
    print(f.read())
