#!/bin/bash

# List of services to monitor
services=("nginx" "sshd" "docker")

echo "-----------------------------------"
echo " Service Health Check Report"
echo "-----------------------------------"

# Loop through each service
for service in "${services[@]}"; do
    # Check service status
    if systemctl is-active --quiet "$service"; then
        echo "$service is ✅ RUNNING"
    else
        echo "$service is ❌ STOPPED"

        # Optional: Try to restart the service
        echo "Attempting to restart $service..."
        sudo systemctl restart "$service"

        # Re-check status
        if systemctl is-active --quiet "$service"; then
            echo "$service has been ✅ restarted successfully."
        else
            echo "⚠️  Failed to restart $service. Check logs."
        fi
    fi
    echo "-----------------------------------"
done
