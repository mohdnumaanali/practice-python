try:
    # 1. Get inputs and convert to float
    balance = float(input("Enter your current balance: "))
    withdraw = float(input("Enter amount to withdraw: "))

    # 2. Logic chain
    if withdraw <= 0:
        print("Invalid amount. You must withdraw more than 0.")
        
    elif withdraw > balance:
        print("Insufficient funds. You cannot withdraw more than you have.")
        
    elif withdraw == balance:
        print("Warning: Your account will be empty!")
        print("Transaction successful. Remaining Balance: 0.0")
        
    else:
        # Standard successful transaction
        new_balance = balance - withdraw
        print("Transaction successful.")
        print("New Balance:", new_balance)

except ValueError:
    # This runs specifically if they type "hello" instead of 50.0
    print("Error: Invalid entry. Please enter numbers for balance and withdrawal.")

except Exception as e:
    # This catches anything else (like a system error) and tells us what happened
    print("An unexpected error occurred:", e)
print("THE END OF THE PROGRAM ")