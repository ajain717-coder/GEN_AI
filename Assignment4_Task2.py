# Task 2: Read File in Different Ways

# 1. Read entire file
file = open("sales_data.txt", "r")
print("Using read():")
print(file.read())
file.close()

# 2. Read first line
file = open("sales_data.txt", "r")
print("Using readline():")
print(file.readline())
file.close()

# 3. Read all lines and convert to integers
file = open("sales_data.txt", "r")
lines = file.readlines()
file.close()

sales_list = []

for line in lines:
    sales_list.append(int(line.strip()))

print("Sales list:", sales_list)