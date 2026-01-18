# 1. Global Price Database
price_list = {
    "Laptop": 800,
    "Mouse": 20,
    "Keyboard": 50,
    "Monitor": 150,
    "USB Cable": 10
}

# 2. The Logic Function
def process_cart(user_cart):
    subtotal = 0
    
    # Calculate initial total
    for item in user_cart:
        if item in price_list:
            subtotal += price_list[item]
        else:
            print(f"Warning: {item} is not in our store!")

    # Logic for Discount
    discount = 0
    if subtotal > 100:
        discount = subtotal * 0.10  # 10% off
    
    final_total = subtotal - discount
    
    # Returning multiple values as a group
    return subtotal, discount, final_total

# 3. Main Program (Using the Function)
my_items = ["Monitor", "Keyboard", "Mouse", "USB Cable"]

# Getting multiple values back from the function
sub, disc, grand = process_cart(my_items)

print("--- MEGA-MART RECEIPT ---")
print(f"Subtotal:   ${sub}")
print(f"Discount:  -${disc}")
print(f"-------------------------")
print(f"TOTAL DUE:  ${grand}")