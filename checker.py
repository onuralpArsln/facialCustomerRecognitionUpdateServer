#!/usr/bin/python3
import os
import time
import asyncio
import protectless_version

async def main():
    # Start the async function in the background
    asyncio.create_task(protectless_version.executeApp())

    while True:
        os.system("git fetch")
        results = os.popen("git status").read()
        if "branch is behind" in results:
            os.system("git pull")
            print("gerisdesin")
            await asyncio.sleep(5)  # Use async sleep
            os.system("reboot")
        else:
            print("herikulade kod")

        await asyncio.sleep(10)  # Use async sleep

asyncio.run(main())  # Run the event loop
