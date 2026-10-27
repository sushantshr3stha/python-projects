#a hangman game

import secrets
words = ["python", "laptop", "keyboard", "internet", "program", "variable",
         "function", "network", "monitor", "software"]
blank = ["_"]
guessed_letter = []
user_lives = 10

guessing_word = secrets.choice(words)
blanks = blank * len(guessing_word)
print("".join(blanks))
print(guessing_word)


user_input = input("Try to guess a letter").lower()
if user_input in guessing_word and len(user_input)==1:
    print("You got one write")
else:
    print("You got it wrong")

for  i, ch in enumerate(guessing_word):
    print(i,ch)