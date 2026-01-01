# def add_numbers(num1, num2):
#     print(num1 + num2)

# # Call it with RAW numbers (no quotes)
# add_numbers(50, 25)
# add_numbers(33,33)
# add_numbers(44,44)
# add_numbers(33,67)

# # user version 
# def add_numbers(n1, n2):
#     print("The sum is:", n1 + n2)

# # Using it for the first set
# a = float(input("Enter first: "))
# b = float(input("Enter second: "))
# add_numbers(a, b)

# # Using it for the second set
# x = float(input("Enter another: "))
# y = float(input("And another: "))
# add_numbers(x, y) # I don't write "print(x+y)", I just reuse the machine5
# add_numbers(x,y)
# add_numbers(x,y)

def add_numbers(n1, n2):
    print("The sum is:", n1 + n2)

# Now, even for 10 inputs, the code looks organized
add_numbers(float(input("1: ")), float(input("2: ")))
add_numbers(float(input("3: ")), float(input("4: ")))
add_numbers(float(input("5: ")), float(input("6: ")))
add_numbers(float(input("7: ")), float(input("8: ")))
add_numbers(float(input("9: ")), float(input("10: ")))

#---------------------------------------------------------

#loop type 
def add_numbers(n1, n2):
    print("The sum is:", n1 + n2)

# This loop runs 5 times, doing 10 inputs in total
for i in range(5):
    a = float(input("Enter first: "))
    b = float(input("Enter second: "))
    add_numbers(a, b)