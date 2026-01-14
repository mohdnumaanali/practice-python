print("Prime numbers between 2 and 50:")

for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break # No need to keep checking if we found a divisor
    
    if is_prime:
        print(num, end=" ")