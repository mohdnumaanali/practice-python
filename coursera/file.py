#files system hai -----------------/n , open -------------file matlab read and write 

file = open('example.txt', 'w')
file.write('Hello, World!')
file.close()
file = open('example.txt', 'r')
output = file.read()
file.close()
print(output)

#oops

file_content = 'Hello\nWorld\n'
stripped_content = file_content.rstrip()
print(stripped_content)

#----------------------------------

try:
    f = open('non_existent_file.txt', 'r')
except IOError:
    print('File not found error')

#=======================================================================

fhand = open('mbox.txt')
x = 0
for line in fhand:
       x = x + 1
print(x)

#===========================================================================

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()   # remove trailing newline
    print(line.upper())    # convert to uppercase
#------------------------------------------------------------------------------------------

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
total = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # Extract the number after the colon
    value = float(line.split(":")[1].strip())
    count = count + 1
    total = total + value

average = total / count
print("Average spam confidence:", average)
