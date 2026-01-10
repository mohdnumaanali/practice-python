# The third number in range (2) is the 'step'
for i in range(0, 21, 2):
    print(i)

word = "nnnnnnn"
# enumerate gives us both the index (i) and the letter (char)
for i, char in enumerate(word):
    print(f"{i}: {char}")