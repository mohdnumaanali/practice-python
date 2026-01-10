# 1. Preparation
grades = []

print("--- Student Grade Database ---")

while True:
    # 2. Input
    entry = int(input("Enter a grade (0-100) or -1 to finish: "))
    
    # 3. The Exit Logic
    if entry == -1:
        break
    
    # 4. The Validation (The "Guard")
    if entry < 0 or entry > 100:
        print("❌ Invalid Grade! Please enter a number between 0 and 100.")
        continue # Jumps back to the start of the loop
        
    # 5. The Storage
    grades.append(entry)
    print(f"Added {entry}. (Total students so far: {len(grades)})")

# --- FINAL REPORT (After the loop) ---
if len(grades) > 0:
    total_sum = sum(grades)
    count = len(grades)
    average = total_sum / count

    print("\n" + "="*20)
    print(f"Final Grades: {grades}")
    print(f"Number of Students: {count}")
    print(f"Class Average: {average:.2f}") # Rounds to 2 decimal places
    print("="*20)
else:
    print("No grades were entered.")