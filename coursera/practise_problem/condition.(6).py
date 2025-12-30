# score_input = input("what is your marks = ")
# score = float(score_input)

# try :
#     if score >= 45 :
#         print("pass")
#     else:
#         print("fail")
# except :
#     print("error ")

score_input = input("Enter your score: ")

try:
    # 1. Try to convert the text to a decimal number
    score = float(score_input)
    
    # 2. If the conversion works, run the logic
    if score >= 40:
        print("Pass")
    else:
        print("Fail")
        
except:
    # 3. If the user typed "abc" instead of a number, this runs
    print("Error: Please enter a number for the score.")