# The Double Catch: Write one try block that handles both ValueError and ZeroDivisionError.
try :
    result = 10 / 0 
except ZeroDivisionError :
    print("you got error you can't divide ")

#2
#The "Success" Message: Use the else keyword to print "Calculation Successful" only if no error occurred.

try :
    a = int(input("enter your age : "))
    if a >= 18 :
        print("approved ")
    else :
        print("disapprove")
except ValueError :
    print("your enter value is incorrect ")

# 2. Catching ValueError (Input Protection)
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Error: Please enter a whole number (e.g., 25).")

# 3. Catching FileNotFoundError
try:
    with open("test.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: The file 'test.txt' was not found.")        

# 4. Catching TypeError
try:
    total = "Price: " + 10  # Cannot add string and int
except TypeError:
    print("Error: You can only join strings to other strings.")
# 5. Catching IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError:
    print("Error: That index is out of range for this list.")