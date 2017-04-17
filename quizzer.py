from tkinter import *
from fractions import Fraction
from random import randint


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

def generate():
   var1.set(randint(0,9))
   var2.set(randint(1,9))
   var3.set(randint(0,9))
   var4.set(randint(1,9))


window = Tk()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

window.geometry("340x200")
window.resizable(width=False, height= False)

operator = IntVar()

window.title("Quizzer")


main = Button(window, text = "Main", width = 5)
main.place(x = 295, y = 0)


#make entry box for numerators and denominators
num1Entry = Label(window, width = 5, textvariable = var1)
num1Entry.place(x = 100, y = 40)

denom1Entry = Label(window, width = 5, textvariable = var2)
denom1Entry.place(x = 100, y = 70)

num2Entry = Label(window, width = 5, textvariable = var3)
num2Entry.place(x = 200, y = 40)

denom2Entry = Label(window, width = 5, textvariable = var4)
denom2Entry.place(x = 200, y = 70)


#solve button, when press will solve the given fractions
solveButton = Button(window, text = "Solve", command = solve)
solveButton.place(x = 160, y = 120)

#generate button, when pressed will generate fractions
genButton = Button(window, text = "Generate", command = generate)
genButton.place(x = 20, y = 50)

#display the answer
solveDisplay = Label(window, width = 7, text = "Answer")
solveDisplay.place(x = 40, y = 120)

#display the answer
answerEntry = Entry(window, width = 7, bg = "lightgrey")
answerEntry.place(x = 100, y = 120)


#operator buttons, when pressed, will solve using given operator
plus = Radiobutton(window, text = "+", variable = operator, value = 1)
plus.place(x = 220, y = 110)

minus = Radiobutton(window, text = "-", variable = operator, value = 2)
minus.place(x = 250, y = 110)

divide = Radiobutton(window, text = "/", variable = operator, value = 3)
divide.place(x = 220, y = 140)

multiply = Radiobutton(window, text = "*", variable = operator, value = 4)
multiply.place(x = 250, y = 140)

print(num1Entry['text'])

window.mainloop()
