file = open("noman.txt")
for line in file:
    print(line.upper().strip())
file.close()