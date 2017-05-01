#-------------------------------------------------------------------#
# Main project file now.                                            #
# Authors: Ryan, Zack, Ben, Sterling                                #
#                                                                   #
#-------------------------------------------------------------------#

from random import randint
from fractions import Fraction
from bcrypt import hashpw, gensalt
import sqlite3
import plotly.plotly as py
import plotly.graph_objs as go
import plotly


try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

USERNAME = ''

class Fractions(Tk):

    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        connect = sqlite3.connect('FractionSolver.db')
        login_info = connect.cursor()
        login_info.execute('''CREATE TABLE IF NOT EXISTS login (username VARCHAR, password VARCHAR, operator VARCHAR(1), score real)''')
        connect.commit()
        connect.close()

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
    ''' Create login frame which deals with a user either entering into the main menu with a previously created username and password or creating a new one'''
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.question = Label(self,text="Login Screen", )
        self.question.pack(side="top")

        self.login_status = Label(self,text="", )
        self.login_status.pack(side="bottom")

        Label(self,text="Username").pack()
        self.username = Entry(self, width=20)
        self.username.pack()

        Label(self,text="Password").pack()
        self.password = Entry(self, width=20, show="*")
        self.password.pack()

        self.loginButton = Button(self,text="Sign in",
                                  command=lambda:controller.show_frame(Login))
        self.loginButton.pack(pady=(20, 10))
        self.loginButton.bind("<Button-1>", self.login_attempt)

        self.createButton = Button(self,text="Sign Up")
        self.createButton.pack(pady=(10))
        self.createButton.bind("<Button-1>", self.create_attempt)

        self.loggedIn = False

    def signIn(self, username, password):
        ''' Verifies that a user exists and that their credentials are valid '''
        connect = sqlite3.connect('FractionSolver.db')
        login_info = connect.cursor()

        login_info.execute("SELECT count(*) FROM login WHERE username = ? AND password = ?", (username, password))
        count = login_info.fetchone()[0]
        if count == 0:
            self.login_status.config(text = 'There is no username with this name')
            return False

        connect.close()

        return True

    def newUser(self, username, password):
        ''' Creates a new user and ensures that user does not already exist '''
        connect = sqlite3.connect('FractionSolver.db')
        login_info = connect.cursor()

        login_info.execute("SELECT count(*) FROM login WHERE username = ?", (username,))
        count = login_info.fetchone()[0]
        if count == 0:
            login_info.execute('''INSERT INTO login (username, password) VALUES(?,?)''', (username, password))
            self.login_status.config(text = 'Account Created')
        connect.commit()
        connect.close()
        return True

    def login_attempt(self, click):
        ''' Attempts to login a user if credentials are correct '''
        global USERNAME
        USERNAME = self.username.get()
        attempt = self.signIn(self.username.get(),self.password.get())

        if(attempt == False):
            self.login_status.config(text = 'Invalid login')
        else:
            self.login_status.config(text = 'Valid login')
            self.loggedIn = True
            app.show_frame(Menu)

    def create_attempt(self, click):
        ''' Attempts to create a user if it does not exist '''
        self.login_status.config(text = 'attempting to create account...')
        attempt = self.newUser(self.username.get(), self.password.get())




