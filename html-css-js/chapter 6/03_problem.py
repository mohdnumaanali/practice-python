p1 = "make a lot of money "
p2 = "buy now "
p3 = "subscribe this "
p4 = "click this "

message = input("enter a commet : ")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this comment is spam")

else:
    print("this commet is not a spam")


#this program has a problem solve this when you have free time
