To set up a notification system for stopped AWS EC2 instances using Amazon SNS and EventBridge, follow these steps:

### Prerequisites:
1. **AWS Account** with required permissions to manage EC2, SNS, and EventBridge.
2. **SNS Topic** created to receive notifications.
3. **IAM Role/Permissions** that allow EventBridge to publish to SNS.

### Step-by-Step Guide:

---

### Step 1: Create an SNS Topic
1. **Go to the SNS Console:**
   - Open the [Amazon SNS Console](https://console.aws.amazon.com/sns/v3/home).
2. **Create Topic:**
   - Click **Create topic**.
   - Choose **Standard** as the topic type.
   - Provide a **name** for the topic (e.g., `EC2StopNotification`).
   - Click **Create topic**.
3. **Create Subscription:**
   - Click on the newly created SNS topic.
   - Click **Create subscription**.
   - Select **Protocol** (Email, SMS, Lambda, etc.).
   - Enter the appropriate **Endpoint** (e.g., email address for email notifications).
   - Click **Create subscription**.

---

### Step 2: Create an EventBridge Rule for EC2 State Changes
1. **Go to the EventBridge Console:**
   - Open the [Amazon EventBridge Console](https://console.aws.amazon.com/events/home).
2. **Create a New Rule:**
   - In the navigation pane, select **Rules**.
   - Click **Create rule**.
   - Enter a **name** for the rule (e.g., `EC2StopStateRule`).
   - For **Rule type**, select **Event Pattern**.
3. **Configure the Event Pattern:**
   - Choose **Event source** as `AWS services`.
   - Under **AWS Service**, select **EC2**.
   - Under **Event type**, choose **EC2 Instance State-change Notification**.
   - Under **Specific states**, select **stopped**.
   - The event pattern should look like this:
     ```json
     {
       "source": ["aws.ec2"],
       "detail-type": ["EC2 Instance State-change Notification"],
       "detail": {
         "state": ["stopped"]
       }
     }
     ```
4. **Choose Target:**
   - In the **Select Targets** section, choose **SNS topic**.
   - Select the SNS topic you created earlier (e.g., `EC2StopNotification`).
5. **Configure Permissions:**
   - Ensure that EventBridge has permission to publish to your SNS topic.
   - EventBridge can automatically create an IAM role for this purpose.
6. **Create Rule:**
   - Click **Create** to save the rule.

---

### Step 3: Testing the Setup
1. **Stop an EC2 Instance:**
   - Open the [EC2 Console](https://console.aws.amazon.com/ec2/v2/home).
   - Select any running EC2 instance.
   - Click **Instance State** > **Stop Instance**.
2. **Check for Notification:**
   - Wait a few minutes.
   - Check your SNS subscription endpoint (e.g., email or SMS) for a notification that the EC2 instance has stopped.

---

This setup will send notifications via SNS whenever an EC2 instance enters a stopped state, leveraging EventBridge to monitor the state changes.
