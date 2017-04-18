import bcrypt
import fractions
import operator
import re
from tkinter import *



'''def getusername():
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

window.mainloop()'''

class FractionsHelper:

    def __init__(self, parent_):

        self.username = ""
        self.password = ""
        self.parent = parent_;

        self.container = Frame(parent_)
        self.container.pack()

        self.question = Label(self.container, text="Login Screen")
        self.question.pack(expand=True, pady=(0, 20))

        Label(self.container, text="Username").pack()
        self.username = Entry(self.container, width=20)
        self.username.pack()
        Label(self.container, text="Password").pack()
        self.password = Entry(self.container, width=20, show="*")
        self.password.pack()

        self.loginButton = Button(self.container, text="Sign in")
        self.loginButton.pack(pady=(20, 10))
        self.loginButton.bind("<Button-1>", self.login_attempt)

        self.createButton = Button(self.container, text="New User")
        self.createButton.pack(pady=10)
        self.createButton.bind("<Button-1>", self.create_attempt)

    def signIn(self, username, password):
        #requires database stuff
        return True

    #def  new_user(self, username, password):
    #requires database stuff


    def login_attempt(self, click):
        #requires database stuff

        attempt = self.signIn(self.username.get(),self.password.get())

        self.menu(self)

    def create_attempt(self, click):

        print("attempting to create account...")
        attempt = self.newUser(self.username.get(), self.password.get())

    def menu(self, click):

        try:
            self.math.destroy()
        except Exception:
            pass


        self.container.destroy()
        self.parent.minsize(width=625, height=400)
        self.container1 = Frame(self.parent, width=625, height=400, background="blue")
        self.container1.pack()

        self.menuText = Text(self.container1)
        self.menuText.pack(anchor=CENTER, fill=Y)
        self.statement = "Fractions Helper Main Menu. \n"
        self.menuText.insert(INSERT, self.statement)
        self.menuText.config(state=DISABLED)

        self.solverButton = Button(self.container1, text="Solver")
        self.solverButton.pack(side=LEFT, padx=(0, 100))
        self.solverButton.bind("<Button-1>", self.solver)

        self.quizzerButton = Button(self.container1, text="Quizzer")
        self.quizzerButton.pack(side=LEFT, padx=(0, 100))
        self.quizzerButton.bind("<Button-1>", self.quizzer)

        self.resultsButton = Button(self.container1, text="Results")
        self.resultsButton.pack(side=LEFT, padx=(0, 100))
        self.resultsButton.bind("<Button-1>", self.results)

    def solver(self, click):
        self.container.destroy()
        self.container1.destroy()

        try:
            self.math.destroy()
        except Exception:
            pass


        self.parent.minsize(width=625, height=400)
        self.math = Frame(self.parent, width=625, height=400, background="red")
        self.math.pack()
        self.text = Text(self.math, height=20, width=20, background="red")
        self.text.pack()
        self.statement = "Solver"
        self.text.insert(INSERT, self.statement)
        self.text.config(state=DISABLED)

        self.menuButton = Button(self.math, text="Menu")
        self.menuButton.pack()
        self.menuButton.bind("<Button-1>", self.menu)

    def quizzer(self, click):
        self.container.destroy()
        self.container1.destroy()

        try:
            self.math.destroy()
        except Exception:
            pass


        self.parent.minsize(width=625, height=400)
        self.math = Frame(self.parent, width=625, height=400, background="green")
        self.math.pack()
        self.text = Text(self.math, height=20, width=20, background="green")
        self.text.pack()
        self.statement = "Quizzer"
        self.text.insert(INSERT, self.statement)
        self.text.config(state=DISABLED)

        self.menuButton = Button(self.math, text="Menu")
        self.menuButton.pack()
        self.menuButton.bind("<Button-1>", self.menu)

    def results(self, click):
        self.container.destroy()
        self.container1.destroy()

        try:
            self.math.destroy()
        except Exception:
            pass

        self.parent.minsize(width=625, height=400)
        self.math = Frame(self.parent, width=625, height=400, background="brown")
        self.math.pack()
        self.text = Text(self.math, height=20, width=20, background="brown")
        self.text.pack()
        self.statement = "Results"
        self.text.insert(INSERT, self.statement)
        self.text.config(state=DISABLED)

        self.menuButton = Button(self.math, text="Menu")
        self.menuButton.pack()
        self.menuButton.bind("<Button-1>", self.menu)





root = Tk()

root.minsize(width=625, height=400)
root.wm_title("Fractions Helper")

fh = FractionsHelper(root)

root.mainloop()
