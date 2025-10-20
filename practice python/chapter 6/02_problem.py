marks1 = int(input("enter marks 1 :"))
marks2 = int(input("enter marks 2 :"))
marks3 = int(input("enter marks 3 :"))


total_percentage = (100*(marks1 + marks2 + marks3 ))/300

if(total_percentage>40 ):
    print("your pass congratulation ", total_percentage)

else:
    print("your are failed try again next year !", total_percentage)

