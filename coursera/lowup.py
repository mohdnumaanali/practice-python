s1 = 'abc'
s2 = 'ABC'
result = s1.lower() == s2.lower()
print(result)                                       #yai hai humara low aur uo wala kisA 

#stip matlab space nikalna hai isme 

s = '  Hello World  '
result = s.strip()
print(result)

#yai in wala hai code understand karne  -------------------------------------------------------------------------- 

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)  

#find wale questions me acha kaam ata --------------------------------------------------------------------------
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

#aur find ----------------------------------------------------------------------------------------------------------------

text = "X-DSPAM-Confidence: 0.8475"

# Find the position of the colon
pos = text.find(':')

# Slice from just after the colon to the end
num_str = text[pos+1:].strip()

# Convert to float
num = float(num_str)

print(num)
