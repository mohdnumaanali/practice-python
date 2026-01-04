n = 2
while n <= 20:
    print(n)
    n += 2  # Skip the odd numbers entirely by jumping by 2

# another method ****

n = 0
while n < 20:
    n += 1
    if n % 2 != 0:  # This check means "If the number is odd"
        continue    # SKIP the print line below
    print(n)