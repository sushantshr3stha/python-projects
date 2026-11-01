import random


num = random.randint(1,50)
print(num)
while True:
    user_input = int(input("Guess the number:(1-50) "))
    if user_input==num:
        print("Congrats! You guessed it correctly\n")
        break
    else:
        continue