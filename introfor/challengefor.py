#!/usr/bin/env python3
# create dictionary of farms

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

nonveg = [ "sheep", "cows", "pigs", "chickens", "llamas", "cats"] 

print("\nPart 1 of Challenge\n")
# loop that returns all the animals from the NE Farm!
for locations in farms:
    farm_location=locations.get("name")
    if farm_location == "NE Farm" :
        for products in locations.get("agriculture"):
            print(products)

print("\nPart 2 of Challenge\n")
# Return the plants/animals that are raised on farm requested by user
resp=9
while resp not in range(0,len(farms)) :
   print("select farm from the list to get product list ")
   idx = 1
   for locations in farms:
       print(f"{idx}",locations.get("name"))
       idx += 1
   resp = int(input(">>> ")) - 1
     
farm_chosen = farms[resp]
#print("farm_chosen")
#print(farm_chosen)

for products in farm_chosen.get("agriculture"):
    print(products)

print("\nPart 3 of Challenge\n")
# Return the animals only that are raised on farm requested by user
resp=9
while resp not in range(0,len(farms)) :
   print("select farm from the list to get product list ")
   idx = 1
   for locations in farms:
       print(f"{idx}",locations.get("name"))
       idx += 1
   resp = int(input(">>> ")) - 1
     
farm_chosen = farms[resp]
#print("farm_chosen")
#print(farm_chosen)

for products in farm_chosen.get("agriculture"):
    #print ("products = " + products)
    for anm in nonveg :
        #print ("anm = "+anm)
        if products == anm :
           print(products)
