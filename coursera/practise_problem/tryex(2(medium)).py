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

#6 

try:
    with open("primary_data.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    # If the first file is missing, we "nest" another try inside the except
    try:
        print("Primary missing, trying backup...")
        with open("backup_data.txt", "r") as f:
            data = f.read()
    except FileNotFoundError:
        print("Total Failure: No data sources found.")

#7

def set_age(age):
    if age < 0:
        # We manually trigger an error because a negative age is impossible
        raise ValueError("Age cannot be negative!")
    return f"Age set to {age}"

try:
    print(set_age(10))      # put - 10 
except ValueError as e:
    print(f"Invalid input: {e}")

#8

try:
    my_data = 12345
    # This will fail because numbers don't have 'upper'
    print(my_data.upper()) 
except AttributeError:
    print("❌ Error: You are trying to use a text-tool on a number!")

#9
try:
    result = 10 / 0
except Exception as e:
    # 'e' contains the official error message: "division by zero"
    print(f"The system reported this specific error: {e}")

#10

file = None
try:
    file = open("log.txt", "w")
    file.write("Updating system logs...")
    # Imagine an error happens here...
except IOError:
    print("Error writing to file.")
finally:
    # This part runs even if the write failed OR succeeded
    if file:
        file.close()
        print("🧹 Cleanup: File closed safely.")