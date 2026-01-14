letter= '''dear <|name|>
        you are selected !
        <|date|>
'''
print(letter.replace("<|name|>","numaan").replace("<|date|>","24 december 2006"))