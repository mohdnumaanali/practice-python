# List of different students' marks ------------- normal way
student_marks = [95, 82, 73, 65, 54]

print("--- Class Grading Report ---")

for mark in student_marks:
    if 90 <= mark <= 100:
        grade = "A"
    elif 80 <= mark < 90:
        grade = "B"
    elif 70 <= mark < 80:
        grade = "C"
    elif 60 <= mark < 70:
        grade = "D"
    else:
        grade = "F"
    
    print(f"Mark: {mark} | Grade Allotted: {grade}")

#  USER INPUT WAY ----------------------------------------------------

# Get input from the user
your_marks = float(input("Enter your marks: "))

# We don't need a for loop for one person! 
# Just use the logic directly:
if 90 <= your_marks <= 100:
    print(f"Grade Allotted: A ({your_marks})")
elif 80 <= your_marks < 90:
    print(f"Grade Allotted: B ({your_marks})")
elif 70 <= your_marks < 80:
    print(f"Grade Allotted: C ({your_marks})")
else:
    print(f"Grade Allotted: Below C ({your_marks})")