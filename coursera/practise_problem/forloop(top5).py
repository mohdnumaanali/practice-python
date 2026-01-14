inventory = [10, 0, 5, 0, 20, 3]
reorder_count = 0

for stock in inventory:
    if stock == 0:
        print("Status: Out of Stock! 🚨")
        reorder_count += 1
    elif stock < 5:
        print(f"Status: Low Stock ({stock}) ⚠️")
        reorder_count += 1
    else:
        print(f"Status: OK ({stock}) ✅")

print("-" * 20)
print(f"Total items to reorder: {reorder_count}")