class Menu(Frame):
    '''Allows the user to select which frame they want to go to.'''
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
    '''Creates the logical placement of all the widgets and buttons'''
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
        '''Converts the radial button inputs into their corresponding operation'''
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
        '''Solves it's inputs from the solver function'''
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
    '''Initializes the layout of the Frames'''
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.operator = IntVar()
        self.op = ''
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.correct = False

        self.menu = Button(self, text = "Menu")
        self.menu.place(x = 450, y = 0)
        self.menu.bind("<Button-1>", self.MENU)

        self.num1Entry = Label(self, width = 7, textvariable = self.var1)

        self.fbar = Label(self, width=5, text="______")
        self.fbar.place(x = 173, y = 105)

        self.denom1Entry = Label(self, width = 7, textvariable=self.var2)

        self.operatorLabel = Label(self, width = 7)
        self.operatorLabel.place(x = 230, y = 110)

        self.num2Entry = Label(self, width=7, textvariable=self.var3)

        self.f2bar = Label(self, width=5, text="______")
        self.f2bar.place(x = 293, y = 105)

        self.denom2Entry = Label(self, width=7, textvariable=self.var4)

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

    def place(self):
        '''Places the labeled entries, removed from init method to allow wiping it from the screen if the user decides to leaves the question without answering '''
        self.num1Entry.place(x = 165, y = 85)
        self.denom1Entry.place(x = 165, y = 140)
        self.num2Entry.place(x = 285, y = 85)
        self.denom2Entry.place(x = 285, y = 140)

    def forget(self):
        '''Hides all of the labels from showing the fractions that they generated'''
        self.num1Entry.place_forget()
        self.denom1Entry.place_forget()
        self.num2Entry.place_forget()
        self.denom2Entry.place_forget()

    def MENU(self, click):
        '''Directs us back to the main menu and wipes the screen'''
        self.forget()
        app.show_frame(Menu)

    def raise_partiallyCorrect(self):
        '''Raises the pop up that tells us that the function was partially correct'''
        root = Toplevel()
        root.geometry("300x100")
        app1 = partiallyCorrect(root)

    def operation(self):
        if str(self.operator.get()) == "1":
            self.operatorLabel.config(text='+')
            self.op = '+'
            return self.frac1 + self.frac2
        elif str(self.operator.get()) == "2":
            self.operatorLabel.config(text='-')
            self.op = '-'
            return self.frac1 - self.frac2
        elif str(self.operator.get()) == "3":
            self.operatorLabel.config(text='/')
            self.op = '/'
            return self.frac1 / self.frac2
        elif str(self.operator.get()) == "4":
            self.operatorLabel.config(text='*')
            self.op = '*'
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
        self.place()
        self.correct = False

    def check(self, click):
        '''Compares the entered in answer to the correct answer while allowing partial credit to recieve multiple attempts.'''
        connect = sqlite3.connect('FractionSolver.db')
        login_info = connect.cursor()
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

        try:
            num, denom = self.strAns.split("/")
        except ValueError:
            num = self.strAns
            denom = '1'
        num1 = int(num)
        denom1 = int(denom)
        frac4 = Fraction(num1, denom1)

        if self.strAns == self.strFrac and self.correct == False:
            self.corrDisplay.config(text = "Correct")
            login_info.execute('''INSERT INTO login (username, operator, score) VALUES(?,?,?)''', (USERNAME, self.op, 1))
            self.correct = True
        elif self.frac3 % frac4 == 0 and self.correct == False:
            self.corrDisplay.config(text = "Partial Credit")
            login_info.execute('''INSERT INTO login (username, operator, score) VALUES(?,?,?)''', (USERNAME, self.op, 0.5))
            self.raise_partiallyCorrect()
        elif self.correct != True:
            self.corrDisplay.config(text="Incorrect")
            login_info.execute('''INSERT INTO login (username, operator, score) VALUES(?,?,?)''', (USERNAME, self.op, 0))

        connect.commit()
        connect.close()

class partiallyCorrect(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.explanation = Label(master, text="Must Reduce Fractions For Full Credit.")
        self.explanation.pack()


class Results(Frame):
    ''' Results frame queries sqlite database table created previously and ses operator and score data to create plotly bar charts '''
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)

        self.menu = Button(self, text = "Menu", command=lambda:controller.show_frame(Menu))
        self.menu.place(x = 450, y = 0)
        self.menu.bind("<Button-1>")
        self.solveButton = Button(self, text="Get Results")
        self.solveButton.place(x=205, y=150)
        self.solveButton.bind("<Button-1>", self.Plotting)

    def Plotting(self, click):
        ''' Queries the data from our sqlite table called login and uses plotly to create a barchart '''
        connect = sqlite3.connect('FractionSolver.db')
        login_info = connect.cursor()


        login_info.execute("SELECT AVG(score) FROM login WHERE username = '%s' AND operator = '+'" % USERNAME)
        plus = login_info.fetchall()

        login_info.execute("SELECT AVG(score) FROM login WHERE username = '%s' AND operator = '-'" % USERNAME)
        minus = login_info.fetchall()

        login_info.execute("SELECT AVG(score) FROM login WHERE username = '%s' AND operator = '*'" % USERNAME)
        mult = login_info.fetchall()

        login_info.execute("SELECT AVG(score) FROM login WHERE username = '%s' AND operator = '/'" % USERNAME)
        divide = login_info.fetchall()

        login_info.execute("SELECT AVG(score) FROM login WHERE username = '%s'" % USERNAME)
        ops = login_info.fetchall()


        #for all
        login_info.execute("SELECT AVG(score) FROM login WHERE operator = '+'")
        all_plus = login_info.fetchall()

        login_info.execute("SELECT AVG(score) FROM login WHERE operator = '-'")
        all_minus = login_info.fetchall()

        login_info.execute("SELECT AVG(score) FROM login WHERE operator = '*'")
        all_mult = login_info.fetchall()

        login_info.execute("SELECT AVG(score) FROM login WHERE operator = '/'")
        all_divide = login_info.fetchall()

        login_info.execute("SELECT AVG(score) FROM login")
        all_ops = login_info.fetchall()

        #connect.commit()
        connect.close()

        plotly.tools.set_credentials_file(username='zwilliams013', api_key = '5ImO4kp7IoFPRSBqqMRE')

        trace0 = go.Bar(
            x = ['Add', 'Sub', 'Mult', 'Div','Sum'],
            y = [plus[0][0], minus[0][0], mult[0][0], divide[0][0], ops[0][0]],
            name = 'USER'
            )
        trace1 = go.Bar(
            x = ['Add', 'Sub', 'Mult', 'Div','Sum'],
            y = [all_plus[0][0], all_minus[0][0], all_mult[0][0], all_divide[0][0], all_ops[0][0]],
            name = 'OVERALL'
        )

        data = [trace0, trace1]
        layout = go.Layout(
            xaxis=dict(tickangle=0),
            barmode='group',
        )

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig,filename='Result Page')

app = Fractions()
app.geometry("525x325")
app.resizable(width=False, height=False)

mainloop()
