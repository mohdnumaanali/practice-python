def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])

#================

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends("Barry")

#================


for number in range(2,8):
    print(number**2)

#=================

def factorial(n):
  print("Factorial called with " + str(n))
  if n < 2:
    print("Returning 1")
    return 1
  result = n * factorial(n-1)
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

factorial(4)

#========================

def sum_of_integers(n):
    if n < 1:
        return 0
    i = 1
    total = 0
    while i <= n:
        total = total + i
        i = i + 1
    return total

print(sum_of_integers(3))  # 6
print(sum_of_integers(4))  # 10
print(sum_of_integers(5))  # 15


# Initialize variables

# Start with i = 1 (the first number to add).

# Start with total = 0 (this will hold the sum).

# Set up the while loop

# Condition: i <= n (keep looping until we reach n).

# Inside the loop

# Add i to total.

# Increase i by 1 (i = i + 1).