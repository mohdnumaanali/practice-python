# with open("noman.txt", "w") as file:
#     file.write("It was a dark and stormy night")
# file.close()
# print(file)
file = open("noman.txt")
with open("noman.txt", "r+") as file:
    file.write("It was a dark and stormy nigh---------t")
    print(file)
file.close()
print(file)