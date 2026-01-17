#Password Strength: Write a function is_strong(password) that returns "Strong"
#  if the password has more than 8 characters, and "Weak" if it has less.

def is_strong(password):
    if len(password) > 8:
        return "Strong"
    else:
        return "Weak"

print(is_strong("12345"))      # Output: Weak
print(is_strong("mypassword123")) # Output: Strong