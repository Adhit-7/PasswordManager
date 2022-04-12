import os
from flask import Flask, render_template
import mysql.connector
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys  # Automate insert id, pword
from time import sleep

PATH = os.path.join(os.getcwd(), 'driver', 'geckodriver.exe')

app = Flask(__name__, template_folder='./template') #  Flask : class 

mydb  = mysql.connector.connect( user = 'root', password = '', host = "127.0.0.1", database = "PasswordManager") 

@app.route('/',methods=['GET']) # routing using get method
def index():
    cursor = mydb.cursor()
    cursor.execute("""SELECT id, Site, Email, Password FROM Credentials""")
    data = cursor.fetchall() 
    return render_template('index.html',data=data) 

@app.route('/open/<int:id>', methods=['POST']) # routing using push method, 
def open_website(id):
    
    cursor = mydb.cursor()
    cursor.execute(f"""SELECT Site, Email, Password FROM Credentials WHERE id = {id};""")
    data = cursor.fetchall()
    
    print(data)

    if data:
        browser = Firefox(executable_path=PATH)
        
        if 'facebook' in data[0][0]:  

            browser.get('https://www.facebook.com')

            email_field = browser.find_element_by_id('email')  
            email_field.send_keys(data[0][1])

            pass_field = browser.find_element_by_id('pass')
            pass_field.send_keys(data[0][2])

        elif 'mail' in data[0][0] or 'youtube' in data[0][0] or 'twitter' in data[0][0]:

            browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3D%252F&hl=en&passive=false&service=youtube&uilel=0&flowName=GlifWebSignIn&flowEntry=AddSession')

            sleep(2)

            email_field = browser.find_element_by_id('identifierId')
            email_field.send_keys(data[0][1])
            
            email_field.send_keys(Keys.ENTER)

            sleep(2)

            pass_field = browser.find_element_by_css_selector('input[type="password"]')
            pass_field.send_keys(data[0][2])
            
            pass_field.send_keys(Keys.ENTER) 
            
            if 'youtube' in data[0][0]:
                
                browser.get('https://www.youtube.com')

            if 'twitter' in data[0][0]:

                browser.get('https://www.twitter.com')
                
        elif 'instagram' in data[0][0]:  

            browser.get('https://www.instagram.com')

            email_field = browser.find_element_by_class_name('pexuQ')  
            email_field.send_keys(data[0][1])

            pass_field = browser.find_element_by_class_name('pexuQ')
            pass_field.send_keys(data[0][2])

        else :

            return "Website not supported yet"


    return "Invalid Data"
        

if __name__ == "__main__":
    app.run(debug=True, port=8080)