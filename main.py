import time
from datetime import datetime as dt

host_temp = "hosts"
#Linux host path
host_path = "/etc/hosts"
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
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):

        print("No distractions...try again later")
        with open(host_path, 'r+') as file:
            content = file.read()
            print(content)

        for website in content:
            #If the website is already there dont do anything
            if website in content:
                pass
            else:
                #Map the hostname to local host IP
                file.write(redirect + " " + website  + " \n")                
    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            for line in content:
                if not any(website in line for website in website_list)
                file.write(line)
        print("Fun Time")
