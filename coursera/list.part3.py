num = [ 1,2,3,4,5,6,7,8,9,10]
print(len(num))

print(max(num))

print(min(num))

print(sum(num))

print(sum(num)/len(num))


# list and string relation and converting string into list 

sentence = "hey this me numaan ali "
result=sentence.split()
print(result)
print(len(result)) , print(result[0])

#loops with this string result 

for w in result :
    print(w)

# for example u have special character between this space not including space  

fruit = "apple;grape;banan"
ans = fruit.split(";")                                         # ( ) iske andar kiya dalna mlum hua na 
print(ans)


#example
data = 'name:John Doe;age:30'
first_split = data.split(';')
second_split = first_split[0].split(':')
print(second_split)

#example for list loops 

words = ['cat', 'dog', 'bird']
for word in words:
    print(word.upper())

#example 2

text = 'Python is awesome'
result = text.split()
print(result)


# Open the file romeo.txt and read it line by line
fname = input("Enter file name: ")
fh = open(fname)

lst = list()  # empty list to store unique words

for line in fh:
    words = line.split()  # split line into words
    for word in words:
        if word not in lst:   # check if word already exists
            lst.append(word)  # add new word

lst.sort()  # sort the list alphabetically
print(lst)
