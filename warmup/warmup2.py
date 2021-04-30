#!/usr/bin/env python3  
# corrected the path and "python" version

num=0
for num in range(1,101):
    div_by=""
    if num % 3 == 0 : 
       div_by = "3" 
    if num % 5 == 0 : 
       div_by = div_by + "5"

    if div_by == "35" : 
        print("FizzBuzz")
    elif div_by == "3" : print("Fizz")
    elif div_by == "5" : print("Buzz")
    else :
        print(f"{num} \n")
