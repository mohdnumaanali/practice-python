# password  = "student69"
# while password :
#     if password == "student69" :
#         break
#         print(" acces granted ")
#     else :
#         print(" try again ")                                  mera try tah yai 

secret = "student69"

while True:  # Run forever until we hit 'break'
    guess = input("Enter password: ")  # Ask the user for a guess
    
    if guess == secret:
        print("Access Granted!") 
        break  # NOW we exit, after saying hello
    else:
        print("Wrong! Try again.")

print("Loop is finished.")