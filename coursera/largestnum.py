# Initialize the variable to store the largest number
largest_so_far = -1                                                #yaha konsa number hona marzi humara set me 74 bada toh 0-73 aya toh bhi wo answer 74 dekatah .... par tuu agar 74 se bada number leka toh teku wo bada number ata change kar ke deklee ree tu

# List of numbers to iterate through
numbers = [9, 41, 12, 3, 74, 15]                                   #numaan tera doubt hai na largesst so far hai kiya .... yai humloga ich diye so zada confuse maat hoo aur blue color mai jo bhi wo purai humlooga diye so ich

# Loop through each number in the list
for the_num in numbers:
    # Check if the current number is greater than the largest number found so far
    if the_num > largest_so_far:
        largest_so_far = the_num  # Update the largest number

# Print the largest number found
print("The largest number is:", largest_so_far)