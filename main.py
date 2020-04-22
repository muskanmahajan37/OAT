# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:49:07 2020

@author: @sunn-e
"""
# import os
import platform
from pathlib.Path import resolve

# for initially windows only
if (platform.release() != "Windows"):
    exit()
# dir path for future work
# dirpath = os.getcwd()

# for windows 10 x64
# host_file = "C:\Windows\System32\drivers\etc\hosts"
host_file = "hosts"
new_host_file = "new_host_file.txt"
websites_file = "websites.txt"
backup_host_file = "hosts.backup"

redirect = "0.0.0.0"    # I can modify this to
# redirect to some different site on case by casebasis
OAT_note = "\n#below content is added by OAT\n"

"""
create backup of original host file.
"""


def backup_host_file():
    # open host file and read it's content
    with open(host_file, "r", encoding="utf-8") as f:
        host_file_content = f.read()

    with open(backup_host_file, "w", encoding="utf-8") as f:
        f.write(host_file_content)


def restore_host_file():
    try:
        backup_host_file.resolve(strict=True)
    except FileNotFoundError:
        print("\nNo backup exists")
    else:
        print("\nBackup File Exists. Restoring!!")
        with open(backup_host_file, "r", encoding="utf-8") as f:
            backup_host_content = f.read()
        with open(host_file, "w", encoding="utf-8") as f:
            f.write(backup_host_content)
        print("\nRestored the host file from host backup successfully!")


def block_sites():
    # open rules file and read each website
    with open(websites_file, "r", encoding="utf-8") as f:
        websites = f.readlines()
    # create a new host file
    with open(host_file, "w", encoding="utf-8") as f:
        # first write the original hostfile
        f.write(OAT_note)  # note for users
        # now get every website mentioned in the rule file
        # given by user
        for website in websites:
            f.write(redirect + "    " + website.strip() + "\n")


def time_management():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
