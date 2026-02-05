# 1.
def unique_list(items):
    return list(set(items))

# 3.
def factorial(n):
    if n == 1: return 1
    return n * factorial(n - 1)

# 4.
import random
def roll_die():
    return random.randint(1, 6)

# 5.
def letter_freq(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# 7.
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

# 9.
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# 1. Unique list
print(unique_list([1, 2, 2, 3, 4, 4]))  
# Output: [1, 2, 3, 4] (order may vary because sets are unordered)

# 3. Factorial
print(factorial(5))  
# Output: 120

# 4. Roll a die
print(roll_die())  
# Output: Random number between 1 and 6

# 5. Letter frequency
print(letter_freq("banana"))  
# Output: {'b': 1, 'a': 3, 'n': 2}

# 7. Safe division
print(safe_div(10, 2))  
# Output: 5.0
print(safe_div(10, 0))  
# Output: "Cannot divide by zero!"

# 9. Prime check
print(is_prime(2))  
# Output: True
print(is_prime(15))  
# Output: False
