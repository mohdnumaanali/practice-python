banned_word = "spam"  # Removed the spaces

while True:
    user_input = input("Say something: ")
    
    # We use .lower() so "SPAM", "Spam", and "spam" all get caught
    if user_input.lower() == banned_word:
        print(f"ERROR: {user_input} is a banned word! System locking...")
        break 
    else:
        print(f"'{user_input}' is safe. Want to try a new word?")