"""
Created on Sat May  1 10:41:45 2021

@author: Lalit Patil

@Description: Python Basics Certification Project
"""
####!/usr/bin/env python3

import datetime 
from datetime import date
from os import path
import re
import requests
import pprint
import operator 
import json 
import pyexcel
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def get_observation_dates():
    ''' Prompt user to enter a date range (maximum of 7 days) to be used to download asteroid observation data.
        Validate entered observation dates, date range values and that range does not exceed 7 days.
        Return validated "Observation From Date" and "Observation To Date".

        Usage       : get_observation_dates()

        Parameters  : None

        Returns     : 
            from_date                    ==> Start of Observation Date
            to_date                      ==> End of Observation Date

    '''
    while True:
        while True:                                                             #*** Ensure user enters a valid date as "FROM" date ***
              from_date = input("Enter Observation FROM Date (YYYY-MM-DD) : ")
              if len(from_date.strip()) == 10:
                 year,month,day = from_date.split("-") 
                 isValidDate = True 
                 try:
                    frdate=datetime.date(int(year),int(month),int(day))
                    if frdate >= date.today():
                       print("'FROM' Date must be prior to today, please try again ...")
                       isValidDate = False
                 except ValueError :
                    isValidDate = False
                    print("Invalid Date entered, please try again ...")
                 if isValidDate : break
          
        
        while True:                                                            #*** Ensure user enters a valid date as "TO" date ***
              to_date = input("Enter Observation  TO  Date (YYYY-MM-DD) : ")
              if len(to_date.strip()) == 10:
                 year,month,day = to_date.split("-") 
                 isValidDate = True 
                 try:
                    todate=datetime.date(int(year),int(month),int(day))
                    if todate >= date.today() or todate < frdate:              #*** Validate "from" date is less than "to" date ***
                       print("' TO ' Date must be prior to today and after 'FROM' Date, please try again ...")
                       isValidDate = False
                 except ValueError :
                    isValidDate = False
                    print("Invalid Date entered, please try again ...")
                 if isValidDate : break

        # convert "FROM" date entered by user into date format
        year,month,day = from_date.split("-") 
        fdt = datetime.date(int(year),int(month),int(day))

        # convert "TO" date entered by user into date format
        year,month,day = to_date.split("-") 
        tdt = datetime.date(int(year),int(month),int(day))
        
        
        if (tdt - fdt).days in range(0,8) :                                    #*** Validate date range is no more than 7 days  *** 
            return from_date, to_date
            break
        else : 
            print("Invalid Date range / exceeds 7 days, please try again ...")

#****

def download_nasa_json():
    ''' Prompt user to enter a date range (maxium of 7 days) to be used to download asteroid observation data.
        Download asteroid observation data from api.nasa.gov using DEMO_KEY for the specifed date range
        and save the JSON output to "asteriod_data.json" file in current directory/folder.


        Usage       : download_nasa_json(sdt,tdt)

        Parameters  :
            sdt = FROM  Observation Date  (YYYY-MM-DD)
            tdt =  TO   Observation Date  (YYYY-MM-DD)

        Returns     : None

    '''
    (sdt,tdt)=get_observation_dates()            # Get Date range from user

    Uri="https://api.nasa.gov/neo/rest/v1/feed?start_date="+sdt+"&end_date="+tdt+"&api_key=DEMO_KEY"
    r = requests.get(Uri).json()
    json_file=open("asteroid_data.json","w") 
    for json_line in  json.dumps(r,indent=2) :
        json_file.write(json_line) 
    json_file.close()
    json_file=open("asteroid_data.json","r")
    json_data=json.load(json_file)
    json_file.close()
    if json_data.get("element_count") == 0:
       print("No Data found for specified Date Range !!!\n")

#****

