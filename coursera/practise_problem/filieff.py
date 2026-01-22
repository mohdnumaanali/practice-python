import os
print("Current working directory:", os.getcwd())
file = open("noman.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()
with open("noman.txt") as file:
    print(file.readline())