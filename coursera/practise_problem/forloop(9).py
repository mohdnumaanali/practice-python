sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
result = ""

for char in sentence:
    if char in vowels:
        continue # Skip the rest of the loop for this character
    result += char
print(result)