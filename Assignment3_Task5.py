# Task 5: filter() Example

prices = [100, 250, 400, 1200, 50, 2000, 850]

greater_than_500 = list(filter(lambda x: x > 500, prices))
less_or_equal_500 = list(filter(lambda x: x <= 500, prices))

print("Prices > 500:", greater_than_500)
print("Prices <= 500:", less_or_equal_500)