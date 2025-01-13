
### 1. **ls** - List directory contents
```bash
ls -l
```
Shows a detailed list of all files and directories in the current directory.

### 2. **cd** - Change directory
```bash
cd /home/user
```
Navigates to the `/home/user` directory.

### 3. **pwd** - Print working directory
```bash
pwd
```
Displays the current directory you are in.

### 4. **mkdir** - Make directory
```bash
mkdir myfolder
```
Creates a new directory named `myfolder`.

### 5. **rmdir** - Remove directory
```bash
rmdir myfolder
```
Deletes the `myfolder` directory (only if it is empty).

### 6. **touch** - Create an empty file
```bash
touch file.txt
```
Creates an empty file named `file.txt`.

### 7. **rm** - Remove file or directory
```bash
rm file.txt
```
Deletes `file.txt`. To remove directories and their contents recursively:
```bash
rm -r foldername
```

### 8. **cp** - Copy files and directories
```bash
cp file1.txt file2.txt
```
Copies `file1.txt` to `file2.txt`. To copy directories:
```bash
cp -r folder1 folder2
```

### 9. **mv** - Move or rename files
```bash
mv file1.txt file2.txt
```
Renames or moves `file1.txt` to `file2.txt`.

### 10. **cat** - Concatenate and display file contents
```bash
cat file.txt
```
Displays the contents of `file.txt`.

### 11. **more** - View file content interactively
```bash
more file.txt
```
Allows interactive file viewing, showing a screen of text at a time.

### 12. **less** - View file content interactively (more advanced than more)
```bash
less file.txt
```
Allows backward navigation in files.

### 13. **head** - Display the beginning of a file
```bash
head file.txt
```
Shows the first 10 lines of `file.txt`.

### 14. **tail** - Display the end of a file
```bash
tail file.txt
```
Shows the last 10 lines of `file.txt`.

### 15. **grep** - Search inside files
```bash
grep "word" file.txt
```
Searches for the word “word” in `file.txt`.

### 16. **find** - Search for files
```bash
find /home -name "file.txt"
```
Searches for `file.txt` starting from the `/home` directory.

### 17. **chmod** - Change file permissions
```bash
chmod 755 file.txt
```
Changes the permissions of `file.txt` to be readable, writable, and executable by the owner, and readable and executable by others.

### 18. **chown** - Change file owner and group
```bash
chown user:group file.txt
```
Changes the owner of `file.txt` to `user` and its group to `group`.

### 19. **ps** - List running processes
```bash
ps aux
```
Displays a detailed list of all running processes.

### 20. **kill** - Terminate processes
```bash
kill 1234
```
Terminates the process with PID `1234`.

### 21. **df** - Display disk space usage
```bash
df -h
```
Shows the disk space usage of file systems in a human-readable format.

### 22. **du** - Estimate file space usage
```bash
du -sh foldername
```
Displays the size of the directory `foldername`.

### 23. **top** - Display running processes
```bash
top
```
Displays a real-time view of running processes and system resources.

### 24. **htop** - Interactive process viewer (more user-friendly than top)
```bash
htop
```
An interactive and detailed view of system processes.

### 25. **ifconfig** - Display network configuration (older version)
```bash
ifconfig
```
Shows network interface configurations.

### 26. **ip** - Show/manipulate routing, devices, and network interfaces
```bash
ip a
```
Displays detailed network interface and IP address information.

### 27. **ping** - Check network connectivity
```bash
ping google.com
```
Sends ICMP packets to `google.com` to test connectivity.

### 28. **wget** - Download files from the internet
```bash
wget https://example.com/file.zip
```
Downloads `file.zip` from the URL.

### 29. **curl** - Transfer data to/from a server
```bash
curl https://example.com
```
Downloads and displays the contents of `https://example.com`.

### 30. **tar** - Archive files
```bash
tar -cvf archive.tar foldername
```
Creates an archive `archive.tar` from the directory `foldername`. To extract:
```bash
tar -xvf archive.tar
```

### 31. **zip** - Compress files into a ZIP archive
```bash
zip archive.zip file1.txt file2.txt
```
Creates a ZIP archive `archive.zip` from `file1.txt` and `file2.txt`.

### 32. **unzip** - Extract files from a ZIP archive
```bash
unzip archive.zip
```
Extracts files from `archive.zip`.

### 33. **nano** - Command-line text editor
```bash
nano file.txt
```
Opens `file.txt` for editing in the Nano editor.

