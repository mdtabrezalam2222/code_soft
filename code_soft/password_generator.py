import random
import string
print("Welcome To Our Password Generator")
t='yes'
while t=='yes':
    symbols = ['!','@','#','$','$','%','&','*','_','-','+','=','|','/']
    lower_char  = string.ascii_lowercase
    upper_char = string.ascii_uppercase
    upperCase= int(input('enter the number of upper_case letter you want in password = '))
    lowerCase= int(input('enter the number of lower_case letter you want in password = '))
    n_symbols= int(input('how many symbols you want in password = '))
    password = ""
    for i in range(upperCase):
        password=  password+random.choice(upper_char)
    for i in range(upperCase):
        password =password +random.choice(lower_char)
    for i in range(n_symbols):
        password = password + random.choice(symbols)
    p = list(password)
    random.shuffle(p)
    str = ""
    for i in p:
        str = str+i
    print(str)
    t=input("Enter'yes' if you want to generate more password = ")