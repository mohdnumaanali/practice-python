# The outer loop handles the rows
for row in range(3):
    # The inner loop handles the stars in that row
    for col in range(3):
        print("*", end=" ") # end=" " keeps stars on the same line
    print() # Moves to the next line after 3 stars

# This uses string multiplication—a very cool Python feature!
for i in range(1, 6):
    print("*" * i)