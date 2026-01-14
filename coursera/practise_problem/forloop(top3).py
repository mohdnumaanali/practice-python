data = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]
unique_data = []

for item in data:
    if item not in unique_data:
        unique_data.append(item)

print(f"Original: {data}")
print(f"Cleaned:  {unique_data}")