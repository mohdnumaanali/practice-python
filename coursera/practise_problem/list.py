fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

#-----------------=========================================-------------------------------------

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
print(fruits)

#------------==========================================---------------------------------------------

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
print(fruits)

#------------------------============================================---------------------------------------

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
print(fruits)

#--------------------===========================================------------------------------------------

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)
fruits[2] = "Strawberry"
print(fruits)

#---------------------==============================================--------------------------------------

x = ["Now", "we", "are", "cooking!"]
type(x)

#----------------------==================================----------------------------------

x = ["Now", "we", "are", "cooking!"]
len(x)

x = ["Now", "we", "are", "cooking!"]
"are" in x

#------------------=====================================------------------------------------

x = ["Now", "we", "are", "cooking!"]
print(x[0])
print(x[3])

#-------------------------------============================--------------------------

x = ["Now", "we", "are", "cooking!"]
x[1:3]

#----------------------------------================--------------------------end-----------========-----------
