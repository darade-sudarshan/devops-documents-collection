To automate the stopping and starting of all DEV instances at specific times (8 PM on Fridays for stopping, and 9 AM on Mondays for starting), you can use **Amazon EventBridge** to schedule these actions. Below is the step-by-step setup:

### Step 1: Tag DEV Instances
You should first tag the DEV EC2 instances to easily identify them for stopping and starting. This can be done through the AWS Console, CLI, or API.

1. **Go to the EC2 Console:**
   - Open the [Amazon EC2 Console](https://console.aws.amazon.com/ec2/v2/home).
   
2. **Tag Instances:**
   - Select all the DEV instances.
   - Click on **Tags** > **Manage Tags**.
   - Add a tag with the following key-value pair:
     - **Key**: `Environment`
     - **Value**: `DEV`

### Step 2: Create an IAM Role for EventBridge to Control EC2
Ensure EventBridge has permission to stop and start EC2 instances.

1. **Go to IAM Console:**
   - Open the [IAM Console](https://console.aws.amazon.com/iam).
   
2. **Create an IAM Role:**
   - Click **Roles** > **Create Role**.
   - Choose **EventBridge** as the service that will use this role.
   - Attach the **AmazonEC2FullAccess** policy or a custom policy that allows EC2 start and stop actions.

3. **Custom Policy Example**:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "ec2:StartInstances",
           "ec2:StopInstances"
         ],
         "Resource": "*"
       }
     ]
   }
   ```

---

### Step 3: Create an EventBridge Rule to Stop DEV Instances on Fridays at 8 PM
1. **Go to the EventBridge Console:**
   - Open the [Amazon EventBridge Console](https://console.aws.amazon.com/events).

2. **Create Rule for Stopping:**
   - Click **Rules** > **Create rule**.
   - Enter a **name** (e.g., `StopDEVInstancesFriday`).
   - For **Rule type**, choose **Schedule**.

3. **Define Schedule Expression**:
   - Choose **Cron expression**.
   - Use the following cron expression to stop instances at 8 PM every Friday:
     ```
     0 20 * * 5
     ```
   - This means at 20:00 (8 PM) on Fridays.

4. **Set Target:**
   - For **Target**, choose **EC2** > **StopInstances**.
   - Add the following **Input Transformer** to filter instances by the `Environment` tag:
     ```json
     {
       "instancesSet": [
         {
           "instanceId": <$.detail.instance-id>
         }
       ]
     }
     ```

---

### Step 4: Create an EventBridge Rule to Start DEV Instances on Mondays at 9 AM
1. **Create Rule for Starting:**
   - Go back to **EventBridge** > **Create rule**.
   - Enter a **name** (e.g., `StartDEVInstancesMonday`).
   - For **Rule type**, choose **Schedule**.

2. **Define Schedule Expression**:
   - Choose **Cron expression**.
   - Use the following cron expression to start instances at 9 AM every Monday:
     ```
     0 9 * * 1
     ```
   - This means at 9:00 AM on Mondays.

3. **Set Target:**
   - For **Target**, choose **EC2** > **StartInstances**.
   - Use the same **Input Transformer** to filter DEV instances by the `Environment` tag.

---

### Step 5: Testing
1. **Manually Trigger Rules:**
   - You can manually trigger both the stop and start rules from the EventBridge Console to test them.
   
2. **Check Instances:**
   - After creating these rules, check the EC2 console to ensure your DEV instances stop on Fridays at 8 PM and start on Mondays at 9 AM.

---

### Optional: Verify Notifications
If you want to verify that the instances were stopped/started successfully, you can set up **SNS** notifications (similar to the first solution) to get notified when the instances are stopped or started. This is helpful for keeping track of automation actions.
