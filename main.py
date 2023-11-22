import time
from datetime import datetime as dt

#Linux host path
host_path = r"C:/Windows/System32/drivers/etc/hosts"
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
    print(dt(dt.now().year, dt.now().month, dt.now().day, 0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23))
    if dt(dt.now().year, dt.now().month, dt.now().day, 0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):

        print("No distractions...try again later")
        with open(host_path, 'r+') as file:
            #Contents of the file
            content = file.read()
            print(content)
            for website in websites_blocked:
                #If the website is already there dont do anything
                if website in content:
                    pass
                else:
                    #Map the hostname to local host IP
                    file.write(redirect + " " + website  + " \n")                
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                if not any(website in line for website in websites_blocked):
                    file.write(line)
                print("Access Granted...")

            file.truncate()
        print("Access Granted...")
    time.sleep(5)
