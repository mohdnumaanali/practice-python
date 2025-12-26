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



fhand = open('mbox.txt')
x = 0
for line in fhand:
       x = x + 1
print(x)