# pasword = "python"

# chance_1 = input("enter the pasword : ")
# chance_2 = input("enter the pasword : ")
# chance_3 = input("enter the pasword : ")
# try :

#     if chance_1 == pasword :
#         print("acces granted")
#     else :
#         print("you have two chance remaining")
# except : 
#     print("try again")
# try :
    
#     if chance_2 == pasword :
#         print("acces granted")
#     else :
#         print("you have one chance remaining")
# except :
#     print("try again ")
# try : 
    
#     if chance_3 == pasword :
#         print("acces granted")
#     else :
#         print("you have zero chance remaining")
# except :
#     print("account is locked ")

password = "python"
attempts = 3  # We start with 3 lives

while attempts > 0:
    guess = input(f"Enter password ({attempts} tries left): ").strip().lower()
    
    if guess == password:
        print("Access Granted!")
        break  # This exits the loop immediately!
    else:
        attempts -= 1  # We lose a life
        if attempts > 0:
            print("Wrong! Try again.")
        else:
            print("Account Locked. Too many failed attempts.")