def even_numbers(maximum):

    return_string = ""  # Initializes variable as a string

    # Loop through even numbers from 2 up to and including maximum
    for number in range(2, maximum + 1, 2): 
        # Append the even number followed by a space
        return_string += str(number) + " "

    # Remove the final space at the end
    return return_string.strip() 

print(even_numbers(6))   # 2 4 6
print(even_numbers(10))  # 2 4 6 8 10
print(even_numbers(1))   # (empty string)
print(even_numbers(3))   # 2
print(even_numbers(0))   # (empty string)
