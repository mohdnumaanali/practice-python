'''
# 1. Handling Multiple Specific Exceptions
try:
    val = int(input("Enter a divisor: "))
    result = 100 / val
    print(result)
except ValueError:
    print("Error: That wasn't a valid number.")
except ZeroDivisionError:
    print("Error: You can't divide by zero.")

# 2. Using the 'else' Block (Runs ONLY if NO error occurs)
try:
    num = int(1.23)
except ValueError:
    print("Conversion failed.")
else:
    print(f"Success! The number is {num}.")

# 3. File Writing Guard (Handling I/O errors)
try:
    with open("/protected_folder/file.txt", "w") as f:
        f.write("Hello")
except IOError:
    print("Error: Could not write to file. Check permissions.")

# 4. Function Safety with Default Returns
def safe_get_first_letter(word):
    try:
        return word[0]
    except (TypeError, IndexError):
        return "N/A" # Returns a default value instead of crashing
'''
# 5. List Processing with try/except
mixed_data = ["10", "apple", "20", "orange"]
total = 0
for item in mixed_data:
    try:
        total += int(item)
    except ValueError:
        continue # Skip items that aren't numbers

#5th explain version 

# A list containing both strings that look like numbers and plain text
mixed_data = ["10", "apple", "20", "orange", "30"]
total = 0

for item in mixed_data:
    try:
        # Step 1: Try to convert the string to an integer
        number = int(item)
        
        # Step 2: If conversion works, add it to our running total
        total += number
        
    except ValueError:
        # Step 3: If it's NOT a number (like "apple"), catch the error
        print(f"⚠️ Skipping '{item}' because it's not a number.")
        continue # Move to the next item in the list

print(f"✅ Final Total: {total}")