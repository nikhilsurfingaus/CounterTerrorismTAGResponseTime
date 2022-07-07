from Resoruces.Vehicle import Vehicle
from Resoruces.Location import Location
import numpy as np
import math



def selectVehicle(location):
    
    #NSW Regions TAG E //////////////////////////////////////////////////////
    if (location.get_name() == "Sydney-North"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2180)
        Heli = Vehicle("Taipan", 200, 10, 20);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Sydney-East"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2180)
        Heli = Vehicle("Taipan", 200, 10, 16);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Sydney-South"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2180)
        Heli = Vehicle("Taipan", 200, 10, 7);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Sydney-West"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2180)
        Heli = Vehicle("Taipan", 200, 10, 24);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Newcastle"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1950)
        Heli = Vehicle("Taipan", 150, 10, 15);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)

    if (location.get_name() == "Mid North Coast"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1720)
        FourxFour = Vehicle("4x4", 80, 10, 25);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)

    if (location.get_name() == "Central Coast Coast"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2050)
        FourxFour = Vehicle("4x4", 80, 10, 20);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Hunter Valley"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1940)
        FourxFour = Vehicle("4x4", 80, 10, 15);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Illawarra"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2250)
        FourxFour = Vehicle("4x4", 80, 10, 25);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Canberra"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2450)
        Heli = Vehicle("Taipan", 150, 10, 15);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Wagga Wagga"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2480)
        Heli = Vehicle("Taipan", 150, 10, 10);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Northern Rivers"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1600)
        Heli = Vehicle("Taipan", 150, 10, 80);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "North West Region NSW"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1600)
        FourxFour = Vehicle("4x4", 80, 10, 30);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Central Region NSW"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1640)
        FourxFour = Vehicle("4x4", 80, 10, 35);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Outback Region NSW"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1900)
        FourxFour = Vehicle("4x4", 80, 10, 50);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    #QLD TAG E ////////////////////////////////////////////////////////////////
    if (location.get_name() == "Brisbane-North"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1300)
        Heli = Vehicle("Taipan", 200, 10, 15);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Brisbane-East"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 10, 1300)
        Heli = Vehicle("Taipan", 200, 10, 10);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Brisbane-South"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1300)
        Heli = Vehicle("Taipan", 200, 10, 15);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Brisbane-West"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1300)
        Heli = Vehicle("Taipan", 200, 10, 20);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Gold Coast"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1450)
        Heli = Vehicle("Taipan", 150, 10, 10);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Sunshine Coast"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1250)
        Heli = Vehicle("Taipan", 150, 10, 10);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Cairns"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 350)
        FourxFour = Vehicle("4x4", 80, 10, 15);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Townsville"):
        Heli = Vehicle("Taipan", 150, 10, 10);
        arr = np.array([Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Toowoomba"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1320)
        Heli = Vehicle("Taipan", 150, 10, 10);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Hervey Bay"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1100)
        FourxFour = Vehicle("4x4", 80, 10, 10);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Mackay"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 390)
        FourxFour = Vehicle("4x4", 80, 10, 15);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Rockhampton"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 720)
        FourxFour = Vehicle("4x4", 80, 10, 25);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Bundaberg"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1000)
        FourxFour = Vehicle("4x4", 80, 10, 10);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "South West Region QLD"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 600)
        FourxFour = Vehicle("4x4", 80, 10, 25);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Central West Region QLD"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 500)
        FourxFour = Vehicle("4x4", 80, 10, 25);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "North West Region QLD"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 450)
        FourxFour = Vehicle("4x4", 80, 10, 30);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Far North Region QLD"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 350)
        Heli = Vehicle("Taipan", 150, 10, 10);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    #VIC TAG E /////////////////////////////////////////////////////
    if (location.get_name() == "Melbourne-North"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 6);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Melbourne-East"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 10);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)

    if (location.get_name() == "Melbourne-South"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 13);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Melbourne-West"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 4);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)   
    
    if (location.get_name() == "Geelong"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 15);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)   
    
    if (location.get_name() == "Ballarat"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 28);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)   
    
    if (location.get_name() == "Bendigo"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2350)
        FourxFour = Vehicle("4x4", 80, 10, 8);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)   
    
    if (location.get_name() == "Mildura"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2200)
        FourxFour = Vehicle("4x4", 80, 10, 10);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Shepparton"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2300)
        FourxFour = Vehicle("4x4", 80, 10, 15);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Wondonga"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2300)
        FourxFour = Vehicle("4x4", 80, 10, 20);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Warrnambool"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2600)
        FourxFour = Vehicle("4x4", 80, 10, 15);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Lakes Region VIC"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2700)
        Heli = Vehicle("Taipan", 200, 10, 28);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "North West Region VIC"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2350)
        FourxFour = Vehicle("4x4", 80, 10, 50);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Great Ocean Region VIC"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2350)
        FourxFour = Vehicle("4x4", 80, 10, 30);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Gippsland Region VIC"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2700)
        Heli = Vehicle("Taipan", 200, 10, 8);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "High Country Region VIC"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2700)
        Heli = Vehicle("Taipan", 200, 10, 22);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    #TAS TAG E ////////////////////////////////////////////////////
    if (location.get_name() == "Hobart"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 3200)
        FourxFour = Vehicle("4x4", 80, 10, 20);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "Launceston"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 3000)
        FourxFour = Vehicle("4x4", 80, 10, 15);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "North West Region TAS"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 3000)
        FourxFour = Vehicle("4x4", 80, 10, 250);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "North Region TAS"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 3000)
        FourxFour = Vehicle("4x4", 80, 10, 100);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "East Region TAS"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 3000)
        FourxFour = Vehicle("4x4", 80, 10, 150);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "South Region TAS"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 3200)
        FourxFour = Vehicle("4x4", 80, 10, 250);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "West Region TAS"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 3200)
        FourxFour = Vehicle("4x4", 80, 10, 300);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    #SA TAG E/W ////////////////////////////////////////////////////////////
    if (location.get_name() == "Adelaide-North"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 7);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Adelaide-East"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 4);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Adelaide-South"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 7);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Adelaide-West"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 3);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Mount Gambier"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2700)
        Heli = Vehicle("Taipan", 200, 10, 10);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Whyalla"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 32);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    #TAG W [ONLY]
    if (location.get_name() == "Coober Pedy"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        FourxFour = Vehicle("4x4", 80, 10, 8);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)  
    
    if (location.get_name() == "North East Region SA"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 200);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr) 
    
    if (location.get_name() == "South East Region SA"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 100);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr) 
    
    if (location.get_name() == "South West Region SA"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 180);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr) 
    
    #TAG W [ONLY]
    if (location.get_name() == "North West Region SA"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        FourxFour = Vehicle("4x4", 80, 10, 250);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr) 
    
    #NT TAG E/W ///////////////////////////////////////////////////////////
    if (location.get_name() == "Darwin-North"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 3);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr) 
    
    if (location.get_name() == "Darwin-East"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 4);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr) 
    
    if (location.get_name() == "Darwin-South"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 6);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr) 
    
    if (location.get_name() == "Darwin-West"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 2);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr) 
    
    if (location.get_name() == "Katherine"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2200)
        Heli = Vehicle("Taipan", 200, 10, 8);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr) 
    
    if (location.get_name() == "Alice Springs"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2070)
        FourxFour = Vehicle("4x4", 80, 10, 25);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr) 
    
    #TAG W [ONLY]
    if (location.get_name() == "Yulara"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2050)
        FourxFour = Vehicle("4x4", 80, 10, 10);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr) 
    
    if (location.get_name() == "South East Region NT"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2070)
        FourxFour = Vehicle("4x4", 80, 10, 300);
        arr = np.array([Aircraft, FourxFour])
        return calcTime(arr)
    
    if (location.get_name() == "North East Region NT"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2200)
        Heli = Vehicle("Taipan", 200, 10, 150);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Central Region NT"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2200)
        Heli = Vehicle("Taipan", 200, 10, 120);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "South West Region NT"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2200)
        Heli = Vehicle("Taipan", 200, 10, 200);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    #WA - TAG W /////////////////////////////////////////////////////
    if (location.get_name() == "Perth-North"):
        Heli = Vehicle("Taipan", 200, 10, 10);
        arr = np.array([Heli])
        return calcTime(arr) 

    if (location.get_name() == "Perth-East"):
        Heli = Vehicle("Taipan", 200, 10, 12);
        arr = np.array([Heli])
        return calcTime(arr) 

    if (location.get_name() == "Perth-South"):
        Heli = Vehicle("Taipan", 200, 10, 8);
        arr = np.array([Heli])
        return calcTime(arr) 
    
    if (location.get_name() == "Perth-West"):
        Heli = Vehicle("Taipan", 200, 10, 4);
        arr = np.array([Heli])
        return calcTime(arr) 
    
    if (location.get_name() == "Learmonth"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1200)
        Heli = Vehicle("Taipan", 200, 10, 3);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Broome"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2050)
        Heli = Vehicle("Taipan", 200, 10, 180);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Exmouth"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1200)
        Heli = Vehicle("Taipan", 200, 10, 30);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Karratha"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1500)
        Heli = Vehicle("Taipan", 200, 10, 18);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Albany"):
        Heli = Vehicle("Taipan", 200, 10, 400);
        arr = np.array([Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Geraldton"):
        Heli = Vehicle("Taipan", 200, 10, 420);
        arr = np.array([Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Port Hedland"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1200)
        Heli = Vehicle("Taipan", 200, 10, 600);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Kununurra"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2200)
        Heli = Vehicle("Taipan", 200, 10, 300);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Kimberley Region WA"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2200)
        Heli = Vehicle("Taipan", 200, 10, 250);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Pilbara Region WA"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1200)
        Heli = Vehicle("Taipan", 200, 10, 400);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Mid West Region WA"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1200)
        Heli = Vehicle("Taipan", 200, 10, 300);
        arr = np.array([Aircraft, Heli])
        return calcTime(arr)
    
    if (location.get_name() == "Goldfields Esperance Region WA"):
        Heli = Vehicle("Taipan", 200, 10, 450);
        arr = np.array([Heli])
        return calcTime(arr) 
    
    if (location.get_name() == "South West Region WA"):
        Heli = Vehicle("Taipan", 200, 10, 100);
        arr = np.array([Heli])
        return calcTime(arr) 


def calcTime(arr):
    time = 0
    #Calculate Time
    for mode in arr:
         time += (((mode.get_travelDistance()/mode.get_speed())*60) + mode.get_marginTime())
         
    #Return Time
    return str(math.ceil(time))


def main():
    location = Location("South West Region WA", 1860, "Medium", None)
    time1 = selectVehicle(location);
    print("TAG-East ETA: " + time1 + " minutes to location: " + location.get_name())
    
    location2 = Location("Goldfields Esperance Region WA", 1670, "Medium", None)
    time2 = selectVehicle(location2);
    print("TAG-East ETA: " + time2 + " minutes to location: " + location2.get_name())

if __name__ == "__main__":
    main()