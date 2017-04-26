#-------------------------------------------------------------------#
# Main project file now.                                            #
# Authors: Ryan, Zack, Sterling, Ben                                #
#                                                                   #
#-------------------------------------------------------------------#

from random import randint
from fractions import Fraction

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here


class Fractions(Tk):

    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (Login, Menu, Solver, Quizzer, Results):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(Login)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class Login(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
                # Why is this named question?
        self.question = Label(self,text="Login Screen", )
        self.question.pack(side="top")

        Label(self,text="Username").pack()
        self.username = Entry(self, width=20)
        self.username.pack()

        Label(self,text="Password").pack()
        self.password = Entry(self, width=20, show="*")
        self.password.pack()

        self.loginButton = Button(self,text="Sign in",
                                  command=lambda:controller.show_frame(Menu))
        self.loginButton.pack(pady=(20, 10))
        self.loginButton.bind("<Button-1>")

        self.createButton = Button(self,text="Sign Up")
        self.createButton.pack(pady=(10))
        self.createButton.bind(self,"<Button-1>", self.create_attempt)

    def signIn(self, username, password):
        #requires database stuff
        return True

    def login_attempt(self, click):
        #requires database stuff

        attempt = self.signIn(self.username.get(),self.password.get())

        self.menu(self)

    def create_attempt(self, click):

        print("attempting to create account...")
        attempt = self.newUser(self.username.get(), self.password.get())


class Menu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)


        self.solverButton = Button(self, text = "Solver", height = 6, width = 50, borderwidth = 2, background="red",
                                 command=lambda:controller.show_frame(Solver))
        self.solverButton.pack()
        self.solverButton.bind("<Button-1>")

        self.quizzerButton = Button(self, text = "Quizzer", height = 6, width = 50, borderwidth = 2, bg="white",
                                 command=lambda:controller.show_frame(Quizzer))
        self.quizzerButton.pack()
        self.quizzerButton.bind("<Button-1>")

        self.resultsButton = Button(self, text = "Results", height = 6, width = 50, borderwidth = 2, bg="blue",
                                 command=lambda:controller.show_frame(Results))
        self.resultsButton.pack()
        self.resultsButton.bind("<Button-1>")


class Solver(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)

        self.operator = IntVar()

        self.menu = Button(self, text = "Menu", command=lambda:controller.show_frame(Menu))
        self.menu.place(x = 450, y = 0)
        self.menu.bind("<Button-1>")

        self.num1Entry = Entry(self, width = 7)
        self.num1Entry.place(x = 165, y = 75)

        self.f1Entry = Label(self, width= 11, text="_____________")
        self.f1Entry.place(x = 151, y = 105)

        self.denom1Entry = Entry(self, width = 7)
        self.denom1Entry.place(x = 165, y = 140)

        self.num2Entry = Entry(self, width = 7)
        self.num2Entry.place(x = 285, y = 75)

        self.f2Entry = Label(self, width = 11 , text="_____________")
        self.f2Entry.place(x = 271, y = 105)

        self.denom2Entry = Entry(self, width = 7)
        self.denom2Entry.place(x = 285, y = 140)


        # # solve button, when press will solve the given fractions
        self.solveButton = Button(self, text="Solve")
        self.solveButton.place(x=375, y=225)
        self.solveButton.bind("<Button-1>", self.solve)

        #display the answer
        self.solveDisplay = Label(self, width=10, bg="lightgrey")
        self.solveDisplay.place(x=358, y=255)

        # operator buttons, when pressed, will solve using given operator
        self.plus = Radiobutton(self, text="+", variable= self.operator, value=1)
        self.plus.place(x=170, y = 225)

        self.minus = Radiobutton(self, text="-", variable=self.operator, value=2)
        self.minus.place(x=215, y = 225)

        self.divide = Radiobutton(self, text="/", variable=self.operator, value=3)
        self.divide.place(x=255, y = 225)

        self.multiply = Radiobutton(self, text="*", variable=self.operator, value=4)
        self.multiply.place(x=295, y = 225)


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

        self.frac3 = Fraction()
        self.frac3 = self.operation()
        self.display()

    def display(self):
        self.solveDisplay.config(text = self.frac3)

