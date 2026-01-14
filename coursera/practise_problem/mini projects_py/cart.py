cart = []
total = 0

for i in range(3):
    item_name = input(f"Enter item {i+1} name: ")
    price = float(input(f"Enter price for {item_name}: "))
    cart.append([item_name, price])

print("\n--- Your Receipt ---")
for item in cart:
    print(f"{item[0]}: ${item[1]}")
    total += item[1]

print(f"Total: ${total}")
print(f"Total with 5% Tax: ${total * 1.05:.2f}")