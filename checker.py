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
        else:
            print("herikulade kod")

        time.sleep(10)


if __name__ == "__main__":
    # Start executeApp in a separate process
    process = multiprocessing.Process(target=checkUpdate)
    process.start()
    protectless_version.executeApp()