### 34. **vim** - Command-line text editor (more advanced than nano)
```bash
vim file.txt
```
Opens `file.txt` for editing in the Vim editor.

### 35. **scp** - Secure copy (remote file transfer over SSH)
```bash
scp file.txt user@remote:/path/to/destination
```
Copies `file.txt` to the remote server at `/path/to/destination`.

### 36. **rsync** - Sync files between systems
```bash
rsync -avz /local/path user@remote:/remote/path
```
Syncs files from the local machine to a remote machine.

### 37. **man** - Display manual for a command
```bash
man ls
```
Shows the manual page for the `ls` command.

### 38. **history** - Show command history
```bash
history
```
Displays a list of previously run commands.

### 39. **alias** - Create a shortcut for a command
```bash
alias ll='ls -l'
```
Creates an alias `ll` for `ls -l`.

### 40. **uname** - Display system information
```bash
uname -a
```
Shows detailed system information, including kernel version.

### 41. **df** - Display disk space usage
```bash
df -h
```
Shows disk usage in a human-readable format.

### 42. **free** - Display memory usage
```bash
free -h
```
Displays system memory and swap usage in a human-readable format.

### 43. **uptime** - Display system uptime
```bash
uptime
```
Shows how long the system has been running, along with the load average.

### 44. **reboot** - Reboot the system
```bash
sudo reboot
```
Reboots the system immediately.

### 45. **shutdown** - Shutdown the system
```bash
sudo shutdown now
```
Shuts down the system immediately.

### 46. **useradd** - Add a new user
```bash
sudo useradd username
```
Creates a new user with the name `username`.

### 47. **passwd** - Change user password
```bash
passwd
```
Prompts to change the password of the current user.

### 48. **groupadd** - Add a new group
```bash
sudo groupadd groupname
```
Creates a new group called `groupname`.

### 49. **chmod** - Change file permissions
```bash
chmod 644 file.txt
```
Sets the permissions of `file.txt` to be readable and writable by the owner, and readable by others.

### 50. **chown** - Change file ownership
```bash
sudo chown user:group file.txt
```
Changes the ownership of `file.txt` to `user` and its group to `group`.

### 51. **stat** - Display file or file system status
```bash
stat file.txt
```
Shows detailed information about `file.txt` such as size, permissions, and timestamps.

### 52. **ln** - Create links between files
```bash
ln -s /path/to/file symlink
```
Creates a symbolic link `symlink` pointing to `/path/to/file`.

### 53. **tr** - Translate or delete characters
```bash
echo "HELLO" | tr 'A-Z' 'a-z'
```
Converts the text from uppercase to lowercase.

### 54. **cut** - Remove sections from each line of files
```bash
cut -d':' -f1 /etc/passwd
```
Cuts and displays the first field (before `:`) from the `/etc/passwd` file.

### 55. **sort** - Sort lines of text files
```bash
sort file.txt
```
Sorts the lines in `file.txt` alphabetically.

### 56. **uniq** - Report or omit repeated lines
```bash
uniq file.txt
```
Removes consecutive duplicate lines from `file.txt`.

### 57. **wc** - Word, line, character, and byte count
```bash
wc file.txt
```
Displays the number of lines, words, and characters in `file.txt`.

### 58. **diff** - Compare files line by line
```bash
diff file1.txt file2.txt
```
Shows the differences between `file1.txt` and `file2.txt`.

### 59. **chmod** - Change permissions of files or directories
```bash
chmod u+x script.sh
```
Grants execute permission to the user for `script.sh`.

### 60. **chgrp** - Change group ownership
```bash
chgrp groupname file.txt
```
Changes the group of `file.txt` to `groupname`.

### 61. **df** - Display disk space usage of file systems
```bash
df -h
```
Shows disk space usage in a human-readable format for all mounted file systems.

### 62. **du** - Estimate file space usage
```bash
du -sh foldername
```
Displays the total size of `foldername`.

### 63. **file** - Determine file type
```bash
file file.txt
```
Determines and displays the file type of `file.txt`.

### 64. **env** - Display or set environment variables
```bash
env
```
Shows all the current environment variables.

### 65. **export** - Export environment variables
```bash
export VAR=value
```
Sets and exports the environment variable `VAR` with the value `value`.

### 66. **basename** - Strip directory and suffix from filenames
```bash
basename /home/user/file.txt
```
Returns just `file.txt` without the directory path.

