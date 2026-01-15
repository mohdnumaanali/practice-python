inventory = {
    "Apple": {"price": 20, "quantity": 50},
    "Banana": {"price": 10, "quantity": 100},
    "Orange": {"price": 15, "quantity": 30}
}

item = input("What do you want to buy? (Apple/Banana/Orange): ").capitalize()

if item in inventory:
    wanted = int(input(f"How many {item}s do you want? "))
    stock = inventory[item]["quantity"]
    price = inventory[item]["price"]

    if wanted <= stock:
        total_bill = wanted * price
        # Update the quantity in the dictionary
        inventory[item]["quantity"] -= wanted
        print(f"✅ Success! Total bill: ${total_bill}")
        print(f"Remaining {item} stock: {inventory[item]['quantity']}")
    else:
        print(f"❌ Sorry, we only have {stock} in stock.")
else:
    print("❌ We don't sell that item.")