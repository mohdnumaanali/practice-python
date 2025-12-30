try:
    print("Step 1: I am starting the program.")
    
    # This line is impossible (Math Error)
    result = 10 / 0 
    
    # This line comes AFTER the error
    print("Step 2: Success!") 

except:
    print("Step 3: An error happened, so I jumped here!")

print("Step 4: The program is finished.")