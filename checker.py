#!/usr/bin/python3
import os
import time
import multiprocessing
import protectless_version

def run_async_task():
    import asyncio
    asyncio.run(protectless_version.executeApp())  # Runs executeApp in a separate process

if __name__ == "__main__":
    # Start executeApp in a separate process
    process = multiprocessing.Process(target=run_async_task)
    process.start()

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
