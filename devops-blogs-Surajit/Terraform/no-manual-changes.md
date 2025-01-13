To ensure that your AWS infrastructure is fully managed through Terraform and that manual changes are not allowed (or at least flagged for review), you can implement several strategies. Here’s a detailed breakdown of how to achieve this:

### 1. **Enforce AWS IAM Policies**
   - **IAM Policies**: Create AWS IAM policies that restrict users' ability to make manual changes directly in the AWS Console or via the AWS CLI/API.
     - **Allow** only specific roles or users to perform changes via Terraform (e.g., through AWS CI/CD pipelines).
     - **Deny** permissions like `ec2:*`, `s3:*`, `rds:*`, etc., from roles that shouldn’t have access to make manual changes.

   **Example** IAM policy for restricting manual changes:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Deny",
         "Action": [
           "ec2:*",
           "s3:*",
           "rds:*"
         ],
         "Resource": "*",
         "Condition": {
           "StringNotEquals": {
             "aws:PrincipalArn": "arn:aws:iam::<account-id>:role/TerraformRole"
           }
         }
       }
     ]
   }
   ```

### 2. **Use AWS Config with Rules**
   - **AWS Config**: AWS Config helps in tracking and auditing any changes in the infrastructure. You can configure rules that detect manual changes in your resources and alert you.
     - For example, you can configure a rule that checks for non-compliance (i.e., any resource changes that did not originate from Terraform).
     - Use a custom **AWS Config Rule** that evaluates whether infrastructure is being managed solely by Terraform. You can create a Lambda function that flags resources not matching the Terraform state.

### 3. **Restrict AWS Console Access**
   - Limit access to the AWS Management Console to read-only roles. This ensures that only Terraform (or automation systems) can make changes to the infrastructure, while manual intervention is limited.
   - Use MFA (Multi-Factor Authentication) and strict policies to prevent ad-hoc changes.

### 4. **Implement Service Control Policies (SCPs) for AWS Organizations**
   - **SCPs**: If you’re managing multiple AWS accounts in an AWS Organization, use SCPs to limit the permissions available in the member accounts.
     - You can restrict manual modifications by denying actions except for those initiated by a specific role (such as a Terraform deployment role).
   - Example of denying manual EC2 instance creation:
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Deny",
           "Action": [
             "ec2:RunInstances"
           ],
           "Resource": "*",
           "Condition": {
             "StringNotEquals": {
               "aws:PrincipalArn": "arn:aws:iam::<account-id>:role/TerraformRole"
             }
           }
         }
       ]
     }
     ```

### 5. **Use Terraform’s `lifecycle` Block with `prevent_destroy`**
   - **Lifecycle Rules**: Terraform’s `lifecycle` block helps prevent manual deletion of infrastructure resources, ensuring that resources can only be deleted via Terraform.
     ```hcl
     resource "aws_instance" "example" {
       ami           = "ami-123456"
       instance_type = "t2.micro"
       
       lifecycle {
         prevent_destroy = true
       }
     }
     ```

### 6. **Automated Drift Detection**
   - **Terraform Plan**: Regularly run `terraform plan` to detect any infrastructure drift (i.e., manual changes not reflected in the Terraform code).
     - Integrate this in a CI/CD pipeline to run nightly or weekly checks.
   - You can also automate this process by sending alerts if any drift is detected.

### 7. **Auditing and Alerts (CloudWatch, CloudTrail, AWS Config)**
   - **AWS CloudTrail**: Enable CloudTrail to monitor and log all API activity in your AWS accounts. Create alarms on actions like EC2 instance creation or termination not originating from Terraform.
   - **CloudWatch Alarms**: Set up CloudWatch alarms to notify you of unexpected changes or unauthorized resource modifications.
   - **AWS Config Alerts**: Use Config rules to alert you about changes that deviate from your Terraform state.

### 8. **Integrate with CI/CD Pipelines**
   - Ensure that infrastructure changes can only be applied via a CI/CD pipeline that runs Terraform.
   - Implement approval mechanisms in the pipeline (e.g., a manual approval step before applying Terraform changes).

### 9. **Tagging Compliance Checks**
   - Use **resource tags** to identify Terraform-managed resources and configure AWS Config rules or custom scripts to validate that only tagged resources are modified.

### 10. **Deploy Terraform Cloud/Enterprise (Optional)**
   - **Terraform Cloud**: Use Terraform Cloud or Terraform Enterprise to centrally manage your Terraform state and enforce policies via Sentinel (policy as code). You can enforce policies that disallow manual changes to infrastructure.
     - Sentinel can be configured to block any changes not approved via Terraform.

By combining these strategies, you can effectively manage your AWS infrastructure through Terraform and minimize the risk of unauthorized manual changes.
