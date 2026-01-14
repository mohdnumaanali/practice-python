for n in range(1, 31):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)




# 1. Convert input to an integer
user_limit = int(input("Give a number to count up to: "))

# 2. Use a different name (i) for the loop variable
# We use range(1, user_limit + 1) to include the actual number you typed
for i in range(1, user_limit + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
