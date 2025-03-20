#!/usr/bin/python3


import os 
import time 


while True:
    os.system("git fetch")
    results=os.popen("git status").read()
    if "branch is behind" in results:
        os.system("git pull")

        print("gerisdesin")
    else:
        print("herikulade kod ")
    time.sleep(10)
