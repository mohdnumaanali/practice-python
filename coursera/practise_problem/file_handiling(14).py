import re

def parse_sentences(sentence):
    pattern = r'\w+[\!\?\.]?|[^\s\w]'
    result = re.findall(pattern, sentence)
    return result

# Test cases
print(parse_sentences("Hello! How are you doing?"))  
# ['Hello!', 'How', 'are', 'you', 'doing?']

print(parse_sentences("what a beautiful day it is"))  
# ['what', 'a', 'beautiful', 'day', 'it', 'is']

print(parse_sentences("2 + 2 is definitely 4!"))  
# ['2', '+', '2', 'is', 'definitely', '4!']
