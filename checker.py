#!/usr/bin/python3
import os 
import time 
import subprocess
import protectless_version

import asyncio
asyncio.run(protectless_version.executeApp()) 



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


    time.sleep(10)
