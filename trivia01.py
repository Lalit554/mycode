#!/usr/bin/python3

import requests
import json
import html
import os

trivia = ""

def get_trivia():
    api = "https://opentdb.com/api.php?amount=1&category=29&difficulty=easy&type=multiple"
    r = requests.get(api)
    trivia = html.unescape(json.loads(r.text))
    print(trivia)

#def play_trivia():
    
def main():
    os.system('clear')
    get_trivia()
#    play_trivia()
    
if __name__ == "__main__":
    main()


