def get_summary(student_data):
    name = student_data["name"]
    marks = student_data["marks"]
    
    # 1. Calculate Average
    avg = sum(marks) / len(marks)
    
    # 2. Determine Grade
    if avg >= 80:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    else:
        grade = "C"
        
    # 3. Return a brand new dictionary
    return {
        "name": name,
        "average": round(avg, 2),
        "grade": grade
    }

# Testing it
student_1 = {"name": "Numan", "marks": [85, 90, 88]}
summary = get_summary(student_1)

print(f"Summary Report: {summary}")