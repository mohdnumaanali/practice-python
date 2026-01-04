balance = 1000
history = []  # This list will store our "memory" of transactions

while True:
    print("\n--- ADVANCED ATM ---")
    print(f"Current Balance: ${balance}")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View History")
    print("4. Exit")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        amount = int(input("Amount to deposit: "))
        balance += amount
        history.append(f"Deposited: ${amount}") # Adding to our list
        print("Done!")
        
    elif choice == "2":
        amount = int(input("Amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            history.append(f"Withdrew: ${amount}") # Adding to our list
            print("Done!")
        else:
            print("Insufficient funds!")
            
    elif choice == "3":
        print("\n--- Transaction History ---")
        if not history:
            print("No transactions yet.")
        else:
            print(history) # Printing our list
            
    elif choice == "4":
        print("Goodbye!")
        break