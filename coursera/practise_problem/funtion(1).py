# #,Concept,What you learned
# 1,def,How to start a function.
# 2,Calling,How to use the machine you built.
# 3,Arguments,"Passing data into the machine (n1,n2)."
# 4,return,Getting data back out (The Delivery Guy).
# 5,The Exit Rule,return kills the function immediately.
# 6,Math Logic,"Doing squares, multiplication, etc."
# 7,Conditionals,Putting if/else inside a function (Computepay).
# 8,Order,"Why (price, discount) is different from (discount, price)."
# 9,Defaults,"Setting a standard value like message=""Hello""."
# 10,Scope,"Why variables inside a function are ""private."""



# # 1. We DEFINE the function (teaching Python the recipe)
# def print_info():
#     print("Name: Ali")
#     print("Favorite Language: Python")

# # 2. We CALL the function (actually cooking the meal)
# print_info()


# --- STEP 1: DEFINE OUR TOOLS (The Recipes) ---

def show_menu():
    print("\n--- WELCOME TO THE BANK ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def calculate_interest(balance, rate):
    # This is a 'Fruitful' function that returns a value
    interest = balance * (rate / 100)
    return interest

def secure_login(correct_pin):
    try:
        user_pin = int(input("Enter your 4-digit PIN: "))
        if user_pin == correct_pin:
            return True
        else:
            print("Incorrect PIN!")
            return False
    except:
        print("Error: PIN must be numbers only.")
        return False

# --- STEP 2: THE "MAIN STORY" (The 1,000-line logic) ---

# Imagine we have 100 users. We just call our tools.
my_balance = 1000.0

if secure_login(1234): # Using our login tool
    show_menu()        # Using our menu tool
    
    # Let's say we want to see interest for the next year
    year_interest = calculate_interest(my_balance, 5.0)
    print("In one year, you will earn:", year_interest)
    
    my_balance = my_balance + year_interest
    print("New projected balance:", my_balance)

else:
    print("Access Denied. Program ending.")