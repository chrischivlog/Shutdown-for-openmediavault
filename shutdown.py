#!/usr/bin/env python

import os

ip1 = '192.168.178.40'

response = os.system("ping -c 1 " + ip1)

if response == 0:
    print("erreichbar")
else:
    print("nicht erreichbar")
    os.system("shutdown -h now")
