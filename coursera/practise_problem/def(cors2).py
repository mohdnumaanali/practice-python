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