#a simple hangman game

import secrets
words = ["python", "laptop", "keyboard", "internet", "program", "variable",
         "function", "network", "monitor", "software" , "graphics"]
guessing_word = secrets.choice(words).lower()
blanks = ["_"] * len(guessing_word)
print("  ".join(blanks))
# print(guessing_word)
guessed = []
user_lives = 10
print(f"You have {user_lives} total lives.")
while True:
    if guessing_word != "".join(blanks):
        user_input = input("Guess the letter(Only one at a time)::").lower()

        if len(user_input)==1 and user_input.isalpha():
            
            if user_input in guessing_word and user_input in guessed:
                print("you already guessed that \n")
            elif user_input in guessing_word:
                for i, ch in enumerate(guessing_word):
                    if user_input == ch:
                        blanks[i] = ch
                print("You got one letter right")
                print(" ".join(blanks))
                guessed += user_input
            
            elif user_input not in guessing_word:
                print("Incorrect! This letter is not in the word. \n")
                user_lives -= 1
                print(f"Remaining lives: {user_lives}\n")

                if user_lives<=0:
                    print("You got out of lives. You Lose! ")
                    break
               
        elif not(len(user_input) == 1) or not(user_input.isalpha()):
            print("The input must be only one alphabetical letter.\n")
            continue

    else:
        print("You won! You got all letters correct")
        break



