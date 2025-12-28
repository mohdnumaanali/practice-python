# now we are going to learn about dictonory { }

dict_example = {'fruit': 'apple', 'vegetable': 'carrot'}
print(dict_example['vegetable'])

# ex 2
dict_example = {'a': 1, 'b': 2, 'c': 3}
print(list(dict_example.keys()))

# count 
# Creating a histogram using a dictionary
sample_data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
histogram = {}
for fruit in sample_data:
    if fruit in histogram:
        histogram[fruit] += 1
    else:
        histogram[fruit] = 1
print(histogram) 

# my code 
city = ["hyderbad", "warangal ", "hyderbad", "warangal","hyderabad","siddipet"]
output = {}
for place in city :
    place = place.strip()
    if place in output :
        output[place] += 1
    else :
        output[place] = 1 
print(output)


# example 3
dictionary = {'a': 5, 'b': 7, 'c': 2}
max_value = None
for value in dictionary.values():
    if max_value is None or value > max_value:
        max_value = value
print(max_value)


#ex

name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)
counts = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

# Find the most frequent sender
bigcount = None
bigemail = None
for email, count in counts.items():
    if bigcount is None or count > bigcount:
        bigemail = email
        bigcount = count

print(bigemail, bigcount)

#_____________________________________________________________

# 10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for each of the messages.

name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

counts = dict()

for line in handle:
    if line.startswith("From "):   # only lines starting with 'From '
        parts = line.split()
        time = parts[5]            # the time field (hh:mm:ss)
        hour = time.split(":")[0]  # extract hour
        counts[hour] = counts.get(hour, 0) + 1

# sort by hour and print
for k, v in sorted(counts.items()):
    print(k, v)


#hum yai bhi kar saktai hai dictionorey me 

counts["11"] = 6      # add new key
counts["09"] = 5      # update value
del counts["10"]      # delete key

