import random
sowpods = "sowpods.txt"
word_list = []

def word_generator():
    filename = sowpods
    f = open(filename, "r", encoding = "utf8")
    words = f.readlines()
    f.close()

    return random.choice(words).strip()

for i in range(1,7):
    word_list.append(word_generator())


def longest_word():
    lengthval = 0
    longword = ""
    for i in word_list:
        if len(i) > lengthval:
            lengthval = len(i)
            longword = i
        elif len(i) == lengthval:
            longword = longword + ", " + i
    return longword

print(longest_word())
