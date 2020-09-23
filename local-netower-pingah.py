#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Local network host discovery probe, now...
# Probe those closest to you

import subprocess
import sys

try:
    if len(sys.argv[1]) == 0:
        hi = 255
    else:
        hi = int(sys.argv[1])
except IndexError:
    print("\nUsage: scanner will scan your local network! \n"
          "Enter a number between 1-255 to scan local hosts \n"
          "i.e. script.py 6 will scan 192.168.1.1, 192.168.1.2 ... 192.168.1.6 \n \n ")

for x in range(1, hi):
    host = '192.168.1.' + str(x)
    res = subprocess.call(['ping', '-c', '3', host])
    finalHosts = []
    if res == 0:
        print("Success!", host, "is alive")
        finalHosts = finalHosts.append([host])
    elif res == 2:
        print(host + " said ....nothing.")
    else:
        print("Fatal error in your attempts.  Fix something or move on.")


