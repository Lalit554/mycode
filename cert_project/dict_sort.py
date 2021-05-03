# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:41:45 2021

@author: T3044LP
"""
####!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# Python code demonstrate the working of
# sorted() with lambda

# Initializing list of dictionaries
lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

# using sorted and lambda to print list sorted
# by age
print("The list printed sorting by age: ")
print(sorted(lis, key = lambda i: i['age']))

print ("\r")

# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
print("The list printed sorting by age and name: ")
print(sorted(lis, key = lambda i: (i['age'], i['name'])))

print ("\r")

# using sorted and lambda to print list sorted
# by age in descending order
print("The list printed sorting by age in descending order: ")
print(sorted(lis, key = lambda i: i['age'],reverse=True))
