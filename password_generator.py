import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqystuvwxyz0123456789@#$&._"
pass_len = int(input("how long password do you want(8-32 characters): "))

for char in chars:
    
    password = random.choice(chars)
print(password)