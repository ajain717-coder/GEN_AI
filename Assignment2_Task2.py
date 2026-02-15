# Task 2: Process Multiple Orders

orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discounted_orders = 0

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

    total_revenue += final_amount

    if discount > 0:
        discounted_orders += 1

    print(order_amount, "|", discount, "|", final_amount)

print("--------------------------------")
print("Total Revenue:", total_revenue)
print("Orders with Discount:", discounted_orders)