def parse_dict_and_create_exceldata():
    ''' parse downloaded JSON file ("asteroid_data.json") and create following lists based on keys and values in dictionary "near_earth_objects"
        a) List of Unique Asteroid Objects and related inforamtion             ==> "astroid_info []"
        b) List of Asteroid Objects and related information by Date            ==> "astroid_uniq_info []"
        c) Observation Date List                                               ==> "Date_List []"


        Usage       : parse_dict_and_create_exceldata()

        Parameters  : None

        Returns     : 
            astroid_info[]               ==> List of Asteroids and related information by Date. Same Asteroid could exist for multiple observation dates.
            astroid_uniq_info[]          ==> List of Unqiue Asteroids and related information regardless of observation date.
            Date_List[]                  ==> List of Observation Dates for which Asteroid information  is available in astroid_info[] and astroid_uniq_info[]

    '''

    data = json.load(open("asteroid_data.json","r"))
    Aster_Objs = { "near_earth_objects" : data.get("near_earth_objects") }

    #data.pop("links")
    #data.pop("element_count")
    
    astroid_info = []
    astroid_uniq_info = []
    Date_List = []
    astroid_data = []
    for (RootKey,ValueDict) in Aster_Objs.items():    # root-level dictionary
        #print(RootKey)
        for Observ_Date in ValueDict.keys():  # Loop for each Date
            #print(Observ_Date)
            Date_List.append(Observ_Date)
            for Astroid_List in ValueDict.values(): # Asteriod Information for each Date
                for idx in range(0,len(Astroid_List)):
                    Astroid_Link = Astroid_List[idx].get("links").get("self")
                    Astroid_id = Astroid_List[idx].get("id")
                    Astroid_Neo_Ref_ID = Astroid_List[idx].get("neo_reference_id")
                    Astroid_name = Astroid_List[idx].get("name")
                    Astroid_nasa_jpl_url = Astroid_List[idx].get("nasa_jpl_url")
                    Astroid_magnitude_h = Astroid_List[idx].get("absolute_magnitude_h")
                    Astroid_est_diam_km_min = Astroid_List[idx].get("estimated_diameter").get("kilometers").get("estimated_diameter_min")
                    Astroid_est_diam_km_max = Astroid_List[idx].get("estimated_diameter").get("kilometers").get("estimated_diameter_max")
                    Astroid_est_diam_m_min = Astroid_List[idx].get("estimated_diameter").get("meters").get("estimated_diameter_min")
                    Astroid_est_diam_m_max = Astroid_List[idx].get("estimated_diameter").get("meters").get("estimated_diameter_max")
                    Astroid_est_diam_miles_min = Astroid_List[idx].get("estimated_diameter").get("miles").get("estimated_diameter_min")
                    Astroid_est_diam_miles_max = Astroid_List[idx].get("estimated_diameter").get("miles").get("estimated_diameter_max")
                    Astroid_est_diam_feet_min = Astroid_List[idx].get("estimated_diameter").get("feet").get("estimated_diameter_min")
                    Astroid_est_diam_feet_max = Astroid_List[idx].get("estimated_diameter").get("feet").get("estimated_diameter_max")
                    Astroid_is_pot_hazardous = Astroid_List[idx].get("is_potentially_hazardous_asteroid")
                    Astroid_close_approach_date = Astroid_List[idx].get("close_approach_data")[0].get("close_approach_date")
                    Astroid_close_approach_date_full = Astroid_List[idx].get("close_approach_data")[0].get("close_approach_date_full")
                    Astroid_epoch_date_close_approach = Astroid_List[idx].get("close_approach_data")[0].get("epoch_date_close_approach")
                    Astroid_rel_velo_km_sec = Astroid_List[idx].get("close_approach_data")[0].get("relative_velocity").get("kilometers_per_second")
                    Astroid_rel_velo_km_hr = Astroid_List[idx].get("close_approach_data")[0].get("relative_velocity").get("kilometers_per_hour")
                    Astroid_rel_velo_miles_hr = Astroid_List[idx].get("close_approach_data")[0].get("relative_velocity").get("miles_per_hour")
                    Astroid_miss_dist_astronm = Astroid_List[idx].get("close_approach_data")[0].get("miss_distance").get("astronomical")
                    Astroid_miss_dist_lunar = Astroid_List[idx].get("close_approach_data")[0].get("miss_distance").get("lunar")
                    Astroid_miss_dist_km = Astroid_List[idx].get("close_approach_data")[0].get("miss_distance").get("kilometers")
                    Astroid_miss_dist_miles = Astroid_List[idx].get("close_approach_data")[0].get("miss_distance").get("miles")
                    Astroid_orbiting_body = Astroid_List[idx].get("close_approach_data")[0].get("orbiting_body")
                    Astroid_is_senrty_obj = Astroid_List[idx].get("is_sentry_object")

                    astroid_data = {"Date" : Observ_Date , 
                                    "links" : Astroid_Link , 
                                    "id" : Astroid_id , 
                                    "neo_reference_id" : Astroid_Neo_Ref_ID , 
                                    "name" : Astroid_name , 
                                    "nasa_jpl_url" : Astroid_nasa_jpl_url , 
                                    "absolute_magnitude_h" : Astroid_magnitude_h ,
                                    "min_est_km_diameter" : Astroid_est_diam_km_min , 
                                    "max_est_km_diameter" : Astroid_est_diam_km_max ,
                                    "min_est_m_diameter" : Astroid_est_diam_m_min ,
                                    "max_est_m_diameter" : Astroid_est_diam_m_max , 
                                    "min_est_miles_diameter" : Astroid_est_diam_miles_min ,
                                    "max_est_miles_diameter" : Astroid_est_diam_miles_max , 
                                    "min_est_feet_diameter" : Astroid_est_diam_feet_min ,
                                    "max_est_feet_diameter" : Astroid_est_diam_feet_max , 
                                    "is_potentially_hazardous" : Astroid_is_pot_hazardous ,
                                    "close_approach_date" : Astroid_close_approach_date , 
                                    "epoch_date_close_approach" : Astroid_epoch_date_close_approach ,
                                    "close_approach_date_full" : Astroid_close_approach_date_full ,
                                    "relative_velocity_km_per_sec" : Astroid_rel_velo_km_sec , 
                                    "relative_velocity_km_per_hr" : Astroid_rel_velo_km_hr ,
                                    "relative_velocity_miles_per_hr" : Astroid_rel_velo_miles_hr , 
                                    "miss_distance_in_astro_units" : Astroid_miss_dist_astronm ,
                                    "miss_distance_in_lunar_units" : Astroid_miss_dist_lunar , 
                                    "miss_distance_in_km_units" : Astroid_miss_dist_km ,
                                    "miss_distance_in_miles_units" : Astroid_miss_dist_miles , 
                                    "orbiting_body" : Astroid_orbiting_body ,
                                    "is_sentry_object" : Astroid_is_senrty_obj }

                    astroid_info.append(astroid_data)

                    Uniq_loaded = "N"
                    for aptr in range(0,len(astroid_uniq_info)):
                        if astroid_uniq_info[aptr].get("id") == Astroid_id:
                           #print(f"Astroid_id = {Astroid_id} already loaded !!")
                           Uniq_loaded = "Y"
                           break
                    if Uniq_loaded == "N":
                           astroid_uniq_info.append(astroid_data)
      
    if astroid_data :
        return True, astroid_info, astroid_uniq_info, Date_List
    else: return False , astroid_info, astroid_uniq_info, Date_List

