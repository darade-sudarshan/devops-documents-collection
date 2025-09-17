#!/bin/bash

########################
# Your application writes logs to /var/log/myapp/. You want to:
#    Compress logs older than 7 days
#    Delete logs older than 30 days
#    Automate it via a daily cron job
#########################

# Directory where logs are stored
LOG_DIR="/var/log/myapp"
LOG_FILE="/var/log/myapp/log_rotation.log"

# Ensure the log directory exists
if [ ! -d "$LOG_DIR" ]; then
    echo "[$(date)] ERROR: Log directory $LOG_DIR does not exist!" >> "$LOG_FILE"
    exit 1
fi

# Compress logs older than 7 days (but newer than 30)
find "$LOG_DIR" -type f -name "*.log" -mtime +7 -mtime -30 ! -name "*.gz" -exec gzip {} \; -exec echo "[$(date)] Compressed: {}" >> "$LOG_FILE" \;

# Delete compressed logs older than 30 days
find "$LOG_DIR" -type f -name "*.gz" -mtime +30 -exec rm -f {} \; -exec echo "[$(date)] Deleted: {}" >> "$LOG_FILE" \;

# Optional: Delete uncompressed logs older than 30 days
find "$LOG_DIR" -type f -name "*.log" -mtime +30 -exec rm -f {} \; -exec echo "[$(date)] Deleted (uncompressed): {}" >> "$LOG_FILE" \;

# Done
echo "[$(date)] Log rotation completed successfully." >> "$LOG_FILE"
