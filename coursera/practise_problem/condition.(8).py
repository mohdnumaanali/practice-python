# number = int(input(" give the number : "))
# num = number %2 == 0
# print(num)

#-----------------------------------------------------------------
# number = int(input(" give the number : "))

# if number %2 == 0 :
#     print("even")
# else :
#     print("odd")
#----------------------------------------------------------------------

try :
    number = int(input(" give the number : "))

    if number %2 == 0 :
        print("even")
    else :
        print("odd")
except:
    print("invalid entry ... check it again ")