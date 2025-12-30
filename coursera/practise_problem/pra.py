import re

# Open your actual data file
handle = open('regex_sum_2347366')

total = 0
for line in handle:
    numbers = re.findall('[0-9]+', line)
    for num in numbers:
        total += int(num)

print(total)
