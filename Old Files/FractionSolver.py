import sys
import re
from fractions import Fraction

#Check for a negative from each numerator. In between each fraction, look for the sign.

patt = re.compile('([-]?[\d]+)\/([\d]+)\s?([+\-/*])\s?([-]?[\d]+)\/([\d]+)')

while True:
    try:
        s = input("Please provide a fractional equation to compute: ")
        if not s:
            sys.exit("Empty String, aborting program as per instructions!")

        user_input = re.findall(patt, s)

        x = Fraction((user_input[0][0]) + "/" + user_input[0][1]) # + '/' ((user_input[0][1])))    #, int(user_input[0][1])))
        y = Fraction(user_input[0][3] + "/" + user_input[0][4])
        op = (user_input[0][2])

        if op == "*":
            r = x * y

        elif op == "/":
            r = x / y

        elif op == "+":
            r = x + y

        elif op == "-":
            r = x - y

        print(s + " = " + str(r))
    except Exception as e:
        print("Error encountered: ", e)

        continue
