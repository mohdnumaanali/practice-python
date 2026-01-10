# now we are going to make table using 
for i in range(1,11):
    square = i ** 2 
    print(f"{i} , squared is = {square}")

#now we take from user :
 
# number = int(input("type any number : "))
# for number in range():
#     square = number ** 2
#     print(f"{number}, square is = ")

target = float(input("Enter a number to find the square root of: "))

# We will try every number from 0 to the target
# We use a large range and divide by 100 to check decimals
guess_root = 0

for i in range(0, int(target * 100)): 
    guess = i / 100  # This lets us check 0.01, 0.02, 0.03...
    
    if guess * guess >= target:
        guess_root = guess
        break # We found the closest match!

print(f"The approximate square root is: {guess_root}")
