# password = input("Enter a password to test: ")

# has_upper = False
# has_lower = False
# has_digit = False

# for char in password:
#     if char.isupper():
#         has_upper = True
#     elif char.islower():
#         has_lower = True
#     elif char.isdigit():
#         has_digit = True

# if has_upper and has_lower and has_digit and len(password) >= 8:
#     print("✅ Strong Password!")
# else:
#     print("❌ Weak Password! (Needs Upper, Lower, Digit, and 8+ chars)")


# above code only run 1 time now we are try new code which run in loop 

while True:
    password = input("\nCreate a new password: ").strip()
    
    if not password:
        print("❌ Password cannot be empty!")
        continue

    has_upper = False
    has_lower = False
    has_digit = False

    # The "Scanner" Loop
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    # Final Validation
    if has_upper and has_lower and has_digit and len(password) >= 8:
        print("✅ Strong Password! Account Created.")
        break # This exits the while loop
    else:
        print("❌ Weak Password! Requirements:")
        print("   - At least 8 characters")
        print("   - One Uppercase, One Lowercase, and One Digit")