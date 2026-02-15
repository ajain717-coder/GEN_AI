# Task 3: User Menu

orders = []

while True:
    print("\nMenu:")
    print("1 - Add order amount")
    print("2 - Show all orders and final totals")
    print("q - Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = input("Enter order amount: ")

        if amount.isdigit():
            orders.append(int(amount))
            print("Order added")
        else:
            print("Invalid amount")
            continue

    elif choice == "2":
        if len(orders) == 0:
            print("No orders available")
            continue

        print("Order | Discount | Final Amount")
        print("--------------------------------")

        for order_amount in orders:
            if order_amount >= 2000:
                discount_rate = 0.15
            elif order_amount >= 1500:
                discount_rate = 0.10
            elif order_amount >= 1000:
                discount_rate = 0.07
            else:
                discount_rate = 0.0

            discount = order_amount * discount_rate
            final_amount = order_amount - discount

            print(order_amount, "|", discount, "|", final_amount)

    elif choice == "q":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
        continue