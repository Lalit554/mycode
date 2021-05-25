#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint
import pandas as pd

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        #pprint.pprint(got_dj)
        
        combined_book_list = []
        combined_book_list.extend(got_dj["books"])
        combined_book_list.extend(got_dj["povBooks"])

        if got_dj["name"]:
           print("Author : "+ got_dj["name"])
        else:
           print("Alias : ",*got_dj["aliases"],sep="\n")

        if not got_dj["allegiances"] :
            print("\tHouse :  N/A")
        else:
            print("\tHouse :")
            for houses in got_dj["allegiances"]:
                print("\t\t"+requests.get(houses).json()["name"])

        if not combined_book_list:
            print("\tList of Books : N/A")
        else:
            print("\tList of Books : ")
            for book_url in combined_book_list:
                print("\t\t"+requests.get(book_url).json()["name"])
        

if __name__ == "__main__":
        main()

