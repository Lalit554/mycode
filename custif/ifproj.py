#!/usr/bin/env python3

import random

movie_releases = { "Pieces of a Woman" : "NETFLIX" ,
                   "Herself" : "AMAZON PRIME" ,
                   "The Reason I Jump" : "THEATERS" ,
                   "Locked Down" : "HBO" ,
                   "Underwater" : "THEATERS" ,
                   "A Dog's Way Home" : "THEATERS" ,
                   "The Kid Who Would be King" : "THEATERS" ,
                   "Uncorked" : "NETFLIX" ,
                   "Sergio" : "NETFLIX" }

ViewingAt = [ "THEATERS" , "NETFLIX" , "HBO" , "AMAZON PRIME" ]

array_size = len(movie_releases) 
#print(array_size)

print("Welcome to list of Movies released at : ")
Idx = 0
while Idx < len(ViewingAt) :
    print( ViewingAt[Idx] )
    Idx = Idx + 1

print("\n\nLet's check if can recognize the movie and guess where it was released ...")

while True:

    key_num = random.randint(0,len(movie_releases)-1)
    #print(key_num)

    movie_list = list(movie_releases)
    movie_name = movie_list[key_num]

    print("\n\nWhere was movie '{}' released ? ".format(movie_name))
    Released_At = movie_releases.get(movie_name)
    #print("Movie Released at = " + movie_releases.get(movie_name))

    Try_num = 1
    resp_correct = "N"
    while Try_num <= 3 :

       User_Resp = input(">>> ")
       User_Resp = User_Resp.upper()

       #print("Try_num = {}".format(Try_num))

       if User_Resp not in ViewingAt and Try_num < 3:
           Idx = 0
           print("Choose from following list only")
           while Idx < len(ViewingAt) :
               print( ViewingAt[Idx] )
               Idx = Idx + 1
           print("\nTry again ...")
       elif User_Resp == Released_At :
           print("\nBingo !! That is correct !!")
           resp_correct = "Y"
           break
       
       Try_num = Try_num + 1

    if resp_correct == "N" :
       print("Nice Try, but ....")
       print("Movie '{}' was released at {} ".format(movie_name,Released_At))

    print("\n\nWant to play again (Y/N) ? ")
    cont_resp = " "
    while cont_resp.lower() not in ["y" , "n"] :
        cont_resp = input(">>  ")

    if cont_resp.lower() == "n" : 
        break