### 67. **dirname** - Get directory path from a filename
```bash
dirname /home/user/file.txt
```
Returns `/home/user` as the directory path.

### 68. **uptime** - Show how long the system has been running
```bash
uptime
```
Displays system uptime and load averages.

### 69. **history** - Display the history of commands
```bash
history
```
Lists the command history for the current session.

### 70. **tee** - Read from standard input and write to standard output and files
```bash
echo "Hello" | tee file.txt
```
Writes "Hello" to both the screen and `file.txt`.

### 71. **xargs** - Build and execute command lines from standard input
```bash
cat file.txt | xargs rm
```
Deletes all the files listed in `file.txt`.

### 72. **which** - Locate a command
```bash
which python
```
Shows the full path of the `python` executable.

### 73. **whereis** - Locate binaries, source, and manual pages for a command
```bash
whereis ls
```
Displays the location of `ls` binary, source code, and manual page.

### 74. **echo** - Display a line of text
```bash
echo "Hello, World!"
```
Prints "Hello, World!" to the screen.

### 75. **bc** - Command-line calculator
```bash
echo "5+5" | bc
```
Performs the calculation `5+5` and displays the result.

### 76. **df** - Display disk space usage of file systems
```bash
df -h /home
```
Displays available disk space in the `/home` directory in a human-readable format.

### 77. **jobs** - List active jobs
```bash
jobs
```
Displays the list of running jobs.

### 78. **fg** - Bring a background job to the foreground
```bash
fg %1
```
Brings job `1` to the foreground.

### 79. **bg** - Resume a suspended job in the background
```bash
bg %1
```
Resumes job `1` in the background.

### 80. **fgrep** - Search fixed strings within files
```bash
fgrep "text" file.txt
```
Searches for the exact string "text" in `file.txt`.

### 81. **egrep** - Search extended regular expressions
```bash
egrep "text[0-9]" file.txt
```
Searches for text followed by a number.

### 82. **sed** - Stream editor for filtering and transforming text
```bash
sed 's/old/new/g' file.txt
```
Replaces all occurrences of "old" with "new" in `file.txt`.

### 83. **awk** - Pattern scanning and processing language
```bash
awk '{print $1}' file.txt
```
Prints the first field from each line of `file.txt`.

### 84. **at** - Schedule a command to run at a later time
```bash
echo "shutdown now" | at 10:00
```
Schedules a system shutdown at 10:00.

### 85. **crontab** - Schedule regular tasks using cron
```bash
crontab -e
```
Opens the cron table for editing to schedule tasks.

### 86. **uptime** - Displays the time for how long the system has been running
```bash
uptime
```
Shows system uptime and current load average.

### 87. **df** - Displays the amount of disk space available on the file system
```bash
df -h
```
Displays available disk space in a human-readable format.

### 88. **hostname** - Display or set the system’s hostname
```bash
hostname
```
Prints the system's hostname.

### 89. **mount** - Mount a filesystem
```bash
mount /dev/sda1 /mnt
```
Mounts the `/dev/sda1` partition to `/mnt`.

### 90. **umount** - Unmount a filesystem
```bash
umount /mnt
```
Unmounts the filesystem at `/mnt`.

### 91. **lsblk** - List block devices
```bash
lsblk
```
Displays a list of block devices (e.g., hard drives and partitions).

### 92. **iostat** - CPU and I/O statistics
```bash
iostat
```
Displays CPU and I/O performance statistics.

### 93. **uptime** - Display system uptime and load average
```bash
uptime
```
Shows how long the system has been running and the system load.

### 94. **sysctl** - Modify kernel parameters at runtime
```bash
sysctl -a
```
Displays all kernel parameters.

### 95. **uname** - Print system information
```bash
uname -r
```
Displays the kernel version of the system.

### 96. **lsof** - List open files
```bash
lsof
```
Shows a list of files that are currently open.

### 97. **dmesg** - Print system boot messages
```bash
dmesg
```
Displays kernel-related messages, typically from system boot.

### 98. **ss** - Display network socket information
```bash
ss -tuln
```
Displays listening sockets.

### 99. **service** - Control system services
```bash
sudo service apache2 start
```
Starts the Apache service.

### 100. **systemctl** - Control the systemd system and services
```bash
sudo systemctl status nginx
```
Displays the status of the NGINX service.

---
