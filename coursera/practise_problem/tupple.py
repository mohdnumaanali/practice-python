fullname = ('Grace', 'M', 'Hopper')

print(fullname)

#-------------==================-----------------------------------

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
result = convert_seconds(5000)
type(result)

#-------------===================------------------------

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))


  #-------------------======================-----------------

  multiples = []
for x in range(1,11):
  multiples.append(x*7)

print(multiples)

#------------------====================-----------------------

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

#-------------====================------------------------

# Convert a list to a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)  # Outputs: (1, 2, 3, 4)