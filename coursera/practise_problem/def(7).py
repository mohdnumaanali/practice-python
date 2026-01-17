#The Max Finder: Write a function find_max(a, b) that takes two numbers and returns the one that is larger.
#  (Use an if statement inside).

def find_max(a,b):
    if a > b :
        return a
    else :
        return b
big = find_max(9,6)
print(f"the larger one is {big}")
