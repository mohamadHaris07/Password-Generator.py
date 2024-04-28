import random
import string

def generate_password(length, uppercase, lowercase, numbers, symbols):
    caharacters = ''
    if uppercase:
        caharacters += string.ascii_uppercase
    if lowercase:
        caharacters += string.ascii_lowercase   
    if numbers:
        caharacters += string.digits
    if symbols:
        caharacters += string.punctuation  
        
    if not caharacters:
        print("error")        
        
    password = ''.join(random.choice(caharacters) for ln in range(length))
    return password       




length = int(input("enter the password length: "))
uppercase = input('include uppercase yes/no').lower() == 'yes'
lowercase = input('include lowercase yes/no').lower() == 'yes'
numbers = input('include number yes/no').lower() == 'yes'
symbols = input('include symbole yes/no').lower() == 'yes'



password = generate_password(length, uppercase, lowercase, numbers, symbols)


print(password)