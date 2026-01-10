# print("checking your a real person or not ")
# while True :
#     user_input = int(input(" enter the screat number 10 to 20 : "))

#     if user_input 

while True:
    num = int(input("Enter a secret number between 10 and 20: "))
    
    # This checks if the number is within the "Safe Zone"
    if 10 <= num <= 20:
        print(f"Perfect! {num} is in the range. Access granted.")
        break  # The only way to escape the loop!
    else:
        print("Invalid! That is not between 10 and 20. Try again.")