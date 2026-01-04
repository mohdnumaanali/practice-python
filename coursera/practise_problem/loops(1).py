# 🔄 Introduction to Loops
# A loop is simply a way to tell the computer: "Don't stop doing this until I say so."

# There are two main types of loops in Python:
#-------------------------------------------------------------------------------------------------------------------------
# while loops: These run as long as a condition is True (like a "While the light is green, keep driving" rule).

# for loops: These run for a set number of times (like a "Do 10 pushups" rule).
#--------------------------------------------------------------------------------------------------------------------------

#while loop example 1 

n = 5
while n > 0:
    print(n)
    n = n - 1  # This is the most important line!
print("Blast off!")

#example 2--------------------------------------------------------------------

count = 1
while count <= 3:
    print("Hello")
    count = count + 1

#example 3-------------------------break-----------------------------------------

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Finished!')

#example 4----------------------------break----------------------------------

total = 0
while True:
    number = int(input("Enter a price (or type 0 to stop): "))
    if number == 0: # 0 is our Sentinel value
        break
    total = total + number

print("Your total is:", total)

#example 5----------------------continue------------------------------------------

n = 5
while n > 0:
    n = n - 1
    if n == 3:
        continue # Skip the rest of the code for this round
    print(n)