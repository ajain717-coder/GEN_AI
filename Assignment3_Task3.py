# Task 3: Lambda Function

gst = lambda price: price + (0.18 * price)

print(gst(100))

# Extra
final_price = lambda price, discount: gst(price - (price * discount / 100))
print(final_price(1000, 10))