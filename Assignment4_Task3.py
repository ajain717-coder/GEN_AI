# Task 3: Append New Sales

new_sales = [5000, 2500, 1700]

file = open("sales_data.txt", "a")

for amount in new_sales:
    file.write(str(amount) + "\n")

file.close()

# Reopen and print updated file
file = open("sales_data.txt", "r")
updated_lines = file.readlines()
file.close()

print("Updated file contents:")
for line in updated_lines:
    print(line.strip())

# Extra (optional): total number of lines
print("Total number of lines:", len(updated_lines))
