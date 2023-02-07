import random 
import time

word_list = ['candy', 'boat', 'feel', 'salt', 'pepper', 'enigmatic', 'solar', 'tomato', 'fruit', 'oranges', 'bottle', 'coding', 'llama', 'lampshade', 'astronaut', 'luggage', 'mississippi', 'revolutionary', 'xylophone', 'porcelain', 'groovy', 'dog', 'cat', 'penguin', 'parrot', 'agregious', 'apparatus', 'argument', 'extraneous', ]
word_display = []
alphabet = []
index_list = []
tries_count = 7
count = 0

secret_word = random.choice(word_list)

for i in range(len(secret_word)):                             #creates display for word
  word_display.append("__")

while tries_count > 0:
  
  if "__" not in word_display:
    print("You got it! The word is " + secret_word + "!")     #checks to see if all the letters in the display are filled
    break
  letter = input("Guess a Letter: ")
  if letter not in alphabet:
    alphabet.append(letter)                                   #adds guessed letter into list of guessed letters
  elif letter in alphabet:
    print("You literally have the list of letters left why did you guess it twice.")
  print(f"These are the letters you've guessed: {alphabet}")
  time.sleep(1)
  if secret_word.count(letter) == 1:                          #code for guessing one of the letters and filling it into the display
    letter_place = secret_word.index(letter)
    word_display[letter_place] = letter
    print("You guessed one of the letters!")
    print("Number of tries left: " + str(tries_count - 1))
    print(word_display)
    print(" ")

  elif secret_word.count(letter) >= 2:                        #code for if there are multiple of one letter in the display
    count = 0
    index_list = []
    for i in secret_word:
      if i == letter:
        index_list.append(secret_word.index(i, count))
        count = index_list[-1] + 1
    print(index_list)
    for x in index_list:
      word_display[x] = letter
    print("You guessed one of the letters!")
    if tries_count > 0: 
      print("Number of tries left: " + str(tries_count - 1))
    print(word_display)
    print(" ")

  elif letter not in secret_word:                             #code for if the wrong letter is guessed
    print("The letter you picked is not in the word!")
    tries_count -= 1
    print("Number of tries left: " + str(tries_count - 1))
    print(word_display)
    print(" ")
    if tries_count == 0:
      print("The game is over, you hanged the man!")
      print("The secret word was: " + secret_word)
      break


#With this refresher, I was able to remember most of the stuff I learned regarding Python, except for dictionaries and OOP. Used basically every loop and alot of built in functions