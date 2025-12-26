ticket_pass_name = "ali"
age = 23
person_name = input(" what is your name : ")
person_name_age = input("what is your age:  ")
if person_name == ticket_pass_name and age == person_name_age :
    print("approved")
else:
    print("reject")

try:
    if "approved":
        print("pay the platform charge")
    else: 
        print("you not allowed to travel ")
except: 
    print("pay online or wait for next train")



