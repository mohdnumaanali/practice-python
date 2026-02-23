def clean_and_save(input_list, output_file):
    try:
        # Open the output file in 'w' mode to start fresh
        with open(output_file, "w") as f:
            for line in input_list:
                try:
                    # 1. Check if the line is just whitespace or empty
                    if not str(line).strip():
                        print("Skipping empty line...")
                        continue
                    
                    # 2. Clean the data (removing spaces and making it Title Case)
                    clean_name = str(line).strip().capitalize()
                    
                    # 3. Save the valid name to our new file
                    f.write(clean_name + "\n")
                    print(f"✅ Saved: {clean_name}")
                
                except Exception as e:
                    print(f"❌ Error processing line '{line}': {e}")
        
        print(f"\n--- Process Complete! Check '{output_file}' ---")

    except IOError:
        print("Fatal Error: Could not create the output file.")

# --- MASHUP TEST ---
# A mix of good names, empty strings, spaces, and numbers
raw_data = ["numan", "  ", "ALEX", "", "sarah", 1024, "  john  "]


clean_and_save(raw_data, "cleaned_users.txt")

#2

import math

def calculate_sqrt(num_list):
    results = []
    
    for item in num_list:
        try:
            # Step 1: Try to convert to float (in case it's a string like "25")
            val = float(item)
            
            # Step 2: Try to get square root
            # math.sqrt() raises ValueError for negative numbers
            res = math.sqrt(val)
            results.append(res)
            print(f"Square root of {val} is {res}")
            
        except ValueError:
            # This catches both text like "abc" AND negative numbers
            print(f"⚠️ Skipping '{item}': Invalid for square root.")
        except TypeError:
            print(f"⚠️ Skipping '{item}': Data type not supported.")
            
    return results

# Test the mashup
test_data = [25, -9, "100", "apple", 16]
final_list = calculate_sqrt(test_data)
print(f"Final valid results: {final_list}")

#2

import math

def calculate_sqrt(num_list):
    results = []
    
    for item in num_list:
        try:
            # Step 1: Try to convert to float (in case it's a string like "25")
            val = float(item)
            
            # Step 2: Try to get square root
            # math.sqrt() raises ValueError for negative numbers
            res = math.sqrt(val)
            results.append(res)
            print(f"Square root of {val} is {res}")
            
        except ValueError:
            # This catches both text like "abc" AND negative numbers
            print(f"⚠️ Skipping '{item}': Invalid for square root.")
        except TypeError:
            print(f"⚠️ Skipping '{item}': Data type not supported.")
            
    return results

# Test the mashup
test_data = [25, -9, "100", "apple", 16]
final_list = calculate_sqrt(test_data)
print(f"Final valid results: {final_list}")

#3
import os

def verify_and_write(folder_name, filename, data):
    # Phase 2: System logic using 'os'
    try:
        # Check if folder exists, if not, create it
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            print(f"📁 Created folder: {folder_name}")
        else:
            print(f"✅ Folder '{folder_name}' already exists.")

        # Phase 2: File Handling
        file_path = os.path.join(folder_name, filename)
        
        with open(file_path, "w") as f:
            f.write(data)
        
        print(f"💾 Data saved successfully to: {file_path}")

    except PermissionError:
        print("❌ Error: You don't have permission to write here.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Test the auditor
verify_and_write("User_Reports", "report_01.txt", "Phase 1 & 2: Status - MASTERED")
