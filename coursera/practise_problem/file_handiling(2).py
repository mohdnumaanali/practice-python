import os

def new_directory(directory, filename):
    if not os.path.isdir(directory):
        os.mkdir(directory)
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as file:
        pass
    return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))
