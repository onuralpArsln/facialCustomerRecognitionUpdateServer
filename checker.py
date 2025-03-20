#!/usr/bin/python3
import os 
import time 
import subprocess

isFirstLoop=True


while True:
    os.system("git fetch")
    results=os.popen("git status").read()
    if "branch is behind" in results:
        os.system("git pull")
        print("gerisdesin")
        time.sleep(5)
        os.system("reboot")        
    else:
        print("herikulade kod ")
        if isFirstLoop:
            isFirstLoop=False
            subprocess.Popen(" myenc/")
    time.sleep(100)
