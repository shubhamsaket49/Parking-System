#!/usr/bin/env python
# coding: utf-8

# In[1]:


c ="Car"
b ="Bus"
t ="Truck"
s ="Scooter"
p ="Cycle"
m ="MotorCycle"
print("c for Car")
print("b for Bus")
print("t for Truck")
print("S for Scooter")
print("p for Cycle")
print("m for Motor Cycle")
vehicle=input("Enter the name of vehicle")
arrival_hr=float(input("Enter entering hours time"))
arrival_min=float(input("Enter entering minutes time"))
leaving_hr=float(input("Enter leaving hours time"))
leaving_min=float(input("Enter leaving minutes time"))
entry=arrival_hr+(arrival_min/60)
exit=leaving_hr+(leaving_min/60)
parking_time= exit - entry
if(vehicle=='c'):
    if(parking_time<=3):
        print("Total Parking time of car: ", parking_time)
        print("Parking charge of car is :Rs10")
    else:
        print("Total Parking time of car: ", parking_time)
        print("Parking charge of car is :Rs20")
elif(vehicle=='b'):
    if(parking_time<=3):
        print("Total Parking time of bus: ", parking_time)
        print("Parking charge of bus is :Rs20")
    else:
        print("Total Parking time of bus: ", parking_time)
        print("Parking charge of bus is :Rs30")
elif(vehicle=='t'):
    if(parking_time<=3):
        print("Total Parking time of truck: ", parking_time)
        print("Parking charge of truck is :Rs20")
    else:
        print("Total Parking time of truck: ", parking_time)
        print("Parking charge of truck is :Rs30")
elif(vehicle=='s'):
    if(parking_time<=3):
        print("Total Parking time of scooter: ", parking_time)
        print("Parking charge of scooter is :Rs5")
    else:
        print("Total Parking time of scooter : ", parking_time)
        print("Parking charge of scooter is :Rs10")
elif(vehicle=='c'):
    if(parking_time<=3):
        print("Total Parking time of cycle: ", parking_time)
        print("Parking charge of cycle is :Rs5")
    else:
        print("Total Parking time of cycle : ", parking_time)
        print("Parking charge of cycle is :Rs10")
elif(vehicle=='m'):
    if(parking_time<=3):
        print("Total Parking time of Motorcycle: ", parking_time)
        print("Parking charge of Motorcycle is :Rs5")
    else:
        print("Total Parking time of Motorcycle : ", parking_time)
        print("Parking charge of Motorcycle is :Rs10")
print()       


# In[ ]:





# In[ ]:





# In[ ]:




