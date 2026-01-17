#List Total: Write a function sum_list(my_list) that takes a list of numbers and returns the total sum of all numbers in that list. 
# (Use a for loop inside the function).
def sum_list (my_list):
    total = 0
    for num in my_list:
        total+=num
    return total
number = [9,9,9,9,1,1,1,1]
print(sum_list(number))