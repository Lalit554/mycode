# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:41:45 2021

@author: T3044LP
"""
####!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
#from IPython.display import HTML
import shutil
import requests
import datetime 
import json 
import pyexcel
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def list_Hazardous_Asteroids(ADict):
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
           Hazardous_Asteroid_Found = "Y"
                          
        if Hazardous_Asteroid_Found == "N": 
           print("No Hazardous Asteroids found !!!")
        
    print("\n\n")

def list_top_5_largest_asteroids(ADict):
    SortedADict = sorted(ADict, key = lambda i: i['absolute_magnitude_h'], reverse=True)
    
    if len(SortedADict) > 0:
       print("\n")
       print("*********************************************************")
       print("*******   List of Top 5 Largest Asteroids   *************")
       print("*********************************************************")
       #print("\n\n")
       print("Sr.No.    Astroid Id              Astroid_Name                    Magnitude_h")
       print("------    ----------              -----------------------------   -----------")
       for idx in range(0,5) :
           print("{}.        {}\t          {}\t                  {}".format(idx+1,SortedADict[idx].get("id"),SortedADict[idx].get("name"),SortedADict[idx].get("absolute_magnitude_h")))
    else:
           print("Asteroid List is Empty !!!\n\n")
        
    print("\n\n")

def filter_by_magnitude(ADict,Mag,criteria):
    if (len(ADict)) > 0:
       print("\n")
       print("************************************************************************************")
       print("****************   List of Asteroids with magnitude {}  {}   ***********************".format(criteria,Mag))
       print("************************************************************************************")
       print("Sr.No.    Astroid Id              Astroid_Name                    Magnitude_h")
       print("------    ----------              -----------------------------   -----------")


       for idx in range(0,len(ADict)):
           if criteria == ">=" :
              if float(ADict[idx].get("absolute_magnitude_h")) >= Mag:   
                 print("{}.        {}\t          {}\t                  {}".format(idx+1,ADict[idx].get("id"),ADict[idx].get("name"),ADict[idx].get("absolute_magnitude_h")))
           elif criteria == "<" :
              if float(ADict[idx].get("absolute_magnitude_h")) < Mag:   
                 print("{}.        {}\t          {}\t                  {}".format(idx+1,ADict[idx].get("id"),ADict[idx].get("name"),ADict[idx].get("absolute_magnitude_h")))
       print("\n\n")
    else: print("Asteroid List is Empty !!!\n\n")
        
    print("\n\n")


def bar_chart(ADict,DL):
    if len(ADict) > 0 and len(DL) > 0 :
       N = len(DL)
       Hazardous_Count = []
       Non_Hazardous_Count = []
       for idx in range(0,N):
           Hazardous_Count.append(0)
           Non_Hazardous_Count.append(0)

       for idx in range(0,len(ADict)):
           for DL_ctr in (0, len(DL)-1):
               if ADict[idx].get("Date") == DL[DL_ctr]:
                   break
           if ADict[idx].get("is_potentially_hazardous"):
              Hazardous_Count[DL_ctr] += 1
           else:
              Non_Hazardous_Count[DL_ctr] += 1

       ind = np.arange(N)
       width = 0.8

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
       plt.xticks(ind, DL)
       plt.yticks(np.arange(0, 50, 5))
       plt.legend((p1[0], p2[0]), ("Hazardous Count", "Non Hazardous Count"))

       # display the graph
       # plt.show() # you can try this on a Python IDE with a GUI if you'd like
       plt.savefig("Asteroid_bar_chart.png")

    else: print("Asteroid List is Empty !!!\n\n")

    print("\n")

           
    #if (len(ADict)) > 0:
    #   N = 
    #localnetMeans = (20, 35, 30, 35) #LAN length of outage (mins)
    #wanMeans = (25, 32, 34, 20) #WAN length of outage (min)
    #ind = np.arange(N)    # the x locations for the groups
    ## the width of the bars: can also be len(x) sequence
    #width = 0.35

    ## describe where to display p1
    #p1 = plt.bar(ind, localnetMeans, width)
    ## stack p2 on top of p1
    #p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    ## Describe the table metadata
    #plt.ylabel("Length of Outage (mins)")
    #plt.title("2018 Network Summary")
    #plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    #plt.yticks(np.arange(0, 81, 10))
    #plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    ## display the graph
    ## plt.show() # you can try this on a Python IDE with a GUI if you'd like
    #plt.savefig("/home/student/mycode/graphing/2018summary.png")
    ## save a copy to "~/static" (the "files" view)
    #plt.savefig("/home/student/static/2018summary.png")

    #else: print("Asteroid List is Empty !!!\n\n")



def parse_dict_and_create_exceldata(sdt,tdt):
    """Run time code"""
    # create r, which is our request object
    #Uri="https://api.nasa.gov/neo/rest/v1/feed?start_date="+sdt+"&end_date="+tdt+"&api_key=DEMO_KEY"
    #r = requests.get(Uri)
    #data = r.json()
    data = json.load(open("asteroid_data1.json","r"))

    Aster_Objs = { "near_earth_objects" : data.get("near_earth_objects") }

    #data.pop("links")
    #data.pop("element_count")
    
    astroid_info = []
    astroid_uniq_info = []
    Date_List = []
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
                    Uniq_Asteriod = "Y"
                    for aptr in range(0,len(astroid_info)-1):
                        #print(astroid_info[aptr].get("id")) 
                        if astroid_info[aptr].get("id") == Astroid_id:
                           #print(f"Astroid_id = {Astroid_id} already loaded !!")
                           Uniq_Asteriod = "N"
                           break
                    if Uniq_Asteriod == "N" :
                       astroid_uniq_info.append(astroid_data)
      
    #print(astroid_info,"\n\n")
    if astroid_data :
        return True, astroid_info, astroid_uniq_info, Date_List
    else: return False , astroid_info, astroid_uniq_info, Date_List

#****

def get_user_input():
    while True:
        #*** Ensure user enters a valid date as "FROM" date ***
        while True:
              from_date = input("Enter FROM Date (YYYY-MM-DD) : ")
              if len(from_date.strip()) == 10:
                 year,month,day = from_date.split("-") 
                 isValidDate = True 
                 try:
                    datetime.datetime(int(year),int(month),int(day))
                 except ValueError :
                    isValidDate = False
                    print("Invalid Date entered, please try again ...")
                 if isValidDate : break
          
        #*** Ensure user enters a valid date as "TO" date ***
        while True:
              to_date = input("Enter  TO  Date (YYYY-MM-DD) : ")
              if len(to_date.strip()) == 10:
                 year,month,day = to_date.split("-") 
                 isValidDate = True 
                 try:
                    datetime.datetime(int(year),int(month),int(day))
                 except ValueError :
                    isValidDate = False
                    print("Invalid Date entered, please try again ...")
                 if isValidDate : break

        #*** Validate "from" date is less than "to" date ***
        #*** and they are only two days apart            ***

        year,month,day = from_date.split("-") 
        fdt = datetime.datetime(int(year),int(month),int(day))

        year,month,day = to_date.split("-") 
        tdt = datetime.datetime(int(year),int(month),int(day))
        
        
        if (tdt - fdt).days in range(0,3) : 
            return from_date, to_date
            break
        else : print("Invalid Date range / exceeds two days, please try again ...")

#****

def main():
    print("*****    Welcome to Asteriod Exploration    *****\n")
    print("\nLimit you exploration to only two days at a time\n")

    while True:                       # Loop until user chooses to end the program
          (fdate,tdate)=get_user_input()            # Get Date range from user
          #print(f"fdate = {fdate} : tdate = {tdate}")
          #break
          (Data_Found,Astroid_Dict,Uniq_Astroid_Dict,DateLst) = parse_dict_and_create_exceldata(fdate,tdate)
          if not Data_Found :
              print("No Data found for specified Date Range !!!\n")
          else:
              while True:
                  print("\n")
                  print("(1) : Download Astroid Info to Excel - Astroid_Info.xls")
                  print("(2) : List Hazardous Astroid Names")
                  print("(3) : Top 5 largest Asteroids")
                  print("(4) : List Asteroids with magnitude >= 25")
                  print("(5) : List Asteroids with magnitude  < 20")
                  print("(6) : Bar Chart of Hazardous Asteroids")
                  print("(7) : Change Date Selection")
                  print("(Q) : Quit")

                  opt_list = [ '1', '2', '3', '4', '5', '6', '7', 'Q' ]
                  while True:
                      user_opt = input("Enter Option Number (1-7,Q) >>> ").strip().upper()
                      if user_opt not in opt_list :
                         print("\nInvalid Option, please try again ...")
                      else : break
                  #print(Astroid_Dict,"\n\n")
              
                  if   user_opt == '1':
                       pyexcel.save_as(records=Astroid_Dict, dest_file_name='Astroid_Info.xls')
                       #shutil.copy("Astroid_Data.html","/home/student/static/Astroid_Data.html")
                  elif user_opt == '2':
                       list_Hazardous_Asteroids(Uniq_Astroid_Dict)
                  elif user_opt == '3':
                       list_top_5_largest_asteroids(Uniq_Astroid_Dict)
                  elif user_opt == '4':
                       filter_by_magnitude(Uniq_Astroid_Dict,25,">=")
                  elif user_opt == '5':
                       filter_by_magnitude(Uniq_Astroid_Dict,20,"<")
                  elif user_opt == '6':
                       bar_chart(Astroid_Dict,DateLst)
                  elif user_opt == '7' or user_opt == 'Q' :
                       break 
              
          if user_opt.upper() == 'Q' : break
    
main()