#****

def list_Hazardous_Asteroids(ADict,NonEmptyDict):
    ''' Read [Unique List] of Asteroids and related observation data extracted from api.nasa.gov. 
        Print list of Asteroids which are deemed "Hazardous"

        Usage       : list_Hazardous_Asteroids(ADict,NonEmptyDict) 

        Parameters  :
            ADict        = Dictionary containing unique list of asteroids and related observation data
            NonEmptyDict = Empty Status of "ADict" dictionary (True/False)

        Returns     : None

    '''

    if not NonEmptyDict :
       print("\n\nAsteroid Information file is missing or empty !!!\n")
    else:
       Hazardous_Asteroid_Found="N"
       #print(type(ADict))
       for idx in range(0,len(ADict)):
           h_ctr = 0    # Count Hazardours Asteroids
           #print("{}. Name = {} is potentially Hazardous {}".format(idx,ADict[idx].get("name"),ADict[idx].get("is_potentially_hazardous")))
           if ADict[idx].get("is_potentially_hazardous"):
              h_ctr += 1
              if h_ctr == 1 :
                 print("\n")
                 print("************************************************")
                 print("*******   List of Hazardous Astroids   *********")
                 print("************************************************")
                 #print("\n\n")
                 print("Sr.No.    Astroid Id         Astroid_Name                 ")
                 print("------    ----------         -----------------------------")
                 print("{}.        {}            {}".format(h_ctr,ADict[idx].get("id"),ADict[idx].get("name")))
              else:
                 print("{}.        {}            {}".format(h_ctr,ADict[idx].get("id"),ADict[idx].get("name")))

              Hazardous_Asteroid_Found = "Y"
                          
       if Hazardous_Asteroid_Found == "N": 
          print("No Hazardous Asteroids found !!!")
        
    print("\n\n")

