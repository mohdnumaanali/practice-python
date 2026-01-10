print("---------- REGISTRATION PORTAL ----------")

while True:
    # NAME CHECK
    name = input("What is your name: ")

    if not name.isalpha():
        print("❌ Invalid name! Name should contain only letters.")
        continue
    else:
        print(f"Hello {name}")

    # PLACE CHECK
    place = input("Where are you from: ").lower()

    if place != "india":
        print("❌ Not allowed! Only people from India are allowed.")
        continue
    else:
        print("✅ Place accepted")

    # HOUSE NUMBER CHECK (try-except)
    try:
        house = int(input("What is your house number: "))
        print(f"House No: {house}")
    except ValueError:
        print("❌ House number must be a number!")
        continue

    # EXIT OPTION
    choice = input("Do you want to register another person? (yes/no): ").lower()
    if choice != "yes":
        print("✅ Registration completed. Thank you!")
        break
