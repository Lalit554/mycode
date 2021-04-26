#!/usr/bin/env python3

# create a list called list1
icecream = ["flavors", "salty"]

icecream.append(99)

print("Enter your name :\n")
uname= input(">> ")

#print(f"{} {}, and {} chooses to be {}",icecream[-1],icecream[0],uname,icecream[-2])

print("{} {}, and {} chooses to be {}".format(icecream[-1],icecream[0],uname,icecream[-2]))
