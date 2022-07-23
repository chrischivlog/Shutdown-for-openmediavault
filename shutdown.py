#!/usr/bin/env python

from logging import shutdown
import os
from time import process_time_ns

ips = ['192.168.178.82','192.168.178.40','192.168.178.41','192.168.178.74']
off_devices = 0  # set offline devcies to 0
sumips = len(ips)  # count all ips in array


for i in ips:
        response_ping = os.system("ping -c 1 " + i)
        print(response_ping)
        
        if response_ping > 0:
                off_devices += 1

                countedoffdevices = off_devices
                print('Geräte offline:', countedoffdevices, '; IPs gezählt:', sumips)


if countedoffdevices == sumips:
    print('shutdown')
    os.system("shutdown -h now")

else:
    print('stay online')