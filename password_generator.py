#this is a basic password generator

import random
import string


chars = string.ascii_lowercase + string.digits + string.ascii_uppercase
pass_len = int(input("enter the length of the password: "))
char = 0
password =""

for _ in range(pass_len):
    password += random.choice(chars)

print(password)