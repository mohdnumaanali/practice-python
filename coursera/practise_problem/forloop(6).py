# name = ["Bob", "Charlie", "Alice", "David"]
# name == "Alice"
# print("Found her!")

names = ["Bob", "Charlie", "Alice", "David"]
for name in names:
    if name == "Alice":
        print("Found her!")
        break # Stops searching immediately once found