import getpass
from select import select
import mysql.connector

def newpasswd():
    print("You have chosen to create a new password!")
    name_of_site = input("Enter the name of the website! ")
    email = input("Enter the email associcated with the account! ")


    passwd = getpass.getpass("Enter the password! ") 
    conf_passwd = getpass.getpass("Enter your password again! ")

    while passwd != conf_passwd:
        print("The password you entered is incorret!\nPlease enter it again!")
        passwd = getpass.getpass("Enter the password! ") 
        conf_passwd = getpass.getpass("Enter your password again! ")

    print("Your infos are; Site name: ",name_of_site," Email associated: ",email)
    conf = input("If all the credentials match press Y; If not press N!")
    confirmation = conf.upper()
    if (confirmation == "Y") or (confirmation == "y"):
        print("Processing Data!")

    while (confirmation == "N") or (confirmation == "n"):
        name_of_site = input("Enter the name of the website! ")
        email = input("Enter the email associcated with the account! ")
        passwd = getpass.getpass("Enter the password! ") 
        conf_passwd = getpass.getpass("Enter your password again! ")

        while passwd != conf_passwd:
            print("The password you entered is incorret!\nPlease enter it again!")
            passwd = getpass.getpass("Enter the password! ") 
            conf_passwd = getpass.getpass("Enter your password again! ")

        print("Your infos are; Site name:",name_of_site," Email associated:",email)
        conf = input("If all the credentials match press Y; If not press N!")
        confirmation = conf.upper()
        if (confirmation == "Y") or (confirmation == "y"):
            print("Processing Data!")  
    database(name_of_site, email, conf_passwd)


def database(name_of_site, email, conf_passwd):
    mydb  = mysql.connector.connect( user = 'root', password = '', host = "localhost", database = "PasswordManager")
    cursor = mydb.cursor() # helps to connect mysql
    sql = "INSERT INTO Credentials(Site, Email, Password) VALUES (%s, %s, %s)"
    val = (name_of_site, email, conf_passwd)
    cursor.execute(sql, val)
    mydb.commit()
    print("Your credentials have now been saved to database.")
    print("------------------------------------------")
    




