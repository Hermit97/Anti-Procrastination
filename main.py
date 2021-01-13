import time
from datetime import datetime as dt

#Linux host path
host_path "/etc/hosts"
#Local host IP address 
redirect = "127.0.0.1"

#Websites blocked
websites_blocked = [
    "www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com",
    "www.yahoo.com", "yahoo.com"
]

active = True

while active:

    #Time period the block is active
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now 
    < dt(dt.now().year, dt.now().month, dt.now().day, 16):

        print("No distractions...try again later")
        with open(host_path, 'r+') as file:
            content = file.read()

        for website in content:
            if website in content:
                pass
            else:
                #map the hostname to local host IP
                file.write(redirect + " " + website  + " \n")
    


            


