from tkinter import *
from fractions import Fraction
from tkinter import ttk
import FractionSolver.py

#Operation calculations
def operation(frac1, frac2):
   if operator.get() == 1:
      return frac1 + frac2
   elif operator.get() == 2:
      return frac1 - frac2
   elif operator.get() == 3:
      return frac1 / frac2
   elif operator.get() == 4:
      return frac1 * frac2

#Function when pressing solve butotn
def solve():
   num1 = int(num1Entry.get())
   num2 = int(denom1Entry.get())

   num3 = int(num2Entry.get())
   num4 = int(denom2Entry.get())

   frac1 = Fraction(num1,num2)
   frac2 = Fraction(num3, num4)
   frac3 = Fraction()
   frac3 = operation(frac1, frac2)

   solveDisplay.config(text = frac3)


window = Tk()
var = IntVar()
window.geometry("340x200")
window.resizable(width=False, height= False)

operator = IntVar()

window.title("Solver")


main = Button(window, text = "Main", width = 5)
main.place(x = 295, y = 0)


#make entry box for numerators and denominators
num1Entry = Entry(window, width = 5)
num1Entry.place(x = 50, y = 20)

denom1Entry = Entry(window, width = 5)
denom1Entry.place(x = 50, y = 50)

num2Entry = Entry(window, width = 5)
num2Entry.place(x = 150, y = 20)

denom2Entry = Entry(window, width = 5)
denom2Entry.place(x = 150, y = 50)


#solve button, when press will solve the given fractions
solveButton = Button(window, text = "Solve", command = solve)
solveButton.place(x = 30, y = 120)

#display the answer
solveDisplay = Label(window, width = 7, bg = "lightgrey")
solveDisplay.place(x = 100, y = 120)

#operator buttons, when pressed, will solve using given operator
plus = Radiobutton(window, text = "+", variable = operator, value = 1)
plus.place(x = 200, y = 110)

minus = Radiobutton(window, text = "-", variable = operator, value = 2)
minus.place(x = 230, y = 110)

divide = Radiobutton(window, text = "/", variable = operator, value = 3)
divide.place(x = 200, y = 140)

multiply = Radiobutton(window, text = "*", variable = operator, value = 4)
multiply.place(x = 230, y = 140)


window.mainloop()
