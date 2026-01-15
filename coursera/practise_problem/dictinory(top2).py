marks = [85, 92, 70, 45, 99, 60, 75]

report_card = {
    "Excellent": [],
    "Good": [],
    "Needs Improvement": []
}

for m in marks:
    if m >= 90:
        report_card["Excellent"].append(m)
    elif m >= 70:
        report_card["Good"].append(m)
    else:
        report_card["Needs Improvement"].append(m)

print("--- Final Report Card ---")
for category, list_of_marks in report_card.items():
    print(f"{category}: {list_of_marks}")