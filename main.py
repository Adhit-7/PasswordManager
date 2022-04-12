import getpass
from newpass import  newpasswd
from viewpass import showpw

def menu():
    user_input = int(input('''Enter:\n1--> To create a new password!\n2--> To view all passwords!\n3--> To edit the program!\n100 --> To quit the program!\n>'''))
    if(user_input == 1):
        newpasswd()
    elif(user_input == 2):
        showpw()
    elif(user_input == 100):
        exit()
    else:
        print("Invaid output; Program is exiting!")


while True:
    menu()