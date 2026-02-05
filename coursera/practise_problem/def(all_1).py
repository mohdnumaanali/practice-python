# Even or Odd: Write a function that returns "Even" or "Odd" for a given integer.
# def even_odd(n):
#     return "Even" if n % 2 == 0 else "Odd"

# print(even_odd(2))

# 1.
def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"
print(even_odd(9) , even_odd(2))
# 2.
def max_three(a, b, c):
    return max(a, b, c)

print(max_three(2,9,6))

# 3.
def sum_list(items):
    total = 0
    for x in items:
        total += x
    return total

# 4.
def in_range(n):
    return 1 <= n <= 10

# 5.
def count_vowels(s):
    count = 0
    for char in s.lower():
        if char in "aeiou":
            count += 1
    return count

# 6.
def reverse_list(items):
    return items[::-1]

# 8.
def is_palindrome(word):
    return word == word[::-1]

# 10.
def mult_table(n):
    for i in range(1, 11):
        print(n * i)

print(even_odd(2))          # Output: Even
print(max_three(5, 9, 3))   # Output: 9
print(sum_list([1, 2, 3]))  # Output: 6
print(in_range(7))          # Output: True
print(count_vowels("Hello"))# Output: 2
print(reverse_list([1,2,3]))# Output: [3,2,1]
print(is_palindrome("madam")) # Output: True
mult_table(5)               # Prints multiplication table of 5
