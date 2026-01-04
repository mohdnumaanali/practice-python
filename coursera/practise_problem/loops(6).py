# total = 0 
# while True :
#     ammount = float(input("enter the number : "))
#     if ammount == 0 :
#         print("end")
#         break
#     else :
#         ammount+= total 
#         print("say more ")

total = 0 
while True :
    ammount = float(input("Enter the number: ")) # User gives 10
    if ammount == 0:
        break
    else:
        total += ammount # ADD the 10 to the total (0 + 10)
        print(f"Current Total: {total}")

print(f"Grand Total: {total}")
