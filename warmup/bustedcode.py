#!/usr/bin/env python3  
# corrected the path and "python" version

# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

def main() :          # appended ":" to designate start of the function body
    calc1 = 0.0       # moved here from outside main()
    calc2 = 0.0       # moved here from outside main()
    operation = ""    # moved here from outside main()
    while calc1 != "q" :   # appended ":" to designate start if "while" loop
        print("\nWhat is the first operator? Or, enter q to quit: ")
        calc1 = input()  # changed from raw_input() to input()
        if calc1.upper() == "Q":
            break
        calc1 = float(calc1)
        print("\nWhat is the second operator? Or, enter q to quit: ")
        calc2 = input()  # changed from raw_input() to input()
        if calc2.lower() == "q":
            break
        calc2 = float(calc2)
        print("Enter an operation to perform on the two operators (+ or -): ")
        operation = input()  # changed from raw_input() to input()
        if operation == "+":
            add(calc1,calc2)
        elif operation == '-':
            sub(calc1,calc2)
        else:
            print("\n Not a valid entry. Restarting...")

def add(num1,num2):
    #print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    #replaced calc1 and calc2 by actual arguments passed
    print("\n" + str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
    
def sub(num1,num2):
    print("\n" + str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
    
main()     # moved to the end such that all function defs are defined and available
