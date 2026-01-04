# banded_word = " spam "
# while True : 
#     user_input = input("say something : ")
#     if user_input.lower() == banded_word :
#         print(" this is bannded word you can;t use it ")
#         break 
#     else :
#         print("this word is not bannded it is safe want to try new word : ")

banned_word = "spam"  # Removed the spaces

while True:
    user_input = input("Say something: ")
    
    # We use .lower() so "SPAM", "Spam", and "spam" all get caught
    if user_input.lower() == banned_word:
        print(f"ERROR: {user_input} is a banned word! System locking...")
        break 
    else:
        print(f"'{user_input}' is safe. Want to try a new word?")