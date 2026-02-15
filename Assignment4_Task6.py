import os

filename = input("Enter file name: ")

if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f.read())
else:
    print("File not found. Please check the filename.")
