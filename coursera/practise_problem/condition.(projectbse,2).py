try:
    # 1. Get input and convert to float (safety first!)
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    # 2. Check for Overtime
    if hours <= 40:
        # Simple math for normal hours
        pay = hours * rate
    else:
        # Math for Overtime:
        # Regular pay for first 40 + Overtime pay for the rest
        regular_pay = 40 * rate
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        
        pay = regular_pay + overtime_pay

    print("Pay:", pay)

except:
    # This runs if the user types "ten" instead of 10
    print("Error, please enter numeric input")


# while True: # This keeps the program running forever...
#     inp = input("Enter Hours (or type 'done' to quit): ")
    
#     if inp == 'done':
#         break # This is the "Emergency Exit" for the loop
        
#     try:
#         hours = float(inp)
#         # ... (the rest of your pay logic goes here)
#         print("Pay calculated!")
#     except:
#         print("Invalid input")

# print("All done!")                                                                    #loops ke sath multiple 