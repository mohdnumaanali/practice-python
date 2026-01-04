total = 0
count = 0

while True:
    num = float(input("Enter a number (or -1 to calculate average): "))
    
    if num == -1:
        break
    
    total += num    # This is the Accumulator (Sum)
    count += 1      # This is the Counter (How many)

# Check if count is greater than 0 to avoid dividing by zero error
if count > 0:
    average = total / count
    print(f"Total Sum: {total}")
    print(f"Numbers entered: {count}")
    print(f"The average is: {average}")
else:
    print("No numbers were entered.")