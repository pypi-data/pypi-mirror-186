.. Title

LINUX
=====

TERMINAL
--------
1. `history` - History of commands

FILES & NAVIGATION
------------------

1. `ls` - Directory listing (list all files and folders in current directory)
2. `ls -l` - Formatted directory listing
3. `ls -la` - Formatted listing including hidden files
4. `cd <dir>` - Change directory to <dir> (dir will be directory name)
5. `cd ..`
   - Change to parent directory
6. `cd ../dir`
   - Change to dir in the parent directory
7. `cd`
   - Change to home directory
8. `pwd`
   - Show current directory
9. `mkdir <dir>`
   - Create a directory <dir>
10. `rm <file-name>`
    - Delete file, <file-name>
11. `rm -f <dir>`
    - Force remove file
12. `rm -r <dir>`
    - Delete directory, <dir>
13. `rm -rf dir`
    - Remove directory, <dir>
14. `rm -rf /`
    - Launch some neuclear bombs targetting your system!!!
15. `cp file1 file2`
    - Copy file1 to file2
16. `mv file1 file2`
    - Rename file1 to file2
17. `mv file1 dir/file2`
    - Move file1 to dir as file2
18. `touch file`
    - Create or update file
19. `cat file`
    - Output contents of file
20. `cat > file`
    - Write standard input into file
21. `cat >> file`
    - Append standard input into file
22. `tail -f file`
    - Output contents of file as it grows

NETWORKING
----------

1. `ping host`
   - Ping host
2. `whois domain`
   - Got whois for domain
3. `dig domain`
   - Get DNS for domain
4. `dig -x host`
   - Resolve lookup host
5. `wget file`
   - Download file
6. `wget -c file`
   - Continue stopped download
7. `wget -r url`
   - Recursively download files from url
8. `curl url`
   - Outputs the webpage from url
9. `curl -o meh.html url`
   - Writes the page to meh.html
10. `ssh user@host`
    - Connnect to host as user
11. `ssh -p port user@host`
    - Connect using port
12. `ssh -D user@host`
    - Connect and user bind port

PROCESSES
---------

1. `ps`
   - Display currently active processes
2. `ps aux`
   - Detailed outputs
3. `kill pid`
   - Kill process with process id(pid)
4. `killall proc`
   - Kill all processes named proc

SYSTEM INFO
-----------

1. `date`
   - Show current date/time
2. `uptime`
   - Show uptime
3. `whoami`
   - Who you're loggen in as 
4. `w`
   - Display who is online
5. `cat /proc/cpuinfo`
   - Display cpu info
6. `cat /proc/meminfo`
   - Memory info
7. `free`
   - Show memory and swap usage
8. `du`
   - Show directory space usage
9. `du -sh`
   - Display readable sizes in GB
10. `df`
    - Show disk usage
11. `uname -d`
    - Show kernal config

COMRESSING
----------
1. `tar cf file.tar files`
   - Tar files into file.tar
2. `tar xf file.tr`
   - Untar file.tr into current directory
3. `tar tf file.tar`
   - Show contents of archive

**Options**
- c - create archive
- t - table of contents
- x - extract 
- z - user zip/gzip
- f - specify filename
- j - bzip2 compression
- w - ask for confirmation
- k - do not overwrite
- T - files from file
- v - verbose

PERMISSIONS
-----------

1. `chmod actual-file`
   - Change permission of file
    
    - 4 - read(r)
    - 2 - write(w)
    - 1 - execute(x)
    
    - Order: owner/group/world

    - chmod 777 - rwx for everyone
    - chmod 755 - rw for owner. rx for group world

SOME OTHERS
-----------

1. `grep pattern files`
   - Search in files for pattern
2. `grep -r pattern dir`
   - Search for pattern recursively in directory
3. `locate file`
    - Find all iinstances of file
4. `whereis app`
    - Show possible locations of app
5. `man command`
   - Show manual page for given command
