#!/usr/bin/env python

from logging import shutdown
import os
from time import process_time_ns

ips = ['192.168.178.82','192.168.178.40','192.168.178.41','192.168.178.74'] #IP list (array)
off_devices = 0  # set offline devcies to 0
sumips = len(ips)  # count all ips in array


for i in ips:
        response_ping = os.system("ping -c 1 " + i) #ping all the ips in range
        print(response_ping) #print out the value of ping
        
        if response_ping > 0: #check if the value is higher than 0
                off_devices += 1 #add one more entry to off_devices

                countedoffdevices = off_devices #make a new variable for off_devices after counting all the offline devices
                print('Geräte offline:', countedoffdevices, '; IPs gezählt:', sumips) # print all info about offline and listed ips


if countedoffdevices == sumips: #if countedoffdevices is equals the sum off all ips in the array make a shutdown
    print('shutdown')
    os.system("shutdown -h now") #shutdown instand

else: #if countedoffdevices is not the same value as sum of all arrays do nothing
    print('stay online')