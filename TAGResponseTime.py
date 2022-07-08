from turtle import width
from Resoruces.Vehicle import Vehicle
from Resoruces.Location import Location
import numpy as np
import math
from tkinter import*
import time
from tkinter import messagebox


#Creat Tkinter UI Interface
test = False
root = Tk()
state = StringVar(root)
test2 = False
var = IntVar()


def selectVehicle(location, access):
    time = 0;
    #NSW Regions TAG E //////////////////////////////////////////////////////
    if (location == "Sydney-North"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2180)
        Heli = Vehicle("Taipan", 200, 10, 20);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Sydney-North", 2200, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "Sydney-East"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2180)
        Heli = Vehicle("Taipan", 200, 10, 16);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Sydney-East", 2196, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]    
    
    if (location == "Sydney-South"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2180)
        Heli = Vehicle("Taipan", 200, 10, 7);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Sydney-South", 2187, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "Sydney-West"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2180)
        Heli = Vehicle("Taipan", 200, 10, 24);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Sydney-West", 2204, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "Newcastle"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1950)
        Heli = Vehicle("Taipan", 150, 10, 15);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Newcastle", 1965, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]

    if (location == "Mid North Coast"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1720)
        FourxFour = Vehicle("4x4", 80, 10, 25);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Mid North Coast", 1745, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]

    if (location == "Central Coast"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2050)
        FourxFour = Vehicle("4x4", 80, 10, 20);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Central Coast", 2070, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "Hunter Valley"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1940)
        FourxFour = Vehicle("4x4", 80, 10, 15);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Hunter Valley", 1955, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "Illawarra"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2250)
        FourxFour = Vehicle("4x4", 80, 10, 25);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Illawarra", 2275, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "Canberra"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2450)
        Heli = Vehicle("Taipan", 150, 10, 15);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Canberra", 2465, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "Wagga Wagga"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2480)
        Heli = Vehicle("Taipan", 150, 10, 10);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Wagga Wagga", 2490, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "Northern Rivers"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1600)
        Heli = Vehicle("Taipan", 150, 10, 80);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Northern Rivers", 1680, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "North West Region NSW"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1600)
        FourxFour = Vehicle("4x4", 80, 10, 30);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("North West Region NSW", 1630, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "Central Region NSW"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1640)
        FourxFour = Vehicle("4x4", 80, 10, 35);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Central Region NSW", 1675, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "Outback Region NSW"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1900)
        FourxFour = Vehicle("4x4", 80, 10, 50);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Outback Region NSW", 1950, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    #QLD TAG E ////////////////////////////////////////////////////////////////
    if (location == "Brisbane-North"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1300)
        Heli = Vehicle("Taipan", 200, 10, 15);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Brisbane-North", 1315, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Brisbane-East"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 10, 1300)
        Heli = Vehicle("Taipan", 200, 10, 10);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Brisbane-East", 1310, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Brisbane-South"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1300)
        Heli = Vehicle("Taipan", 200, 10, 15);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Brisbane-South", 1315, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Brisbane-West"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1300)
        Heli = Vehicle("Taipan", 200, 10, 20);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Brisbane-West", 1320, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Gold Coast"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1450)
        Heli = Vehicle("Taipan", 150, 10, 10);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Gold Coast", 1460, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location== "Sunshine Coast"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1250)
        Heli = Vehicle("Taipan", 150, 10, 10);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Sunshine Coast", 1260, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Cairns"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 350)
        FourxFour = Vehicle("4x4", 80, 10, 15);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Cairns", 365, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Townsville"):
        Heli = Vehicle("Taipan", 150, 10, 10);
        arr = np.array([Heli])
        locObject = Location("Townsville", 10, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Toowoomba"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1320)
        Heli = Vehicle("Taipan", 150, 10, 10);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Toowoomba", 1330, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Hervey Bay"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1100)
        FourxFour = Vehicle("4x4", 80, 10, 10);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Hervey Bay", 1120, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Mackay"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 390)
        FourxFour = Vehicle("4x4", 80, 10, 15);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Mackay", 405, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Rockhampton"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 720)
        FourxFour = Vehicle("4x4", 80, 10, 25);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Rockhampton", 745, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Bundaberg"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1000)
        FourxFour = Vehicle("4x4", 80, 10, 10);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Bundaberg", 1010, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "South West Region QLD"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 600)
        FourxFour = Vehicle("4x4", 80, 10, 25);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("South West Region QLD", 625, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Central West Region QLD"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 500)
        FourxFour = Vehicle("4x4", 80, 10, 25);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Central West Region QLD", 525, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "North West Region QLD"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 450)
        FourxFour = Vehicle("4x4", 80, 10, 30);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("North West Region QLD", 480, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Far North Region QLD"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 350)
        Heli = Vehicle("Taipan", 150, 10, 10);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Far North Region QLD", 360, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    #VIC TAG E /////////////////////////////////////////////////////
    if (location == "Melbourne-North"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 6);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Melbourne-North", 2506, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Melbourne-East"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 10);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Melbourne-East", 2510, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "Melbourne-South"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 13);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Melbourne-South", 2513, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Melbourne-West"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 4);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Melbourne-West", 2504, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Geelong"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 15);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Geelong", 2515, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Ballarat"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 28);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Ballarat", 2528, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Bendigo"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2350)
        FourxFour = Vehicle("4x4", 80, 10, 8);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Bendigo", 2358, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Mildura"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2200)
        FourxFour = Vehicle("4x4", 80, 10, 10);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Mildura", 2210, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Shepparton"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2300)
        FourxFour = Vehicle("4x4", 80, 10, 15);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Shepparton", 2315, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Wondonga"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2300)
        FourxFour = Vehicle("4x4", 80, 10, 20);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Wondonga", 2320, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Warrnambool"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2600)
        FourxFour = Vehicle("4x4", 80, 10, 15);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Warrnambool", 2615, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Lakes Region VIC"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2700)
        Heli = Vehicle("Taipan", 200, 10, 28);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Lakes Region VIC", 2728, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "North West Region VIC"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2350)
        FourxFour = Vehicle("4x4", 80, 10, 50);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("North West Region VIC", 2400, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Great Ocean Region VIC"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2350)
        FourxFour = Vehicle("4x4", 80, 10, 30);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Great Ocean Region VIC", 2380, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Gippsland Region VIC"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2700)
        Heli = Vehicle("Taipan", 200, 10, 8);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Gippsland Region VIC", 2708, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "High Country Region VIC"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2700)
        Heli = Vehicle("Taipan", 200, 10, 22);
        arr = np.array([Aircraft, Heli])
        locObject = Location("High Country Region VIC", 2722, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    #TAS TAG E ////////////////////////////////////////////////////
    if (location == "Hobart"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 3200)
        FourxFour = Vehicle("4x4", 80, 10, 20);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Hobart", 3220, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "Launceston"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 3000)
        FourxFour = Vehicle("4x4", 80, 10, 15);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Launceston", 3015, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "North West Region TAS"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 3000)
        FourxFour = Vehicle("4x4", 80, 10, 250);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("North West Region TAS", 3250, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "North Region TAS"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 3000)
        FourxFour = Vehicle("4x4", 80, 10, 100);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("North Region TAS", 3100, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "East Region TAS"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 3000)
        FourxFour = Vehicle("4x4", 80, 10, 150);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("East Region TAS", 3150, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "South Region TAS"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 3200)
        FourxFour = Vehicle("4x4", 80, 10, 250);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("South Region TAS", 3450, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    if (location == "West Region TAS"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 3200)
        FourxFour = Vehicle("4x4", 80, 10, 300);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("West Region TAS", 3500, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
    
    #SA TAG E/W ////////////////////////////////////////////////////////////
    if (location == "Adelaide-North"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 7);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Adelaide-North", 2407, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    if (location == "Adelaide-East"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 4);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Adelaide-East", 2404, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
            
    if (location == "Adelaide-South"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 7);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Adelaide-South", 2407, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
            
    if (location == "Adelaide-West"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 3);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Adelaide-West", 2403, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
            
    if (location == "Mount Gambier"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2700)
        Heli = Vehicle("Taipan", 200, 10, 10);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Mount Gambier", 2710, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
            
    if (location == "Whyalla"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 32);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Whyalla", 2432, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
            
    #TAG W [ONLY]
    if (location == "Coober Pedy"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        FourxFour = Vehicle("4x4", 80, 10, 8);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Coober Pedy", 2508, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
            
    if (location == "North East Region SA"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 200);
        arr = np.array([Aircraft, Heli])
        locObject = Location("North East Region SA", 2600, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
            
    if (location == "South East Region SA"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 100);
        arr = np.array([Aircraft, Heli])
        locObject = Location("South East Region SA", 2500, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
            
    if (location == "South West Region SA"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2400)
        Heli = Vehicle("Taipan", 200, 10, 180);
        arr = np.array([Aircraft, Heli])
        locObject = Location("South West Region SA", 2580, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
            
    #TAG W [ONLY]
    if (location == "North West Region SA"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        FourxFour = Vehicle("4x4", 80, 10, 250);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("North West Region SA", 2750, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
        
    #NT TAG E/W ///////////////////////////////////////////////////////////
    if (location == "Darwin-North"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 3);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Darwin-North", 2503, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Darwin-East"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 4);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Darwin-East", 2504, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Darwin-South"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 6);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Darwin-South", 2506, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location== "Darwin-West"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2500)
        Heli = Vehicle("Taipan", 200, 10, 2);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Darwin-West", 2502, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Katherine"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2200)
        Heli = Vehicle("Taipan", 200, 10, 8);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Katherine", 2208, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Alice Springs"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2070)
        FourxFour = Vehicle("4x4", 80, 10, 25);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Alice Springs", 2095, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    #TAG W [ONLY]
    if (location == "Yulara"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2050)
        FourxFour = Vehicle("4x4", 80, 10, 10);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("Yulara", 2060, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "South East Region NT"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2070)
        FourxFour = Vehicle("4x4", 80, 10, 300);
        arr = np.array([Aircraft, FourxFour])
        locObject = Location("South East Region NT", 2370, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "North East Region NT"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2200)
        Heli = Vehicle("Taipan", 200, 10, 150);
        arr = np.array([Aircraft, Heli])
        locObject = Location("North East Region NT", 2350, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Central Region NT"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2200)
        Heli = Vehicle("Taipan", 200, 10, 120);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Central Region NT", 2320, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "South West Region NT"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2200)
        Heli = Vehicle("Taipan", 200, 10, 200);
        arr = np.array([Aircraft, Heli])
        locObject = Location("South West Region NT", 2400, access, "East")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    #WA - TAG W /////////////////////////////////////////////////////
    if (location == "Perth-North"):
        Heli = Vehicle("Taipan", 200, 10, 10);
        arr = np.array([Heli])
        locObject = Location("Perth-North", 10, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
         
    if (location == "Perth-East"):
        Heli = Vehicle("Taipan", 200, 10, 12);
        arr = np.array([Heli])
        locObject = Location("Perth-East", 12, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
         
    if (location == "Perth-South"):
        Heli = Vehicle("Taipan", 200, 10, 8);
        arr = np.array([Heli])
        locObject = Location("Perth-South", 8, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Perth-West"):
        Heli = Vehicle("Taipan", 200, 10, 4);
        arr = np.array([Heli])
        locObject = Location("Perth-West", 4, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Learmonth"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1200)
        Heli = Vehicle("Taipan", 200, 10, 3);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Learmonth", 1203, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Broome"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2050)
        Heli = Vehicle("Taipan", 200, 10, 180);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Broome", 2230, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Exmouth"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1200)
        Heli = Vehicle("Taipan", 200, 10, 30);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Exmouth", 1230, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Karratha"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1500)
        Heli = Vehicle("Taipan", 200, 10, 18);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Karratha", 1518, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Albany"):
        Heli = Vehicle("Taipan", 200, 10, 400);
        arr = np.array([Heli])
        locObject = Location("Albany", 400, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Geraldton"):
        Heli = Vehicle("Taipan", 200, 10, 420);
        arr = np.array([Heli])
        locObject = Location("Geraldton", 420, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Port Hedland"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1200)
        Heli = Vehicle("Taipan", 200, 10, 600);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Port Hedland", 1800, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Kununurra"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2200)
        Heli = Vehicle("Taipan", 200, 10, 300);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Kununurra", 2500, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Kimberley Region WA"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 2200)
        Heli = Vehicle("Taipan", 200, 10, 250);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Kimberley Region WA", 2450, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Pilbara Region WA"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1200)
        Heli = Vehicle("Taipan", 200, 10, 400);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Pilbara Region WA", 1600, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Mid West Region WA"):
        Aircraft = Vehicle("RAAF Fixed Wing", 600, 20, 1200)
        Heli = Vehicle("Taipan", 200, 10, 300);
        arr = np.array([Aircraft, Heli])
        locObject = Location("Mid West Region WA", 1500, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "Goldfields Esperance Region WA"):
        Heli = Vehicle("Taipan", 200, 10, 450);
        arr = np.array([Heli])
        locObject = Location("Goldfields Esperance Region WA", 450, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
             
    if (location == "South West Region WA"):
        Heli = Vehicle("Taipan", 200, 10, 100);
        arr = np.array([Heli])
        locObject = Location("South West Region WA", 100, access, "West")
        time= calcTime(arr)
        return [locObject, time, arr]
         

def calcTime(arr):
    time = 0
    #Calculate Time
    for mode in arr:
         time += (((mode.get_travelDistance()/mode.get_speed())*60) + mode.get_marginTime())
         
    #Return Time
    return str(math.ceil(time))


def confirmQuit(root3):
    response=messagebox.askyesno('TAG Response Estimator','Are you sure you want to exit?')
    if response:
        time.sleep(1)
        root3.destroy()    
    

def printETA(loc, access):
    res = selectVehicle(loc, access)
    vehicles = res[2]
    names = np.array([])    
    
    for n in vehicles:
        names = np.append(names, n.get_name())
        
    nameStr = ', '.join([str(n) for n in names])
        
    vInvol = "Vehicles Involved include: " + nameStr
    loc = "Location: " + res[0].get_name()
    arr = "TAG team will arrive within: " + str(res[1]) + " mins"
    team = "Team Responding will be ADF Special Forces TAG-" + res[0].get_tag()
    dis = "TAG Base Distance To Your Area Approx: " + str(res[0].get_baseDistance()) + " kms"
    
    root3 = Tk()
    root3.geometry('500x400')
    root3.title("TAG Response Estimator")
    
    label_0 = Label(root3, text="Result",width=28,font="Helvetica 25 bold")
    label_0.place(x=-25,y=23)
    
    label_1 = Label(root3, text=vInvol,width=60, anchor="w",font="Helvetica 10 bold")
    label_1.place(x=20,y=100)

    label_2 = Label(root3, text=loc,width=60, anchor="w",font="Helvetica 10 bold")
    label_2.place(x=20,y=140)

    label_4 = Label(root3, text=dis,width=60, anchor="w", justify=LEFT,font="Helvetica 10 bold")
    label_4.place(x=20,y=180)
    
    label_4 = Label(root3, text=team,width=60, anchor="w",font="Helvetica 10 bold")
    label_4.place(x=20,y=220)
    
    label_4 = Label(root3, text=arr,width=60, anchor="w",font="Helvetica 16 bold")
    label_4.place(x=20,y=280)
    
    Button(root3, text='Quit',width=20,bg='brown',fg='white', command=lambda : confirmQuit(root3)).place(x=160,y=340)

    root3.mainloop()
    
    
    

def displayLocAc(location, access):
    printETA(location, access)
    
def inter2(location, access, root2):
    time.sleep(1)
    root2.destroy()
    displayLocAc(location, access)

def createLocation():
    specificState = state.get()
    locList = []
    NSW = ["Sydney-North", "Sydney-East", "Sydney-South", "Sydney-West", "Newcastle", "Mid North Coast", "Central Coast", "Hunter Valley", "Illawarra", "Canberra", "Wagga Wagga", "Northern Rivers", "North West Region NSW", "Central Region NSW", "Outback Region NSW"]
    QLD = ["Brisbane-North", "Brisbane-East", "Brisbane-South", "Brisbane-West", "Gold Coast", "Sunshine Coast", "Cairns", "Townsville",  "Toowoomba", "Hervey Bay", "Mackay", "Rockhampton", "Bundaberg", "South West Region QLD", "Central West Region QLD", "North West Region QLD", "Far North Region QLD"]
    VIC = ["Melbourne-North", "Melbourne-East", "Melbourne-South", "Melbourne-West", "Geelong", "Ballarat", "Bendigo", "Mildura", "Shepparton", "Wondonga", "Warrnambool", "Lakes Region VIC", "North West Region VIC", "Great Ocean Region VIC", "Gippsland Region VIC", "High Country Region VIC" ]
    TAS = ["Hobart", "Launceston", "North West Region TAS", "North Region TAS", "East Region TAS", "South Region TAS", "West Region TAS" ]
    SA = ["Adelaide-North", "Adelaide-East", "Adelaide-South", "Adelaide-West", "Mount Gambier", "Whyalla", "Coober Pedy", "North East Region SA", "South East Region SA", "South West Region SA", "North West Region SA" ]
    NT = ["Darwin-North", "Darwin-East", "Darwin-South", "Darwin-West", "Katherine", "Alice Springs" , "Yulara", "South East Region NT", "North East Region NT", "Central Region NT", "South West Region NT" ]
    WA = ["Perth-North", "Perth-East", "Perth-South", "Perth-West", "Learmonth", "Broome", "Exmouth", "Karratha", "Albany", "Geraldton", "Port Hedland", "Kununurra", "Kimberley Region WA", "Pilbara Region WA", "Mid West Region WA", "Goldfields Esperance Region WA", "South West Region WA"  ]
    accessList = ["Simple", "Standard", "Complex"]
    
    #Select State Region Specific Options
    if (specificState == "NSW"):
        locList = NSW
    if (specificState == "QLD"):
        locList = QLD
    if (specificState == "VIC"):
        locList = VIC
    if (specificState == "TAS"):
        locList = TAS
    if (specificState == "SA"):
        locList = SA
    if (specificState == "NT"):
        locList = NT
    if (specificState == "WA"):
        locList = WA
    
    
    
    
    root2 = Tk()
    root2.geometry('500x400')
    root2.title("TAG Response Estimator")
    


    label_0 = Label(root2, text="Select Location",width=28,font=("bold", 20))
    label_0.place(x=20,y=53)
    
    area = StringVar(root2)
    access = StringVar(root2)
    
    area.set(locList[0]) # default value
    access.set(accessList[0])
    
    selectedLocation = OptionMenu(root2, area, *locList)
    selectedLocation.config(width=20)
    selectedLocation.pack()
    selectedLocation.place(x=160,y=123)
    

    label_1 = Label(root2, text="Select Accessibility",width=28,font=("bold", 20))
    label_1.place(x=20,y=200)
    
    selectedAccess = OptionMenu(root2, access, *accessList)
    selectedAccess.config(width=20)
    selectedAccess.pack()
    selectedAccess.place(x=160,y=270)
    
    Button(root2, text='Next',width=20,bg='brown',fg='white', command=lambda : inter2(area.get(), access.get(), root2)).place(x=160,y=320)

    root2.mainloop()
    
def inter():
    #Create UI delay for better UX
    time.sleep(1)
    root.destroy()
    createLocation()
    
def mainScreen():
    STATES = ["NSW", "QLD", "VIC", "TAS", "SA", "NT", "WA"]
    root.geometry('500x400')
    root.title("TAG Response Estimator")
    label_0 = Label(root, text="Select State/Territory",width=28,font=("bold", 20))
    label_0.place(x=20,y=53)

    state.set(STATES[0]) # default value

    w = OptionMenu(root, state, *STATES)
    w.pack()
    w.place(x=200,y=143)
    
    Button(root, text='Next',width=20,bg='brown',fg='white', command=inter).place(x=160,y=280)

    

    root.mainloop()    

def main():
    # location = Location("South West Region WA", 1860, "Medium", None)
    # time1 = selectVehicle(location);
    # print("TAG-East ETA: " + time1 + " minutes to location: " + location.get_name())
    
    # location2 = Location("Goldfields Esperance Region WA", 1670, "Medium", None)
    # time2 = selectVehicle(location2);
    # print("TAG-East ETA: " + time2 + " minutes to location: " + location2.get_name())

    mainScreen()
    
if __name__ == "__main__":
    main()