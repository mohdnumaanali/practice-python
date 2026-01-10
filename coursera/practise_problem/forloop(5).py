# prices = [1, 2, 4, 9, 0]
# total = 0
# for p in prices:
#     total += p
# print(f"Total cost: {total}")

total = 0

print("Enter 5 numbers:")

for i in range(1, 6):
    # We loop until we get a valid number for THIS specific 'i'
    while True:
        raw_data = input(f"Number {i}: ")
        clean_data = raw_data.strip() # This removes hidden spaces
        
        try:
            number = int(clean_data)
            total += number
            break # Moves to the next 'i' in the for loop
        except ValueError:
            # This tells us EXACTLY what Python saw that it didn't like
            print(f"❌ Error: Python saw '{raw_data}', which is not a number.")

print(f"✅ Finished! Total is: {total}")