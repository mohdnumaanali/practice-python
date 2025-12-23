#def hai isme 
#max and minimum aya 
#abb return ------------------funtion hai jo stop ya end bhi karta
def addtwo (a , b ):
    added = a + b 
    return added 
x = addtwo(2 ,2)
print(x)

#--------------------------------------------------------------------------------------

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')

#------------------------------------------------------------------------------------------

def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)

#-------------------------------------------------------------------------------------------------------

def computepay(h, r):
    if h > 40:
        reg = 40 * r
        otp = (h - 40) * r * 1.5
        pay = reg + otp
    else:
        pay = h * r
    return pay

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
p = computepay(hrs, rate)
print("Pay", p)

#------------------------------------------------------------------------------