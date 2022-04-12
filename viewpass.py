import mysql.connector

def showpw():
    mydb  = mysql.connector.connect( user = 'root', password = '', host = "localhost", database = "PasswordManager") 
    cursor = mydb.cursor()
    cursor.execute("""SELECT Site, Email, Password FROM Credentials""")
    data = cursor.fetchall()
    for credentials in data:
        print("------------------------------------------")
        print("Site = ", credentials[0])
        print("Email Used = ", credentials[1])
        print("Password = ", credentials[2], "\n")
    print("------------------------------------------")