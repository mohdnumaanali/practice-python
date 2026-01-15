contacts = {
    "Numan": {"phone": "9876543210", "email": "numan@example.com"},
    "Ali": {"phone": "1234567890", "email": "ali@example.com"}
}

name = input("Enter name to search: ").capitalize()

if name in contacts:
    print(f"Found {name}!")
    choice = input("Do you want (1) Phone or (2) Email? ")
    
    if choice == "1":
        print(f"Phone: {contacts[name]['phone']}")
    elif choice == "2":
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Invalid choice.")
else:
    print("Contact not found!")
    add_new = input("Would you like to add this contact? (yes/no): ").lower()
    
    if add_new == "yes":
        new_phone = input("Enter Phone: ")
        new_email = input("Enter Email: ")
        # Adding a new dictionary inside the main dictionary
        contacts[name] = {"phone": new_phone, "email": new_email}
        print(f"✅ {name} has been added to your contacts!")

print("\nUpdated Contacts List Keys:", list(contacts.keys()))