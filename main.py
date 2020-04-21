# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:49:07 2020

@author: @sunn-e
"""
#import os
import platform

# for initially windows only
if (platform.release() != "Windows"):
    exit()
# dir path for future work
#dirpath = os.getcwd()

# for windows 10 x64
#host_file = "C:\Windows\System32\drivers\etc\hosts"
host_file = "hosts"
new_host_file = "new_host_file.txt"
block_list_file = "blocklist.txt"

redirect = "0.0.0.0" # I can modify this to 
                     #redirect to some different site on case by 

OAT_note = "\n#below content is added by OAT\n"




# open host file and read it's content
with open(host_file, "r", encoding = "utf-8") as f:
    host_file_content = f.read()


# open rules file and read each website
with open(block_list_file, "r", encoding = "utf-8") as f:
    _temp_block_lines = f.readlines()

# create a new host file
with open(new_host_file, "w", encoding = "utf-8") as f:
    # first write the original hostfile
    f.write(str(host_file_content) + OAT_note) #note for users
    # now get every website mentioned in the rule file
    #given by user
    for line in _temp_block_lines:
        f.write(redirect + "     " + line.strip()+ "\n")


 