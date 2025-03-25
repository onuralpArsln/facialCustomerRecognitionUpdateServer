#!/usr/bin/python3
import os
import time
import multiprocessing
import protectless_version


def checkUpdate():
    while True:
        os.system("git fetch")
        results = os.popen("git status").read()
        if "branch is behind" in results:
            os.system("git pull")
            print("gerisdesin")
            time.sleep(5)
            os.system("reboot")
            os.system("sudo reboot")
        else:
            print("herikulade kod")

        time.sleep(10)


if __name__ == "__main__":
    # Start executeApp in a separate process
    process = multiprocessing.Process(target=checkUpdate)
    process.start()
    protectless_version.executeApp()


### Crontablamak için 
"""
@reboot export DISPLAY=:0 &&  cd /home/proje/adresi && . .venv/bin/activate && python3 checjer.py >> /home/usr_name/cronlog.txt 2>&1 

export DISPLAY=:0 ile ekrana gui açtır 
cd ile pathte çalış
. .venv/  source yerine . atmak daha güvenilir 
>> /home/usr_name/cronlog.txt 2>&1  log al

"""