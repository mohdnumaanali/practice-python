import os
import csv

def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

def contents_of_file(filename):
    return_string = ""
    create_file(filename)

    # Open the file
    with open(filename) as file:
        rows = csv.reader(file)
        # Skip header
        next(rows)
        # Process each row
        for row in rows:
            name, color, type_flower = row
            return_string += "a {} {} is {}\n".format(color, name, type_flower)
    return return_string

print(contents_of_file("flowers.csv"))
