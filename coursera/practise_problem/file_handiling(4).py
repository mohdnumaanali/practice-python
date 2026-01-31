import os

def parent_directory():
    relative_parent = os.path.join(os.getcwd(), "..")
    return os.path.abspath(relative_parent)

print(parent_directory())
