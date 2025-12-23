# # List of numbers
# numbers = [9, 41, 12, 3, 74, 15]

# # Initialize the counter
# count = 0

# # Loop through each number in the list
# for number in numbers:
#     count += 1  # Increment the counter for each number

# # Print the total count
# print("Total count:", count)

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)