# total = 0 
# while True : 
#     user = int(input("enter a number : "))
#     if user == 0 :
#         print("come back again ")
#         break 
#     if user 

total = 0
print("Enter numbers to add them. Only EVEN numbers will be saved! (0 to quit)")

while True:
    num = int(input("Enter number: "))
    
    if num == 0:
        break # Exit the loop
        
    if num % 2 != 0:
        print("Skipping odd number...")
        continue # Jumps back to the 'while True' line immediately
        
    total += num
    print(f"Current Even Total: {total}")

print(f"Final Sum of Even Numbers: {total}")