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


#---------------------------------------------------------------
print("The allotted marks are in range between 0.0 to 10.0")

try :
    # 1. Use float so 9.5 works!
    student_marks = float(input("what is your secured score : "))
    
    # 2. First, check if the number is even possible (Range check)
    if student_marks > 10.0 or student_marks < 0.0:
        print("Error: Score is out of range (0.0 - 10.0)")
        
    # 3. Now do the grading logic
    elif student_marks >= 9.0 :
        print("A grade") 
    elif student_marks >= 8.0 :
        print("B grade")
    elif student_marks >= 7.0 :
        print("C grade")
    elif student_marks >= 6.0 :
        print("D grade")
    else :
        print("F grade")

except:
    print("Error: Invalid entry... please enter a number only.")