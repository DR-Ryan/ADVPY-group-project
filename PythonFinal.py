from tkinter import *
import sqlite3

def setusername(username, password):
	connect = sqlite3.connect('FractionSolver.db')
	login_info = connect.cursor()
	login_info.execute('''CREATE TABLE login (username text, password text)''') #comment out after first run
	login_info.execute('''INSERT INTO login (username, password) VALUES(?,?)''', (username, password))
	login_info.commit()
	login_info.close()

#Create table to store grocery information
#login_info.execute('''CREATE TABLE login (user_name text not null, password text not null)''') #comment out after first run

def getsusers():
	connect = sqlite3.connect('FractionSolver.db')
	login_info = connect.cursor()
	login_info.execute('''SELECT username, password FROM login''')
	users = login_info.fetchall()
	connect.close()
	return users

def getusername():
    text = TextEntry.get()
    password = TextEntry2.get()
    text= text.upper()

    if text=="BOB" and password=="pass":
        lbl2.config(text="Access Granted")
    else:
        lbl2.config(text="Access Denied")


window = Tk()
window.geometry("200x175")
window.title("Finale")
# Set window color to light blue
window.configure(background='#DEEFF5')

lbl = Label(window, text="Enter your username")
# Set label color to light blue
lbl.configure(background='#DEEFF5')
lbl.pack()
# Make text entry box for username
TextEntry = Entry(window, bd=5)
TextEntry.pack()

lbl3 = Label(window, text = "Enter your password")
# Set password color to light blue
lbl3.configure(background='#DEEFF5')
lbl3.pack()
# Make text entry box for password
TextEntry2 = Entry(window, bd=5)
TextEntry2.pack()

button = Button(window, text="Submit", command=getusername)
button.pack()
lbl2 = Label(window, text="")
# Set label color to light blue
lbl2.configure(background="#DEEFF5")
lbl2.pack()

window.mainloop()