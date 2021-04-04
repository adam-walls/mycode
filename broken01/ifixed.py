#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

calc1 = 0.0
calc2 = 0.0
operation = ""

while calc1 != "q" or calc2 != "q":
    print("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = input()
    if calc1 == "q":
        break
    calc1 == float(calc1)
    calc2 = input("What is the second operator? or, enter q to quit:\n")
    if calc2 == "q":
        break
    calc2 = float(calc2)
    print("\nEnter an operation to perform on the two operators (+ or -): ")
    operation = input()
    if operation == "+":
        addition = float(calc1) + float(calc2)
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(addition))
    elif operation == '-':
        subtract = float(calc1) - float(calc2)
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(subtract))
    else:
        print("\n Not a valid entry. Restarting...")