class Quizzer(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.operator = IntVar()
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()

        self.menu = Button(self, text = "Menu", command=lambda:controller.show_frame(Menu))
        self.menu.place(x = 450, y = 0)
        self.menu.bind("<Button-1>")

        self.num1Entry = Label(self, width = 7, textvariable = self.var1)
        self.num1Entry.place(x = 165, y = 85)

        self.fbar = Label(self, width=5, text="______")
        self.fbar.place(x = 173, y = 105)

        self.denom1Entry = Label(self, width = 7, textvariable=self.var2)
        self.denom1Entry.place(x = 165, y = 140)

        self.operatorLabel = Label(self, width = 7)
        self.operatorLabel.place(x = 230, y = 110)

        self.num2Entry = Label(self, width=7, textvariable=self.var3)
        self.num2Entry.place(x = 285, y = 85)

        self.f2bar = Label(self, width=5, text="______")
        self.f2bar.place(x = 293, y = 105)

        self.denom2Entry = Label(self, width=7, textvariable=self.var4)
        self.denom2Entry.place(x = 285, y = 140)


        # generate button, when pressed will generate fractions
        self.genButton = Button(self, text="Generate")
        self.genButton.place(x=20, y=105)
        self.genButton.bind("<Button-1>", self.generate)

        # display the answer
        self.solveDisplay = Label(self, width=7, text="Answer:")
        self.solveDisplay.place(x=300, y=255)

        # display the answer
        self.answerEntry = Entry(self, width=7, bg="lightgrey")
        self.answerEntry.place(x=370, y=255)

        self.corrDisplay = Label(self, width=11, text= "")
        self.corrDisplay.place(x=355, y=285)

        # solve button, when press will solve the given fractions
        self.solveButton = Button(self, text="Submit")
        self.solveButton.place(x=373, y=225)
        self.solveButton.bind("<Button-1>", self.check)

        # operator buttons, when pressed, will solve using given operator
        self.plus = Radiobutton(self, text="+", variable=self.operator, value=1, command=self.changeOp)
        self.plus.place(x=170, y = 225)

        self.minus = Radiobutton(self, text="-", variable=self.operator, value=2, command=self.changeOp)
        self.minus.place(x=215, y = 225)

        self.divide = Radiobutton(self, text="/", variable=self.operator, value=3, command=self.changeOp)
        self.divide.place(x=255, y = 225)

        self.multiply = Radiobutton(self, text="*", variable=self.operator, value=4, command=self.changeOp)
        self.multiply.place(x=295, y = 225)

    def operation(self):
        if str(self.operator.get()) == "1":
            self.operatorLabel.config(text='+')
            return self.frac1 + self.frac2
        elif str(self.operator.get()) == "2":
            self.operatorLabel.config(text='-')
            return self.frac1 - self.frac2
        elif str(self.operator.get()) == "3":
            self.operatorLabel.config(text='/')
            return self.frac1 / self.frac2
        elif str(self.operator.get()) == "4":
            self.operatorLabel.config(text='*')
            return self.frac1 * self.frac2

    def changeOp(self):
        if str(self.operator.get()) == "1":
            self.operatorLabel.config(text='+')
        elif str(self.operator.get()) == "2":
            self.operatorLabel.config(text='-')
        elif str(self.operator.get()) == "3":
            self.operatorLabel.config(text='/')
        elif str(self.operator.get()) == "4":
            self.operatorLabel.config(text='*')


    def generate(self, click):
        self.var1.set(randint(1, 20))
        self.var2.set(randint(1, 20))
        self.var3.set(randint(1, 20))
        self.var4.set(randint(1, 20))

    def check(self, click):
        self.userAns = self.answerEntry.get()

        self.num1 = int(self.var1.get())
        self.num2 = int(self.var2.get())
        self.num3 = int(self.var3.get())
        self.num4 = int(self.var4.get())

        self.frac1 = Fraction(self.num1, self.num2)
        self.frac2 = Fraction(self.num3, self.num4)

        self.frac3 = Fraction()
        self.frac3 = self.operation()

        self.strFrac = str(self.frac3)

        self.strAns = self.answerEntry.get()

        num, denom = self.strAns.split("/")
        num1 = int(num)
        denom1 = int(denom)
        frac4 = Fraction(num1, denom1)

        if self.strAns == self.strFrac:
            self.corrDisplay.config(text = "Correct")
        elif self.frac3 % frac4 == 0:
            self.corrDisplay.config(text = "Partial Credit")
        else:
            self.corrDisplay.config(text="Incorrect")

class Results(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)

        self.menu = Button(self, text = "Menu", command=lambda:controller.show_frame(Menu))
        self.menu.place(x = 450, y = 0)
        self.menu.bind("<Button-1>")


app = Fractions()
app.geometry("525x325")
app.resizable(width=False, height=False)

mainloop()
