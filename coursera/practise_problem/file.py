try:
    # We try to open a file that probably isn't there
    fhand = open("my_secret_data.txt")
    print("File found! Reading contents...")
except:
    # If the file is missing, this runs instead of crashing
    print("File not found! Please check the filename and try again.")

print("Program continues to run...")