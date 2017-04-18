import bcrypt
# import fractions
import operator
from fractions import Fraction
from random import randint
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


self.math = Tk()
self.math.geometry("200x175")
self.math.title("Finale")
# Set self.math color to light blue
self.math.configure(background='#DEEFF5')

lbl = Label(self.math, text="Enter your username")
# Set label color to light blue
lbl.configure(background='#DEEFF5')
lbl.pack()
# Make text entry box for username
TextEntry = Entry(self.math, bd=5)
TextEntry.pack()

lbl3 = Label(self.math, text = "Enter your password")
# Set password color to light blue
lbl3.configure(background='#DEEFF5')
lbl3.pack()
# Make text entry box for password
TextEntry2 = Entry(self.math, bd=5)
TextEntry2.pack()

button = Button(self.math, text="Submit", command=getusername)
button.pack()
lbl2 = Label(self.math, text="")
# Set label color to light blue
lbl2.configure(background="#DEEFF5")
lbl2.pack()

self.math.mainloop()'''

class FractionsHelper:

    def __init__(self, parent_):

        self.username = ""
        self.password = ""
        self.parent = parent_;

        # self.num1Entry = ""
        # self.num2Entry = ""
        # self.denom1Entry = ""
        # self.denom2Entry = ""
        self.operator = IntVar()
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()

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
        # self.parent.resizable(width=False, height=False)
        self.container1 = Frame(self.parent, width=625, height=400)
        # self.container1.resizable(width=False, height=False)

        self.container1.pack()

        # self.menuText = Text(self.container1)
        # self.menuText.pack(anchor=CENTER, fill=Y)
        # self.menuText.place(x = 0, y = 0)
        # self.statement = "Fractions Helper Main Menu. \n"
        # self.menuText.insert(INSERT, self.statement)
        # self.menuText.config(state=DISABLED)

        self.solverButton = Button(self.container1, text = "Solver", height = 8, width = 84, borderwidth = 2)
        # self.solverButton.pack(side=LEFT, padx=(0, 100))
        self.solverButton.place(x = 0, y = 0)
        self.solverButton.bind("<Button-1>", self.solver)

        self.quizzerButton = Button(self.container1, text = "Quizzer", height = 8, width = 84, borderwidth = 2)
        # self.quizzerButton.pack(side=LEFT, padx=(0, 100))
        self.quizzerButton.place(x=0, y= 100)
        self.quizzerButton.bind("<Button-1>", self.quizzer)

        self.resultsButton = Button(self.container1, text = "Results", height = 8, width = 84, borderwidth = 2)
        # self.resultsButton.pack(side=LEFT, padx=(0, 100))
        self.resultsButton.place(x=0, y=250)
        self.resultsButton.bind("<Button-1>", self.results)


    def operation(self):
        print("Operation func")
        if str(self.operator.get()) == "1":
            return self.frac1 + self.frac2
        elif str(self.operator.get()) == "2":
            return self.frac1 - self.frac2
        elif str(self.operator.get()) == "3":
            return self.frac1 / self.frac2
        elif str(self.operator.get()) == "4":
            return self.frac1 * self.frac2

    # Function when pressing solve butotn
    def solve(self, click):
        print("Solve func")
        self.num1 = int(self.num1Entry.get())
        self.num2 = int(self.denom1Entry.get())

        self.num3 = int(self.num2Entry.get())
        self.num4 = int(self.denom2Entry.get())

        self.frac1 = Fraction(self.num1, self.num2)
        self.frac2 = Fraction(self.num3, self.num4)
        # self.frac1 = Fraction(1,2)
        # self.frac2 = Fraction(3,4)
        self.frac3 = Fraction()
        self.frac3 = self.operation()
        print(self.frac3)

        self.solveDisplay.config(text = self.frac3)
        print("Display changed")
        print(self.operator)

    def generate(self, click):
        self.var1.set(randint(1, 20))
        self.var2.set(randint(1, 20))
        self.var3.set(randint(1, 20))
        self.var4.set(randint(1, 20))

    def solver(self, click):
        self.container.destroy()
        self.container1.destroy()

        try:
            self.math.destroy()
        except Exception:
            pass


        self.math = Frame(self.parent, width=625, height=400)
        # self.math.resizable(width=False, height=False)

        self.math.pack()

        # make entry box for numerators and denominators
        self.num1Entry = Entry(self.math, width=5)
        self.num1Entry.place(x = 50, y = 35)

        self.f1Entry = Label(self.math, width=5, text="_______")
        self.f1Entry.place(x = 49, y = 53)

        self.denom1Entry = Entry(self.math, width=5)
        self.denom1Entry.place(x = 50, y = 75)

        self.num2Entry = Entry(self.math, width=5)
        self.num2Entry.place(x = 150, y = 30)

        self.f2Entry = Label(self.math, width=5, text="________")
        self.f2Entry.place(x = 146, y = 48)

        self.denom2Entry = Entry(self.math, width=5)
        self.denom2Entry.place(x = 150, y = 75)

        # # solve button, when press will solve the given fractions
        self.solveButton = Button(self.math, text="Solve")
        self.solveButton.place(x=30, y=120)
        self.solveButton.bind("<Button-1>", self.solve)


        # display the answer
        self.solveDisplay = Label(self.math, width=7, bg="lightgrey")
        self.solveDisplay.place(x=100, y=120)

        # operator buttons, when pressed, will solve using given operator
        self.plus = Radiobutton(self.math, text="+", variable= self.operator, value=1)
        self.plus.place(x=200, y=110)

        self.minus = Radiobutton(self.math, text="-", variable=self.operator, value=2)
        self.minus.place(x=230, y=110)

        self.divide = Radiobutton(self.math, text="/", variable=self.operator, value=3)
        self.divide.place(x=200, y=140)

        self.multiply = Radiobutton(self.math, text="*", variable=self.operator, value=4)
        self.multiply.place(x=230, y=140)

        # self.parent.minsize(width=625, height=400)
        # self.math = Frame(self.parent, width=625, height=400, background="red")
        # self.math.pack()
        # self.text = Text(self.math, height=20, width=20)
        # self.text.pack()
        # self.statement = "Solver"
        # self.text.insert(INSERT, self.statement)
        # self.text.config(state=DISABLED)
        #
        # self.menuButton = Button(self.math, text="Menu")
        # self.menuButton.pack()
        # self.menuButton.bind("<Button-1>", self.menu)
        self.menuButton = Button(self.math, text="Menu")
        self.menuButton.place(x = 300, y = 50)
        self.menuButton.bind("<Button-1>", self.menu)


    def quizzer(self, click):
        self.container.destroy()
        self.container1.destroy()

        try:
            self.math.destroy()
        except Exception:
            pass

        self.math = Frame(self.parent, width=625, height=400)
        # self.math.resizable(width=False, height=False)

        self.math.pack()

        # make entry box for numerators and denominators
        self.num1Entry = Label(self.math, width=5, textvariable = self.var1)
        self.num1Entry.place(x=100, y=35)

        self.fbar = Label(self.math, width=5, text="__")
        self.fbar.place(x=100, y=50)

        self.denom1Entry = Label(self.math, width=5, textvariable=self.var2)
        self.denom1Entry.place(x=100, y=75)

        self.num2Entry = Label(self.math, width=5, textvariable=self.var3)
        self.num2Entry.place(x=200, y=35)

        self.f2bar = Label(self.math, width=5, text="__")
        self.f2bar.place(x=200, y=50)

        self.denom2Entry = Label(self.math, width=5, textvariable=self.var4)
        self.denom2Entry.place(x=200, y=75)

        # solve button, when press will solve the given fractions
        self.solveButton = Button(self.math, text="Solve")
        self.solveButton.place(x=160, y=120)
        self.solveButton.bind("<Button-1>", self.solve)

        # generate button, when pressed will generate fractions
        self.genButton = Button(self.math, text="Generate")
        self.genButton.place(x=20, y=50)
        self.genButton.bind("<Button-1>", self.generate)

        # display the answer
        self.solveDisplay = Label(self.math, width=7, text="Answer")
        self.solveDisplay.place(x=40, y=120)

        # display the answer
        self.answerEntry = Entry(self.math, width=7, bg="lightgrey")
        self.answerEntry.place(x=100, y=120)

        # operator buttons, when pressed, will solve using given operator
        self.plus = Radiobutton(self.math, text="+", variable=self.operator, value=1)
        self.plus.place(x=220, y=110)

        self.minus = Radiobutton(self.math, text="-", variable=self.operator, value=2)
        self.minus.place(x=250, y=110)

        self.divide = Radiobutton(self.math, text="/", variable=self.operator, value=3)
        self.divide.place(x=220, y=140)

        self.multiply = Radiobutton(self.math, text="*", variable=self.operator, value=4)
        self.multiply.place(x=250, y=140)

        # self.parent.minsize(width=625, height=400)
        # self.math = Frame(self.parent, width=625, height=400, background="green")
        # self.math.pack()
        # self.text = Text(self.math, height=20, width=20, background="green")
        # self.text.pack()
        # self.statement = "Quizzer"
        # self.text.insert(INSERT, self.statement)
        # self.text.config(state=DISABLED)

        self.menuButton = Button(self.math, text="Menu")
        self.menuButton.place(x = 300, y = 50)
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

root.geometry("625x400")
root.resizable(width= False, height= False)
root.wm_title("Fractions Helper")

fh = FractionsHelper(root)

root.mainloop()
