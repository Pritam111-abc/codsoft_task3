import random
import string

length = int(input("Enter password length: "))

char = string.ascii_letters + string.digits + string.punctuation

#string.ascii_letters = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#string.digits = 0123456789
#string.punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

password = ""

for i in range(length):
    password += random.choice(char)

print("Your Generated Password is :", password)