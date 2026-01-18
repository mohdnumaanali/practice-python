database = {
    "numan123": "pass@12",
    "ali_v": "hello2026"
}

def login(user, pwd):
    # Check if user is in keys AND if password matches the value
    if user in database and database[user] == pwd:
        return True
    else:
        return False

# Loop for 3 attempts
attempts = 3
while attempts > 0:
    u = input("Username: ")
    p = input("Password: ")

    if login(u, p):
        print("🔓 Access Granted! Welcome to the system.")
        break
    else:
        attempts -= 1
        print(f"❌ Access Denied. {attempts} attempts left.")

if attempts == 0:
    print("🚫 Account Locked. Contact Support.")