def power(base, exponent=2):
    return base ** exponent

# Scenario 1: Providing both numbers
print(power(10, 3))  # 10 to the power of 3 = 1000

# Scenario 2: Providing ONLY the base
print(power(10))     # Since exponent is missing, it uses 2. Output: 100