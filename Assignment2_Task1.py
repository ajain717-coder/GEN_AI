# Task 1: Discount Rules

user_input = input("Enter order amount: ")

# Check if input is numeric
if user_input.isdigit():
    order_amount = int(user_input)

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

    print("Order Amount:", order_amount)
    print("Discount Applied:", discount)
    print("Final Amount:", final_amount)

else:
    print("Error: Please enter a valid numeric amount")