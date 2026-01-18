numbers = range(1, 21)
evens = []
odds = []

for n in numbers:
    if n > 5:  # Boss Level condition
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)

print(f"Evens (> 5): {evens}")
print(f"Odds (> 5): {odds}")