from tkinter import *
from tkinter import ttk
import FractionSolver.py

def sel():
   selection = "" + str(var.get())
   solveDisplay.config(text = selection)

#erase answer when clicking different operator button
def erase():
   solveDisplay.config(text = "")


window = Tk()
var = IntVar()
window.geometry("240x100+0+0")
window.resizable(width=False, height= False)

window.title("Solver")


main = Button(window, text = "Main", width = 5)
main.grid(row = 0, column = 20 , sticky = W)


#make entry box for numerators and denominators
num1Entry = Entry(window, width = 5)
num1Entry.grid(row = 0, column = 0, columnspan = 3)

denom1Entry = Entry(window, width = 5)
denom1Entry.grid(row = 2,  columnspan = 3)

num2Entry = Entry(window, width = 5)
num2Entry.grid(row = 0, column = 3, columnspan =3 )

denom2Entry = Entry(window, width = 5)
denom2Entry.grid(row = 2, column = 3, columnspan =3 )


#solve button, when press will solve the given fractions
solveButton = Button(window, text = "Solve")
solveButton.grid(row = 3, column = 0, padx = 5)

#display the answer
solveDisplay = Label(window, width = 7, bg = "lightgrey")
solveDisplay.grid(row = 3, column = 3, padx = 10)

#operator buttons, when pressed, will solve using given operator
plus = Radiobutton(window, text = "+", value = 1)
plus.grid(row = 3, column = 4, sticky = E)

minus = Radiobutton(window, text = "-", value = 2)
minus.grid(row = 3, column = 5, sticky = W)

divide = Radiobutton(window, text = "/", value = 3, command = sel)
divide.grid(row = 4, column = 4, sticky = E)

multiply = Radiobutton(window, text = "*", value = 4, command = erase)
multiply.grid(row = 4, column = 5, sticky = W)


label = Label(window)
label.grid(row = 8, column = 0, sticky = W)

window.mainloop()
