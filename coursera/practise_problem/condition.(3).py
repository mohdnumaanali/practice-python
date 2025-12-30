hour = int(input("what is the time now : "))
if hour < 14 :
    print(" it is morning ")
elif hour < 18 :
    print("this is after noon ")
else:
    print(" this is evening ")


#----------------------------------------------------------------------------------

raw_hour = input("what is the time now : ")

try:
    hour = int(raw_hour) # Try to convert to number
    
    if hour < 12:
        print("it is morning")
    elif hour < 18:
        print("this is afternoon")
    else:
        print("this is evening")
except:
    print("Error: Please enter the time as a number (e.g., 14)")