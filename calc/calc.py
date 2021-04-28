#!/usr/bin/env python3

def add(num1,num2=0):
    return num1 + num2

def subtract(num1,num2=0):
    return num1 - num2

def divide(num1,num2=1):
    return num1 / num2

def multiply(num1,num2=1):
    return num1 * num2

def main():
    val1 = 1
    val2 = 1
    print("Welcome to Primitive Calculator ..... \n")
    while True:

        while True:
              try :
                   oper1 = int(input("Enter 1st Operand (Default = 1) >>>  "))
                   val1 = oper1
                   break
              except ValueError :
                   if UnboundLocalError :
                       val1 = 1
                       break
                   else :
                       print("Only integer values allowed ... remember I am 'Primitive' ... Ha ha ha ha")

        while True:
              action = input("Choose Operator Add/Subtract/Multiply/Divide >>>  ")
              if action.lower().strip() not in [ 'add','subtract','multiply','divide' ] :
                  print("Invalid Operation requested, try again")
              else : 
                  break
              
        while True:
              try :
                   oper2 = int(input("Enter 2nd Operand (Default = 1) >>>  "))
                   val2 = oper2
                   break
              except ValueError :
                   if UnboundLocalError :
                       val2 = 1
                       break
                   else :
                       print("Only integer values allowed ... remember I am 'Primitive' ... Ha ha ha ha")

        break

    if action.lower().strip() == "add" : print(f"{val1} + {val2} = {add(val1,val2)}")
    if action.lower().strip() == "subtract" : print(f"{val1} - {val2} = {subtract(val1,val2)}")
    if action.lower().strip() == "divide" : print(f"{val1} / {val2} = {divide(val1,val2)}")
    if action.lower().strip() == "multiply" : print(f"{val1} * {val2} = {multiply(val1,val2)}")


main()
