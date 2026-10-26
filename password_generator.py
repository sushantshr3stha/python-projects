#this is a strong password generator

import secrets
import string


chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation

def get_password(pass_len):
    password =""
    for _ in range(pass_len):
        password += secrets.choice(chars)

    return password

while True:
        try:
            pass_len = int(input("enter the length of the password: "))       
        except ValueError:
            print("You can only enter numbers ")
            continue
        if pass_len>=8 and pass_len<= 24:   
            break
        else:
            print("The password length must be greater or equal to eight and lesser than 24")
password = get_password(pass_len)
print(password)