# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:49:07 2020

@author: @sunn-e
"""
# import os
import platform
import time
from datetime import datetime as dt
from pathlib import Path
from os import path

# for initially windows only
if (platform.release() != "Windows"):
    exit()
# dir path for future work
# dirpath = os.getcwd()

# for windows 10 x64
# host_file = "C:\Windows\System32\drivers\etc\hosts"
host_file = "hosts"
websites_file = "blocklist.txt"
backup_host_file = "hosts.backup"

redirect = "0.0.0.0"    # I can modify this to
# redirect to some different site on case by casebasis
OAT_note = "\n#below content is added by OAT\n"

"""
create backup of original host file.
"""


def backup_host():
    # open host file and read it's content
    with open(host_file, "r", encoding="utf-8") as f:
        host_file_content = f.read()

    with open(backup_host_file, "w", encoding="utf-8") as f:
        f.write(str(host_file_content))


def restore_host():
    if(path.exists(backup_host_file)):
        print("\nTrying to restore!!")
        with open(backup_host_file, "r", encoding="utf-8") as f:
            backup_host_content = f.read()
        with open(host_file, "w", encoding="utf-8") as f:
            f.write(backup_host_content)
        print("\nRestored the host file from host backup successfully!")
    else:
        print("Backup Not Found!")


def add_block_sites():
    # open rules file and read each website
    with open(websites_file, "r", encoding="utf-8") as f:
        websites = f.readlines()
    # create a new host file
    with open(host_file, "w+", encoding="utf-8") as f:
        # first write the original hostfile
        host_content = f.read()
        for website in websites:
            if website in host_content:
                pass
            else:
                f.write(redirect + "    " + website.strip() + "\n")



def time_manager(start_time, end_time):
    while (dt(dt.now().year, dt.now().month, dt.now().day,start_time) < dt.now() < dt(dt.now().year, dt.now().month,dt.now().day, end_time)):
        add_block_sites()
        time.sleep(10)

def main():
    print("I'm OAT!")
    start_time = int(input("Enter the start time in 24 Hours format.\nExample\t2 for 2 AM 18 for 6PM."))

    end_time = int(input("Similarly, enter end time!"))
    if(((0<= start_time <=24) and (0<= end_time <= 24 )) == True):
        backup_host()
        time_manager(start_time, end_time)
        restore_host()
    exit()


if __name__ == "__main__":
    main()
