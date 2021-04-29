#!/usr/bin/env python3

import os

os.system('clear')

comic_publisher = {}

with open("comic_book_data.txt", "r") as comic_data :
     for comic_book_info in comic_data :
         publisher = comic_book_info.split(";")[3]
         if comic_publisher == {} :
             comic_publisher[publisher] = 1
         elif comic_publisher.get(publisher) :
             comic_publisher[publisher] = int(comic_publisher.get(publisher)) + 1
         else :
             comic_publisher[publisher] = 1

# print number of comics owned by publisher
for key, value in comic_publisher.items() :
    if key == "" :
       key = "Unknown Publisher"
    print(f"Number of comics published by -> {key.strip()} = {value}")


