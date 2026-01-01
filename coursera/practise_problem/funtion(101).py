def computepay(hours, rate):
    # THE HARD MATH IS HIDDEN IN HERE
    if hours > 40:
        return (40 * rate) + (hours - 40) * (rate * 1.5)
    else:
        return hours * rate

# Now, look how clean the rest of your code is:
print(computepay(45, 10))
print(computepay(30, 15))
print(computepay(60, 20))
print(computepay(30, 45)) 

