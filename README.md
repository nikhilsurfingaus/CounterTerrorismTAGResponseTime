# CounterTerrorismTAGResponseTime (Python GUI)

<img src="https://github.com/nikhilsurfingaus/CounterTerrorismTAGResponseTime/blob/master/Resources/SASR.png" width="200"> 


# Introduction
The CounterTerrorismTAGResponseTime is a Python based Tkinter GUI application which estimates the time taken for a specialist 
reponse team known as the Tactical Assualt Group (TAG). TAG is part of the Special Air Service Regiment (SASR), under the 
Australian Defence Force. More specifically the Special Operations Engineer Regiment and 171st Special Operations Aviation 
Squadron. The TAG unit tasked with responding as a counter-terrorism force to respond to terrorism incidents 
in Australia on land and maritime environments and also with conducting overseas special recovery operations.

The TAG unit is divided into TAG-East and TAG-West, seperating Australias two major coasts. TAG-East has two main barracks based in
Townsville Lavarack Barracks and Sydneys suburb of Holsworthy Barracks. Meanwhile TAG-West is located at the Campbell Barracks 
in the Perth suburb of Swanbourne.

# Usage
## Python Requirments & Libraries 

``` Python 3 ```
``` Numpy ```
``` Math ```
``` Time ```
``` Tkinter ```
``` PIL ``` 

## Demo
### Picture-By-Picture
Step 1                     |  Step 2                   | Step 3
:-------------------------:|:-------------------------:|:-------------------------
![](https://github.com/nikhilsurfingaus/CounterTerrorismTAGResponseTime/blob/master/Resources/DEMO1.jpg)  |  ![](https://github.com/nikhilsurfingaus/CounterTerrorismTAGResponseTime/blob/master/Resources/DEMO2.jpg) | ![](https://github.com/nikhilsurfingaus/CounterTerrorismTAGResponseTime/blob/master/Resources/DEMO3.jpg)

### Video
## [Link To Youtube Demo Video](https://youtu.be/0pkNlw2e1UM)
[![Everything Is AWESOME](https://yt-embed.herokuapp.com/embed?v=0pkNlw2e1UM)](https://youtu.be/0pkNlw2e1UM "Australia Tactical Assault Group (SASR TAG) Response Time Python Program
")

# Process
Time is determined using a number of factor:
- The distance from the closest TAG base either East (Sydney/Townsville) or West (Perth) to location
- The distance and speed covered by Vehicle(s)
  - 4x4
  - Taipan Helicopter
  - Fixed Wing RAAF Aircraft
- Margin of error time by mode of Vehicle(s)
- Accessability of final loction, ie terrain, buildings, weather etc
  - Simple
  - Standard
  - Complex
- Output information of within how many minutes TAG East/West will arrive

# Disclaimer
*This is not an official product nor is  it endorsed by the Special Air Service Regiment (SASR) and Australian Defence Force (ADF)*
