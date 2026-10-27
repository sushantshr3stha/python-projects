#a hangman game

import secrets
words = ["python", "laptop", "keyboard", "internet", "program", "variable",
         "function", "network", "monitor", "software"]
blank = ["_"]
guessed_letter = []
user_lives = 10

guessing_word = secrets.choice(words)
blanks = blank * len(guessing_word)
print("  ".join(blanks))
print(guessing_word)


user_input = input("Try to guess a letter: ").lower()
if user_input in guessing_word and len(user_input)==1 and user_input.isalpha():
    for  i, ch in enumerate(guessing_word):
        if ch == user_input:
            blanks[i] = ch
            print("  ".join(blanks))
            break
    print("You got one right")
elif not (user_input in guessing_word) and len(user_input) == 1:
    print("You entered wrong letter")
else:
    print("you must enter only one value which must be a letter")

