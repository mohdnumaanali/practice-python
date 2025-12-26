ticket_pass_name = "ali"
age = 23

person_name = input("What is your name: ")
# FIX 1: Wrap input in int() to convert the text to a number
person_name_age = int(input("What is your age: ")) 

# We create a variable to track the status
status = "pending"

if person_name == ticket_pass_name and age == person_name_age:
    print("Approved")
    status = "approved" # Update the status
else:
    print("Reject")
    status = "rejected"

print("--- Next Step ---")

# FIX 2: Check if the VARIABLE status is equal to "approved"
try:
    if status == "approved":
        print("Pay the platform charge.")
    else: 
        print("You are not allowed to travel.")
except: 
    # This only runs if the code above crashes
    print("An error occurred. Please wait for the next train.")