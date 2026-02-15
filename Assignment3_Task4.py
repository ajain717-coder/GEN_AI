# Task 4: map() Example
gst = lambda price: price + (0.18 * price)
prices = [100, 250, 400, 1200, 50]

prices_with_gst = list(map(gst, prices))

print("Original prices:", prices)
print("Prices after GST:", prices_with_gst)