# while True :
#     user = int(input("enter a number or enter - 0 - to quit  : "))
#     if user == 0 :
#         print("okat come again later ")
#         break
#     elif user == user%3 :
#         print('fizz')
#     elif user == user%5 :
#         print("buzz")
#     else :
#         print("fizzbuzz")

while True:
    user = int(input("Enter a number (0 to quit): "))
    
    if user == 0:
        print("Okay, come again later!")
        break
    
    # Check for BOTH first
    if user % 3 == 0 and user % 5 == 0:
        print("fizzbuzz")
    elif user % 3 == 0:
        print("fizz")
    elif user % 5 == 0:
        print("buzz")
    else:
        print(user)