#****

def list_top_5_largest_asteroids(ADict,NonEmptyDict):
    ''' Read [Unique List] of Asteroids and related observation data extracted from api.nasa.gov. 
        Print list of top 5 largest Asteroids

        Usage       : list_top_5_largest_asteroids(ADict,NonEmptyDict) 

        Parameters  :
            ADict        = Dictionary containing unique list of asteroids and related observation data
            NonEmptyDict = Empty Status of "ADict" dictionary (True/False)

        Returns     : None

    '''

    if not NonEmptyDict :
       print("\n\nAsteroid Information file is missing or empty !!!\n")
    else:
       SortedADict = sorted(ADict, key = lambda i: i['absolute_magnitude_h'], reverse=True)
       print("\n")
       print("*********************************************************")
       print("*******   List of Top 5 Largest Asteroids   *************")
       print("*********************************************************")
       #print("\n\n")
       print("Sr.No.    Astroid Id              Astroid_Name                    Magnitude_h")
       print("------    ----------              -----------------------------   -----------")
       for idx in range(0,5) :
           print("{}.        {}\t          {}\t                  {}".format(idx+1,SortedADict[idx].get("id"),SortedADict[idx].get("name").strip(),SortedADict[idx].get("absolute_magnitude_h")))
        
    print("\n\n")

#****

def get_magnitude_crieria():
    ''' Prompt user to enter a criteria to filter Asteroids by.                                                  
        Validate entered criteria and Return validated criteria comparison operator and comparison value.

        Usage       : get_magnitude_crieria()

        Parameters  : None

        Returns     : 
            Mag_H                        ==> {VALUE} to compare with Asteroid's Absolute Magnitude H
            Compare_Operator             ==> {COMPARISON OPERATOR} to be used to perform the comparison
                                              Possible values are :
                                                     ">"  
                                                     "<"
                                                     ">="
                                                     "<="
                                                     "="
                                                     "!="

    '''

    ops = ['>' , '<' , '>=' , '<=' , '=' , '!=' , '<>' , '==' ]

    Compare_operator = ""
    Meg_H            = ""

    while Compare_operator not in ops:
          Compare_operator=input(f"\n\nEnter a valid comparison opertor {ops} : ")

    while not Meg_H.replace('.','').isnumeric() :
          Meg_H=input("Enter Absolute Magnitude (H) value to use for comparision : ")

    print("\n\n")
    return Meg_H,Compare_operator

#****

