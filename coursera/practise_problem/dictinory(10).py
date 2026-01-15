fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count_dict = {}

for f in fruits:
    if f in count_dict:
        count_dict[f] += 1 # If already there, add 1
    else:
        count_dict[f] = 1  # If first time, set to 1

print(count_dict) 
# Output: {'apple': 3, 'banana': 2, 'cherry': 1}