# ATM MACHINE MINI PROJECT - 01  
balance = 10000

# Step 1: Language Selection (Asked only once)
step1 = input("Select your language (English, Hindi, Telugu): ").lower().strip()

if step1 == "hindi":
    print("आपने हिंदी चुनी है।")
elif step1 == "telugu":
    print("మీరు తెలుగును ఎంచుకున్నారు।")
else:
    print("You have selected English.")

# Step 2: Main Transaction Loop
while True:
    print("\n" + "="*20)
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choose = input("Select an option (1-4): ")

    if choose == "1":
        print(f"Your current balance is: ${balance}") 
    
    elif choose == "2":
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"✅ Transaction successful! Remaining: ${balance}")
        else:
            print("❌ Insufficient amount!")
            
    elif choose == "3":
        amount2 = float(input("Enter the amount to deposit: "))
        balance += amount2
        print(f"✅ Deposit successful! Current balance: ${balance}")
        
    elif choose == "4":
        print("Exiting... Thank you for using our ATM!")
        break # This breaks the loop immediately
        
    else:
        print("⚠️ ERROR: Invalid Choice")

    # Step 3: The "Continue" Question
    # We ask this after every transaction except 'Exit'
    repeat = input("\nDo you want to perform another transaction? (yes/no): ").lower().strip()
    if repeat == "no":
        print("Thank you! Visit again.")
        break # This stops the loop