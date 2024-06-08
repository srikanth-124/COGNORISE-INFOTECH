import random
import string
print("welcome to password generator")

length=int(input("enter the desired length of the password:"))

want_letters=int(input("how many letters do you want in your password?"))
want_symbols=int(input("how many symbols do you want in your password?"))
want_numbers=int(input("how many numbers do you want in your password?"))

if  want_letters+want_symbols+want_numbers!=length:
    print("The sum of letters,Symbols and numbers doesn't match the total length of the password")
    exit()

want_password=[]

letters_list=list(string.ascii_lowercase)
for i in range(want_letters):
    selected_letters=random.choice(letters_list)
    want_password.append(selected_letters)

Symbols_list=list(string.punctuation)
for i in range(want_symbols):
    selected_symbols=random.choice(Symbols_list)
    want_password.append(selected_symbols)
numbers_ist=list(str(num) for num in range(10))

for i in range(want_numbers):
    selected_numbers=random.choice(numbers_ist)
    want_password.append(selected_numbers)
    
random.shuffle(want_password)
for i in range(len(want_password)):
    print(want_password[i],end="")