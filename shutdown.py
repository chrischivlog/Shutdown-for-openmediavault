#!/usr/bin/env python

import os

ips = ['192.168.178.41','192.168.178.40']

for i in ips: 
   response = os.system("ping -c 1 " + i)

if response == 0:
    print("erreichbar")
else:
    print("nicht erreichbar")
    os.system("shutdown -h now")
