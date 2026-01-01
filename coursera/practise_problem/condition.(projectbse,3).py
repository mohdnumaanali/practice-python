try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = num1 / num2
    
    if result > 100:
        print("Wow, that's a huge result:", result)
    else:
        print("The result is:", result)

except ZeroDivisionError:
    # This specifically catches dividing by zero
    print("Error: You can't divide by zero!")
except ValueError:
    # This specifically catches if they type "hello"
    print("Error: You must enter a number!")
except:
    # This catches anything else we forgot
    print("Something else went wrong.")