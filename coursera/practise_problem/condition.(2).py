#Write a program that asks for a number using input(). Use try and except so that if the user types a word (like "hello"), the program prints "Invalid Input" instead of crashing.

# 1. Ask for input
user_input = input("Enter a number: ")

# 2. Start the safety net
try:
    # This is dangerous because we don't know if input is a number
    number = (user_input) 
    print("Success! Your number is:", number)
    
except:
    # This runs ONLY if the line above failed (user typed a word)
    print("Invalid Input")
    