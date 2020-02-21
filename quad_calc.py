#  Copyright © 2020 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: ZRonnieColab
#  File Name: quad_calc.py
#  Last Modified: 21/02/2020, 19:57
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: ZRonnieColab
#  File Name: quad_calc.py
#  Last Modified: 21/02/2020, 19:46

import math as mt
import os
import platform as pf


def clearScreen():
    if "Windows" in pf.platform():
        os.system("cls")
    else:
        os.system("clear")


while True:
    print("If a quadratic equation was in the form ax^2 + bx + c = 0, enter the values for a, b and c.")
    a = int(input("Gimme a: "))
    b = int(input("Gimme b: "))
    c = int(input("Gimme c: "))

    if (b ** 2) - 4 * a * c < 0:
        print("Oh, sorry. Your equation doesn't have any solutions.")

    elif b ** 2 - 4 * a * c == 0:
        sol = (-b + mt.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

        print("Here ya go! The discriminant is 0 so there's only 1 solution for x: " + str(sol))

    else:
        sol1 = (-b + mt.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        sol2 = (-b - mt.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

        print(
            "Here ya go! The discriminant is greater than 0 so there's 2 solutions for x: {} and {}".format(sol1, sol2))

    if input("Would you like to quit? (Y/n): ").lower() == "y":
        break

    clearScreen()

print("Thanks for using my quadratic equation solver!")
