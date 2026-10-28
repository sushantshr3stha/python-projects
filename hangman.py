#a simple hangman game

import secrets
words = ["python", "laptop", "keyboard", "internet", "program", "variable",
         "function", "network", "monitor", "software" , "graphics"]
guessed_letter=0
user_lives = 10
letters = []
guessing_word = secrets.choice(words).lower()
blanks = ["_"] * len(guessing_word)
print("  ".join(blanks))
print(guessing_word)

while True:
    if guessing_word != "".join(blanks):
        user_input = input("Try to guess a letter: \n").lower()

        if user_input in guessing_word and len(user_input)==1 and user_input.isalpha():
            for  i, ch in enumerate(guessing_word):
                if ch == user_input:
                    blanks[i] = ch
                    letters += ch
                    print("  ".join(blanks))
                    break
            print("You got one right\n")


            guessed_letter += 1
            print(f"No of Guessed letter: {guessed_letter} and Guessed letters: {letters}")

        elif not (user_input in guessing_word) and len(user_input) == 1:
            print("You entered wrong letter\n")
            user_lives -= 1
            print(f"remaining lives: {user_lives}\n")
            if user_lives == 0:
                print("You are out of lives. You Lose! :(")
                break

        else:
            print("you must enter only one value which must be a letter\n")
            choice = input("Do you want to continue? 1 for yes && 2 for no\n ")
            if choice == "1":
                continue
            elif choice == "2":
                break
            else:
                print("wrong choice")
    else:
        print("You won! :)")
        break
        


