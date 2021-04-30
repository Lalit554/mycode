#!/usr/bin/env python3  
# corrected the path and "python" version
fruitcompanies= [{"name":"Zesty","employees":["Ajay","Ashfaq","Bob","Brian","Chad F.", "Chad H."]},
                 {"name":"Ripe.ly","employees":["Eric","Gibran", "Chad","Idris","Juan","Julian"]},
                 {"name":"FruitBee","employees":["Kulwinder","Lalit","Chad","Michael","Milford","Scott"]},{"name":"JuiceGrove","employees":["Chad","Srini","Srinivasa","Vasanti","Vimal"]}]


def collegues(emplist,coname,exclname=""):
    for idx in range(0,len(emplist)):
        for (keys, values) in emplist[idx].items():
            if values == coname :
                print(f"Employees in Company = {values} :")
                for empname in emplist[idx].get("employees") :
                    if empname != exclname : print(empname)

def main():
    colist = [ "Zesty" , "Ripe.ly" , "FruitBee" , "JuiceGrove" ]

    #function 1 simulation
    collegues(fruitcompanies,"FruitBee")

    #function 2 simulation
    Company=""
    while Company not in colist :
          Company=input("Choose a company (Zesty, Ripe.ly, FruitBee, JuiceGrove) >>> ") 
    collegues(fruitcompanies,Company)

    #function 3 simulation
    Company=""
    while True:
          Company=input("Choose a company (Zesty, Ripe.ly, FruitBee, JuiceGrove) >>> ") 
          if Company in colist : break
    collegues(fruitcompanies,Company,"Chad F.")

main()
