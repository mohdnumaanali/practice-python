file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

#--------------=====================---------------------------

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

#---------------------------================================----------------------------

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["txt"]

#---------============================-----------------------------

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
"jpg" in file_counts
"html" in file_counts
#---------------==============================----------------------------------

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["cfg"] = 8
print(file_counts)

#---------------------======================------------------------------

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
  print(extension)

#-------------------========================----------------------------------

pet_dictionary = {"dogs": ["Yorkie", "Collie", "Bulldog"], "cats": ["Persian", "Scottish Fold", "Siberian"], "rabbits": ["Angora", "Holland Lop", "Harlequin"]}  


print(pet_dictionary.get("dogs", 0))


#======================

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new_filenames.append(filename.replace("hpp", "h"))
    else:
        new_filenames.append(filename)

print(new_filenames)
# ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

#==========================

def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""
    # Iterate through each letter
    for letter in input_string.lower():
        if letter != " ":
            new_string = new_string + letter
            reverse_string = letter + reverse_string
    # Compare
    if new_string == reverse_string:
        return True
    return False

print(is_palindrome("Never Odd or Even"))  # True
print(is_palindrome("abc"))                # False
print(is_palindrome("kayak"))              # True


#====================


def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return user_groups

print(groups_per_user({
    "local": ["admin", "userA"],
    "public": ["admin", "userB"],
    "administrator": ["admin"]
}))
# {'admin': ['local', 'public', 'administrator'], 'userA': ['local'], 'userB': ['public']}
