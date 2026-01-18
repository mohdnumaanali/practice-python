sentence = input("Type a sentence: ").lower()
vowels = "aeiou"
v_count = 0
s_count = 0

for char in sentence:
    if char in vowels:
        v_count += 1
    elif char == " ":
        s_count += 1

print(f"Vowels found: {v_count}")
print(f"Spaces found: {s_count}")