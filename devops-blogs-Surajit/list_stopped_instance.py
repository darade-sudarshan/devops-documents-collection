import boto3
import csv
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from datetime import datetime, timezone, timedelta

# List of AWS accounts (profile names) to check the instances status
aws_profiles = ['339713033591', '3397130334235', '339713067890']  # Replace with your profile names

# Filename for the output CSV file
output_file = 'stopped_ec2_instances.csv'

# Number of days to consider an instance as stopped.
days_stopped = 90

# Get the date 90 days ago from today
date_threshold = datetime.now(timezone.utc) - timedelta(days=days_stopped)

# Function to get all regions
def get_all_regions(session):
    ec2_client = session.client('ec2')
    response = ec2_client.describe_regions(AllRegions=True)
    regions = [region['RegionName'] for region in response['Regions']]
    return regions

# Function to get stopped instances in a specific region
def get_stopped_instances(session, region):
    ec2_client = session.client('ec2', region_name=region)
    response = ec2_client.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['stopped']
            }
        ]
    )
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # Check if the instance has been stopped for more than 'days_stopped' days
            launch_time = instance['LaunchTime']
            stopped_date = launch_time  # Placeholder; replace with accurate stopped date if available
            if (datetime.now(timezone.utc) - launch_time).days >= days_stopped:
                instances.append({
                    'AccountID': session.profile_name,
                    'Region': region,
                    'InstanceID': instance['InstanceId'],
                    'StoppedDate': stopped_date.strftime('%Y-%m-%d %H:%M:%S')
                })
    return instances

# Main function to get stopped instances across all regions and accounts
def main():
    all_instances = []
    
    for profile in aws_profiles:
        session = boto3.Session(profile_name=profile)
        regions = get_all_regions(session)
        
        for region in regions:
            try:
                instances = get_stopped_instances(session, region)
                all_instances.extend(instances)
            except NoCredentialsError:
                print(f"Credentials not available for profile {profile}. Skipping...")
            except PartialCredentialsError:
                print(f"Partial credentials found for profile {profile}. Skipping...")
            except Exception as e:
                print(f"An error occurred in profile {profile} in region {region}: {str(e)}")
    
    # Write the results to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['AccountID', 'Region', 'InstanceID', 'StoppedDate']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for instance in all_instances:
            writer.writerow(instance)
    
    print(f"Script executed successfully. Stopped instances saved to {output_file}.")

if __name__ == "__main__":
    main()

