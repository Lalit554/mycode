#!/usr/bin/env python3

## create a dictionary
heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "magic",
    "archenemy": "Voldemort",},
"captain america":
    {"real name": "Steve Rogers",
    "powers": "frisbee shield",
    "archenemy": "Hydra",}
        }

repeat = "Y"

while repeat.upper() == "Y" :
   print("Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz) ")
   char_name = input(">>  ")


   print("What statistic do you want to know about? (real name, powers, archenemy) ")
   char_stat = input(">>  ")

   if (heroes.get(char_name.lower(),"Name not found") == "Name not found") :
      char_value="Not Defined" 
   else :
      char_value=heroes[char_name.lower()].get(char_stat.lower(),"Unknown Stat") 

   print(char_value)

   print("{}'s  {} is : {}".format(char_name,char_stat,char_value))

   #challenge 1
   print("{}'s  {} is : {}".format(char_name.title(),char_stat,char_value.title()))

   #challenge 3
   repeat = " "
   while repeat.upper() != "Y" and repeat.upper() != "N" :

      print("Would you like to try again? (Y/N) ")
      repeat=input(">> ")