def filter_by_magnitude(ADict,Mag,criteria,NonEmptyDict):
    ''' Read [Unique List] of Asteroids and related observation data extracted from api.nasa.gov. 
        Print list of Asteroids which satisfy the user query criteria of Asteroid's absolute magnitude (H).

        Usage       : filter_by_magnitude(ADict,Mag,criteria,NonEmptyDict) 

        Parameters  :
            ADict        = Dictionary containing unique list of asteroids and related observation data
            Mag          = Asteroid's Absolute Magnitude (H)
            criteria     = comparison operator to be used to compare Asteroid's absolute magnitude (H) with "Mag" parameter. 
                           Acceptable parameter /argument values are :
                           ">"  
                           "<"
                           ">="
                           "<="
                           "="
                           "!="
            NonEmptyDict = Empty Status of "ADict" dictionary (True/False)

        Returns     : None

    '''

    ops = {'>' : operator.gt , '<' : operator.lt, '>=' : operator.ge, '<=' : operator.le, '=' : operator.eq, '!=' : operator.ne, '<>' : operator.ne, '==' : operator.eq}


    if not NonEmptyDict :
       print("\n\nAsteroid Information file is missing or empty !!!\n")
    else:
       print("\n")
       print("************************************************************************************")
       print("****************   List of Asteroids with magnitude {}  {}   ***********************".format(criteria,Mag))
       print("************************************************************************************")
       print("Sr.No.    Astroid Id              Astroid_Name                    Magnitude_h")
       print("------    ----------              -----------------------------   -----------")

       ctr=0
       for idx in range(0,len(ADict)):
           if ops[criteria](float(ADict[idx].get("absolute_magnitude_h")),float(Mag)):   
              ctr += 1
              print("{}.        {}\t          {}\t                  {}".format(ctr,ADict[idx].get("id"),ADict[idx].get("name").strip(),ADict[idx].get("absolute_magnitude_h")))

    print("\n\n")

#****

def bar_chart(ADict,DL,NonEmptyDict):
    ''' Plot a bar chart for "Hazardous" vs. "Non Hazardous" asteroid counts by observation date and save it to a file "Asteroid_bar_chart.png"

        Usage       : filter_by_magnitude(ADict,DL,NonEmptyDict) 

        Parameters  :
            ADict        = Dictionary containing list of asteroids and related observation data by observation dates
            DL           = List of Observation Dates
            NonEmptyDict = Empty Status of "ADict" dictionary (True/False)

        Returns     : None

    '''

    if not NonEmptyDict :
       print("\n\nAsteroid Information file is missing or empty !!!\n")
    else:
       N = len(DL)
       Hazardous_Count = []
       Non_Hazardous_Count = []
       for idx in range(0,N):
           Hazardous_Count.append(0)
           Non_Hazardous_Count.append(0)

       max_ytick = 0
       for idx in range(0,len(ADict)):
           for DL_ctr in range(0, len(DL)):
               if ADict[idx].get("Date") == DL[DL_ctr]:
                   break
           if ADict[idx].get("is_potentially_hazardous"):
              Hazardous_Count[DL_ctr] += 1
           else:
              Non_Hazardous_Count[DL_ctr] += 1
           if (Hazardous_Count[DL_ctr] > max_ytick) : max_ytick = Hazardous_Count[DL_ctr]
           if (Non_Hazardous_Count[DL_ctr] > max_ytick) : max_ytick = Non_Hazardous_Count[DL_ctr]

       print("Hazardous_Count = ",Hazardous_Count)
       print("Non_Hazardous_Count = ",Non_Hazardous_Count)

       ind = np.arange(N)
       #width = 0.8     #if only 2 dates
       width = 1.6 / N   #if 7 dates

       HCnt = []
       NHCnt = []
       for idx in range(0,N):
           HCnt.append(Hazardous_Count[idx])
           NHCnt.append(Non_Hazardous_Count[idx])

       p1 = plt.bar(ind, HCnt, width)
       p2 = plt.bar(ind, NHCnt, width, bottom=Hazardous_Count)

       # Describe the table metadata
       plt.ylabel("Asteroid Count")
       plt.title("Asteroid Count Summary by Day")
       plt.autoscale()
       plt.xticks(ind, DL, fontsize='xx-small')
       #plt.yticks(np.arange(0, 50, 5))    #if only 2 dates
       plt.yticks(np.arange(0, max_ytick, int(max_ytick/10)))
       plt.legend((p1[0], p2[0]), ("Hazardous Count", "Non Hazardous Count"))

       # display the graph
       # plt.show() # you can try this on a Python IDE with a GUI if you'd like
       plt.savefig("Asteroid_bar_chart.png")

    print("\nBar chart saved to 'Asteroid_bar_chart.png' file\n")

