list = ['apple', 'chestnut', 'gargoyle', 'pandas', 'sheep', 'raptor']

def longest_word():
    lengthval = 0
    longword = ""
    for i in list:
        if len(i) > lengthval:
            lengthval = len(i)
            longword = i
        elif len(i) == lengthval:
            longword = longword + ", " + i
    return longword

print(longest_word())
