
### 1. **Backup a Directory**
This script creates a backup of a directory and saves it as a compressed `.tar.gz` file.
```bash
#!/bin/bash
# Backup script for a directory

SOURCE="/path/to/source"
DEST="/path/to/destination/backup_$(date +%Y%m%d).tar.gz"

tar -czvf $DEST $SOURCE
echo "Backup of $SOURCE completed and stored in $DEST"
```

### 2. **Disk Usage Report**
This script provides a detailed disk usage report of the file system.
```bash
#!/bin/bash
# Disk usage report script

df -h | awk '{print $1, $5}' > disk_usage_report.txt
echo "Disk usage report generated: disk_usage_report.txt"
```

### 3. **Check if a Service is Running**
This script checks if a service (e.g., Apache) is running and restarts it if it’s not.
```bash
#!/bin/bash
# Check if Apache is running and restart if not

SERVICE="apache2"

if ! systemctl is-active --quiet $SERVICE; then
    echo "$SERVICE is not running, restarting..."
    systemctl start $SERVICE
else
    echo "$SERVICE is running"
fi
```

### 4. **Rename Files in Bulk**
This script renames all `.txt` files in a directory by adding a timestamp.
```bash
#!/bin/bash
# Rename .txt files in bulk by adding timestamp

for file in *.txt; do
    mv "$file" "${file%.txt}_$(date +%Y%m%d).txt"
done
echo "Renamed all .txt files with timestamp."
```

### 5. **Monitor CPU Usage**
This script monitors CPU usage and sends an alert if it exceeds a threshold.
```bash
#!/bin/bash
# Monitor CPU usage and alert if above threshold

THRESHOLD=80
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')

if (( $(echo "$CPU_USAGE > $THRESHOLD" | bc -l) )); then
    echo "Warning: CPU usage is above $THRESHOLD%. Current usage: $CPU_USAGE%"
else
    echo "CPU usage is normal: $CPU_USAGE%"
fi
```

### 6. **Find and Delete Old Files**
This script finds and deletes files older than 30 days in a specified directory.
```bash
#!/bin/bash
# Delete files older than 30 days

find /path/to/directory -type f -mtime +30 -exec rm {} \;
echo "Deleted files older than 30 days."
```

### 7. **Ping Multiple Servers**
This script pings a list of servers to check if they are reachable.
```bash
#!/bin/bash
# Ping multiple servers

SERVERS=("server1.com" "server2.com" "8.8.8.8")

for server in "${SERVERS[@]}"; do
    if ping -c 1 $server &> /dev/null; then
        echo "$server is reachable"
    else
        echo "$server is not reachable"
    fi
done
```

### 8. **User Account Creation**
This script automates the creation of user accounts with a default home directory and password.
```bash
#!/bin/bash
# Create a user account with a default password

read -p "Enter username: " USERNAME
useradd -m $USERNAME
echo "$USERNAME:password123" | chpasswd
echo "User $USERNAME created with default password."
```

### 9. **File Permission Check**
This script checks the permissions of a given file and outputs whether it's writable, readable, or executable.
```bash
#!/bin/bash
# Check file permissions

FILE="/path/to/file"

if [ -r $FILE ]; then
    echo "$FILE is readable"
fi

if [ -w $FILE ]; then
    echo "$FILE is writable"
fi

if [ -x $FILE ]; then
    echo "$FILE is executable"
fi
```

### 10. **System Uptime Report**
This script generates a report of the system's uptime.
```bash
#!/bin/bash
# System uptime report

UPTIME=$(uptime -p)
echo "System has been up for: $UPTIME"
```
Here are **20 more generic shell scripts** for common tasks, useful for system administration, automation, and monitoring:

### 11. **Automated System Update**
This script updates all packages on a Linux system.
```bash
#!/bin/bash
# Update system packages

sudo apt-get update -y && sudo apt-get upgrade -y
echo "System updated."
```

### 12. **Check Memory Usage**
This script checks the system's memory usage and sends an alert if usage exceeds a threshold.
```bash
#!/bin/bash
# Monitor memory usage

THRESHOLD=80
MEM_USAGE=$(free | grep Mem | awk '{print $3/$2 * 100.0}')

if (( $(echo "$MEM_USAGE > $THRESHOLD" | bc -l) )); then
    echo "Memory usage is above $THRESHOLD%. Current usage: $MEM_USAGE%"
else
    echo "Memory usage is normal: $MEM_USAGE%"
fi
```

### 13. **Archive Log Files**
This script compresses log files older than 7 days into a `.tar.gz` archive.
```bash
#!/bin/bash
# Archive old log files

find /var/log -type f -mtime +7 -exec tar -czvf logs_$(date +%Y%m%d).tar.gz {} +
echo "Archived old log files."
```

### 14. **Simple Database Backup (MySQL)**
This script creates a backup of a MySQL database.
```bash
#!/bin/bash
# MySQL database backup

DB_NAME="database_name"
DB_USER="username"
DB_PASS="password"
BACKUP_FILE="/path/to/backup/$(date +%Y%m%d)_$DB_NAME.sql"

mysqldump -u $DB_USER -p$DB_PASS $DB_NAME > $BACKUP_FILE
echo "Backup of $DB_NAME completed at $BACKUP_FILE"
```

### 15. **Check Open Ports**
This script checks for open ports on the system.
```bash
#!/bin/bash
# Check open ports

netstat -tuln | grep LISTEN
echo "Listed all open ports."
```

### 16. **Download a File Using `wget`**
This script downloads a file from a URL using `wget`.
```bash
#!/bin/bash
# Download file from a URL

URL="http://example.com/file.zip"
wget $URL -P /path/to/destination
echo "Downloaded file from $URL"
```

