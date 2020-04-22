# OAT
 Only Allow This

## Idea
An application that will take 

### input

A string of website
A Start Time 
End Time

### Output

Allow Only This websites to be launched in that time frame. Evething else just redirects to nothing.

#### issues

- abrupt shutdowns may leave hosts "unrestored" from backup host file.
   - solution could be to do this in memory. Like create a new temporary host file and let it work till session is running. Once the OS is shutdown, we need not have to worry about backups. Oh well. Good.

## Implementation - bruteforce

### High Level

- A small GUI that takes either 
   - a file containing the websites
   - or type manually urls
- A time defining widget
- Run buttong

### Low Level
- Read the url strings
- check if already a backup exists
   - if exists
      - match with current hostfile
	  - if no difference then ignore
	  - if difference, overwrite,because we might have abruptly closed last session.Need inplace version. 
- backup the original host file for initial run.
- modify the host files at the start time specified by the user, with the websites the user has given.
   - windows(High priority)
   - mac
   - linux
- Then restore the host file from the backup file when time is up.


## Implementation - in memory version

- get the current host file from OS.
- Create a new temporary file. Add new rules.
- Start the process when start time triggeres.
- Make OS lookup our new host file till session runs.
