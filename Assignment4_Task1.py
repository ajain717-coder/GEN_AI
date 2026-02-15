# Task 1: Write Sales Records to a File

sales = [1200, 450, 980, 1500, 3000]

file = open("sales_data.txt", "w")

for amount in sales:
    file.write(str(amount) + "\n")

file.close()

# Reopen and print contents
file = open("sales_data.txt", "r")
print("File contents after writing:")
print(file.read())
file.close()