#****

def main():
    ''' Asteroid Data Analysis program.
            (a) Extract Asteroid Data from api.nasa.gov for up to  7 days
            (b) Parse and store asteroid data extracted in JSON file for analysis

        Usage       : python3 alta3research-pythoncert01.py

        Parameters  : None

        Returns     : None

    '''

    print("*************************************************")
    print("*****    Welcome to Asteriod Exploration    *****")
    print("*************************************************")
    print("( !! Limit you exploration to only seven days !! )\n")

    errmsg=""
    Data_Found = False
    Astroid_Dict = []
    Uniq_Astroid_Dict = []
    DateLst = []

    #print("File Size = {}".format(path.getsize("asteroid_data.json")))
    if path.exists("asteroid_data.json") and path.getsize("asteroid_data.json") >= 448 :
       (Data_Found,Astroid_Dict,Uniq_Astroid_Dict,DateLst) = parse_dict_and_create_exceldata()
       if not Data_Found : 
           errmsg = "\n\nAsteroid Information file is EMPTY, choose option '1' to download data first !!!\n"
       else: 
           Data_Found = True
    else:
        errmsg = "\n\nAsteroid Information file NOT FOUND, choose option '1' to download data first !!!\n"

    if not Data_Found :
       print(errmsg)

    while True:
          print("\n")
          print("(1) : Download Astroid Data from api.nasa.gov (max 7 days)")
          print("(2) : Convert  Astroid Info to Excel - Astroid_Info.xls")
          print("(3) : List Hazardous Astroid Names")
          print("(4) : Top 5 largest Asteroids")
          print("(5) : Query Asteroids by magnitude")
          print("(6) : Bar Chart of Hazardous Asteroids")
          print("(7) : Change Date Selection")
          print("(Q) : Quit")

          opt_list = [ '1', '2', '3', '4', '5', '6', '7', 'Q' ]
          user_opt = input("Enter Option Number (1-7,Q) >>> ").strip().upper()
          if user_opt not in opt_list :
             print("\nInvalid Option, please try again ...")
          elif user_opt == '1':
               download_nasa_json()
               (Data_Found,Astroid_Dict,Uniq_Astroid_Dict,DateLst) = parse_dict_and_create_exceldata()
          elif user_opt == '2':
               pyexcel.save_as(records=Astroid_Dict, dest_file_name='Astroid_Info.xls')
               print("\nAsteroid Data downloded to excel file 'Astroid_Info.xls'\n")
          elif user_opt == '3':
               list_Hazardous_Asteroids(Uniq_Astroid_Dict,Data_Found)
          elif user_opt == '4':
               list_top_5_largest_asteroids(Uniq_Astroid_Dict,Data_Found)
          elif user_opt == '5':
               (Asize,Acriteria)=get_magnitude_crieria()
               filter_by_magnitude(Uniq_Astroid_Dict,Asize,Acriteria,Data_Found)
          elif user_opt == '6':
               bar_chart(Astroid_Dict,DateLst,Data_Found)
          elif user_opt == '7':
               download_nasa_json()
               (Data_Found,Astroid_Dict,Uniq_Astroid_Dict,DateLst) = parse_dict_and_create_exceldata()
          elif user_opt == 'Q' :
               break 

    
#****

if __name__ == "__main__":
    main()
