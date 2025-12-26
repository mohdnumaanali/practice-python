# Normal Python code (VS Code / Notepad)

a = [2, 4, 3]   # represents 342
b = [5, 6, 4]   # represents 465

carry = 0
result = []

for i in range(len(a)):
    total = a[i] + b[i] + carry
    carry = total // 10
    result.append(total % 10)

if carry:
    result.append(carry)

print("Result:", result)
