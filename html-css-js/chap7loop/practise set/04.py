#write a program to   find the number is prime or not

n = int(input("enter a number : "))

for i in range  (2,n):
    if(n%i)==0:
        print("number is not a prime ")
        break
    else:
        print("it is a prime number ")