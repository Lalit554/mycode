#!/usr/bin/python3

import requests
import json
import argparse
import os

cf=""

def returncreds(cred_file):
    with open(cred_file,"r") as mycreds:
         nasacreds = mycreds.read()
    return "api_key="+nasacreds.strip("\n")

def load_rover_dict():
    with open("rover_list.json","r") as json_file:
         rovers = json.load(json_file)
    return rovers

def validate_user_response(cp,prompt,choices):
    resp=""
    print(cp,*choices,sep="\n")
    while resp not in choices:
       resp=input(prompt).lower()
       if resp  == "q" : 
           break
       elif resp not in choices: print("Invalid selection, try again !!  (Q) = Quit")
    return resp
    
def select_rover(rover_dict):
    choice_prompt="Available rovers to choose from :"
    User_prompt="Choose rover name : "
    user_response=validate_user_response(choice_prompt,User_prompt,rover_dict.keys())
    return user_response

def select_camera(rover_dict,rname):
    choice_prompt="Available cameras to choose from :"
    User_prompt="Choose camera name : "
    user_response=validate_user_response(choice_prompt,User_prompt,rover_dict[rname])
    return user_response
          

def print_image_links(rname,cname,cfile):
    base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/"
    NASA_URL=base_url+rname+"/photos?sol=1000&camera="+cname+"&"+returncreds(cfile)
    #nasa_photo = urllib.request.urlopen(NASA_URL)
    r = requests.get(NASA_URL)
    nasa_photo_dict = r.json()
    #for json_line in json.dumps(r,indent=2) :
    #    nasa_photo_dict = nasa_photo_dict.extend(json_line)
    #print(nasa_photo_dict)
    x = nasa_photo_dict.values()
    print(x["img_src"])
    #print(f"Links to {rname} rover photos taken by camera '{cname}' :", *nasa_photo_dict["img_src"],sep="\n")

def main():
    os.system('clear')
    rover_dict=load_rover_dict()
    rover_name=select_rover(rover_dict)
    if rover_name != 'q' : cam_name=select_camera(rover_dict,rover_name)
    if rover_name != 'q' and cam_name != 'q' : print_image_links(rover_name,cam_name,cf)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='nasa_rover_01')
    parser.add_argument("--credfile",help="Credential file location and name")
    args = parser.parse_args()
    if not args.credfile:
        parser.print_help()
    else: 
        cf=args.credfile
        main()


