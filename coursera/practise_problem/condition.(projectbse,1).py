print("The alloted marks are in range between 0.0 to 10.0")
try :
    student_marks = int(input("what is your secured score : "))
    if student_marks >= 10 :
        print("A grade") 
    elif student_marks >= 9 :
        print("B grade")
    elif student_marks >= 8 :
        print("C grade ")
    elif student_marks >= 7 :
        print("D grade ")
    elif student_marks >= 6 :
        print("E grade ")
    else :
        print("F grade")
except:
    print("error invalid entry ... give only number ")