### 17. **Monitor Disk I/O Usage**
This script uses `iostat` to monitor disk I/O usage.
```bash
#!/bin/bash
# Monitor disk I/O usage

iostat -x 1 5
```

### 18. **Find Large Files**
This script finds files larger than 1GB in a specified directory.
```bash
#!/bin/bash
# Find files larger than 1GB

find /path/to/directory -type f -size +1G
```

### 19. **Generate SSH Key**
This script generates an SSH key pair for secure authentication.
```bash
#!/bin/bash
# Generate SSH key

ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa -N ""
echo "SSH key generated."
```

### 20. **Monitor Network Traffic**
This script uses `iftop` to monitor real-time network traffic.
```bash
#!/bin/bash
# Monitor network traffic

sudo iftop -i eth0
```

### 21. **Check Available Updates**
This script checks for available package updates on Ubuntu/Debian.
```bash
#!/bin/bash
# Check for available updates

apt list --upgradable
```

### 22. **Create a Swap File**
This script creates a swap file and activates it.
```bash
#!/bin/bash
# Create a swap file

sudo fallocate -l 1G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo "Swap file created and activated."
```

### 23. **Send an Email Notification**
This script sends an email notification using `mail` command.
```bash
#!/bin/bash
# Send email notification

echo "This is a test email" | mail -s "Test Subject" user@example.com
```

### 24. **Rotate Logs**
This script rotates log files by renaming them with a timestamp.
```bash
#!/bin/bash
# Rotate log files

LOG_FILE="/var/log/app.log"
mv $LOG_FILE $LOG_FILE.$(date +%Y%m%d)
touch $LOG_FILE
echo "Log file rotated."
```

### 25. **Reboot the System at Midnight**
This script schedules a system reboot at midnight.
```bash
#!/bin/bash
# Schedule reboot at midnight

echo "sudo reboot" | at 00:00
```

### 26. **Automated File Sync Using `rsync`**
This script synchronizes files between two directories using `rsync`.
```bash
#!/bin/bash
# Sync files between directories

rsync -av /source/directory/ /destination/directory/
echo "Files synchronized."
```

### 27. **Check System Information**
This script gathers system information such as OS version, CPU, and memory.
```bash
#!/bin/bash
# Check system information

echo "OS Version:"
lsb_release -a

echo "CPU Info:"
lscpu

echo "Memory Info:"
free -h
```

### 28. **Create and Extract a Tarball**
This script compresses a directory into a tarball and extracts it.
```bash
#!/bin/bash
# Create and extract tarball

# Compress directory
tar -czvf archive.tar.gz /path/to/directory

# Extract tarball
tar -xzvf archive.tar.gz -C /path/to/extract
```

### 29. **Count Files in a Directory**
This script counts the number of files in a specified directory.
```bash
#!/bin/bash
# Count files in a directory

DIRECTORY="/path/to/directory"
COUNT=$(ls -1 $DIRECTORY | wc -l)
echo "There are $COUNT files in $DIRECTORY."
```

### 30. **Monitor a Directory for Changes**
This script monitors a directory and prints changes in real-time.
```bash
#!/bin/bash
# Monitor directory for changes

DIRECTORY="/path/to/directory"
inotifywait -m $DIRECTORY
```

### 31. **Kill Processes by Name**
This script kills all processes by a specific name.
```bash
#!/bin/bash
# Kill processes by name

PROCESS_NAME="process_name"
pkill $PROCESS_NAME
echo "Killed all processes with name $PROCESS_NAME."
```

### 32. **Check Last Login**
This script checks the last login of all users on the system.
```bash
#!/bin/bash
# Check last login of users

lastlog
```

### 33. **Copy Files to Multiple Servers**
This script copies files to multiple remote servers using `scp`.
```bash
#!/bin/bash
# Copy files to multiple servers

SERVERS=("server1.com" "server2.com")
FILE="/path/to/file"

for server in "${SERVERS[@]}"; do
    scp $FILE user@$server:/path/to/destination
done
```

### 34. **Monitor Available RAM**
This script monitors available RAM and alerts if below a threshold.
```bash
#!/bin/bash
# Monitor available RAM

THRESHOLD=1000 # in MB
FREE_RAM=$(free -m | grep Mem | awk '{print $4}')

if (( FREE_RAM < THRESHOLD )); then
    echo "Warning: Available RAM is below $THRESHOLD MB. Current available: $FREE_RAM MB"
else
    echo "Available RAM is sufficient: $FREE_RAM MB"
fi
```

### 35. **Reboot on High Load**
This script reboots the system if the load average is too high.
```bash
#!/bin/bash
# Reboot on high system load

LOAD_THRESHOLD=5.0
LOAD=$(uptime | awk -F 'load average:' '{ print $2 }' | cut -d, -f1)

if (( $(echo "$LOAD > $LOAD_THRESHOLD" | bc -l) )); then
    echo "System load is high ($LOAD). Rebooting..."
    sudo reboot
else
    echo "System load is normal ($LOAD)."
fi
```

### 36. **Remove Duplicate Lines from a File**
This script removes duplicate lines from a file.
```bash
#!/bin/bash
# Remove duplicate lines

sort file.txt | uniq > file_no_duplicates.txt
echo "Removed duplicate lines from file.txt."
```

### 37. **Track User Login**
This script tracks user logins and writes the details to a log file.
```bash
#!/bin/bash
# Track user login

who | awk '{print $1 " logged in at " $4}' >> login.log
```

