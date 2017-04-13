from tkinter import *

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