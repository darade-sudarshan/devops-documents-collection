### **Hands-On Demo: S3 Trigger with Lambda**

Now, let's create a more advanced example where Lambda is triggered by an event in S3.

#### **Scenario**:
Whenever a file is uploaded to an S3 bucket, the Lambda function will be triggered to process the file.

#### **Design**:
![image](https://github.com/user-attachments/assets/927079fe-2fd0-4e78-9be0-3ace9bb1d1aa)

#### **Step 1: Create an S3 Bucket**
1. **Go to S3 Console**:
   - Open the AWS S3 console and create a new bucket (e.g., `my-lambda-trigger-bucket`).

2. **Enable S3 Event Notifications**:
   - In the **Properties** tab of the S3 bucket, scroll down to **Event notifications**.
   - Click on **Create event notification** and set the event type to **All object create events**.
   - Set the destination to **Lambda function** and choose your previously created Lambda function (`MyFirstLambda`).

#### **Step 2: Modify Lambda Function to Process S3 Events**

1. **Modify the Lambda Code**:
   - Update the Lambda function to process the S3 event. Replace the old code with this new Python code:
   
   ```python
   import json

   def lambda_handler(event, context):
       # Get the S3 bucket and object key from the event
       bucket = event['Records'][0]['s3']['bucket']['name']
       key = event['Records'][0]['s3']['object']['key']
       
       print(f"File uploaded: {key} to bucket: {bucket}")
       
       return {
           'statusCode': 200,
           'body': json.dumps(f'File {key} uploaded to bucket {bucket}')
       }
   ```
   This code processes the S3 event and logs the file name and bucket name.

2. **Deploy the Code**:
   - Click **Deploy** to save and deploy the updated function.

#### **Step 3: Creating SNS email notification as destination**

#### **Step 4: Upload a File to the S3 Bucket**

1. **Upload a Test File**:
   - Go to your S3 bucket and upload any file (e.g., `testfile.txt`).
   
2. **Check the Logs**:
   - Go to the **CloudWatch Logs** console, find the log group for your Lambda function, and check the logs.
   - You should see an entry similar to:
     ```
     File uploaded: testfile.txt to bucket: my-lambda-trigger-bucket
     ```

---
