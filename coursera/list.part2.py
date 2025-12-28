#manuplation of the list using operation 
# a = [ " 3 ", "4" , "5 "]
# b = [ " 2 ", "1" , "5 "]
# c = a + b 
# print(c)

a = [  3 , 4 , 5 ]
b = [  2 , 1 , 5 ]
c = a + b 
print(c)
print(a)
print(b)

# slicing in the string of ist 

#normal slicing 

name = "numaan"
print(name[0:3])
print(name[:6])
print(name[1:2])

#now we do this in list 

y = ["numaan" ," noman ", "numan "]

print(y[0:2])

my_list = [10, 20, 30, 40, 50]
sub_list = my_list[1:4]
print(sub_list)


# liat methods = append , remove , count , extend , inder , insert , pop , reverse , sort ***

#now we use append method 

item = list()
print(item)
item.append("hero")
print(item)
item.append("king ,queen")
print(item)
item.append(99)
print(item)

#example 
my_list = ['apple', 'banana', 'cherry']
my_list.append('date')
print(my_list)

#now like true and false some in the list question 

some = [4 , 5 , 6 , 7, 8, 9]
print(9 in some)
print(10 in some)
print(25 in some)
print(20 not in some)

# sorting system in the list 

letters = [ "c", "b", "a"]
letters.sort()
print(letters)

numbers = [ 1, 3, 4 , 5, 6, 2 ]
numbers.sort()
print(numbers)
#*****************go to next part countinue from there 