To create **IAM Roles** that provide access across Organizational Units (OUs) in AWS Organizations, you typically follow a few important steps. The goal is to allow an IAM role from one AWS account (source) to assume a role in another AWS account (target) that belongs to a different OU, and access resources within that account.

### Step-by-Step Guide to Create IAM Roles for Cross-OU Access

#### **1. Enable Trusted Relationships Between AWS Accounts**
You must ensure that the source account (the account needing access) and the target account (the account where the resources are hosted) have a trust relationship. This involves setting up IAM roles that trust the source account.

#### **2. Identify the Role in the Target Account (Resource Account)**
In the target account where the resources are located, you'll create an IAM role that the source account can assume.

##### **Steps to Create IAM Role in Target Account:**

1. **Create a new IAM Role:**
   - Open the IAM console in the **target account**.
   - Select **Roles** and click **Create Role**.
   - Choose **Another AWS account** as the trusted entity.
   - Enter the Account ID of the **source account** (the account that will assume the role).
   - Enable external ID for added security (optional but recommended).

2. **Add permissions to the IAM Role:**
   - Attach the appropriate permission policies that allow access to the resources needed within the target account.
   - For example, if you want to allow access to S3 buckets, attach a policy like `AmazonS3ReadOnlyAccess` or create a custom policy as needed.

3. **Define the trust relationship policy**:
   - Go to the **Trust relationships** tab of the newly created role and ensure the trust policy allows the source account to assume this role. The policy would look something like this:

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::SOURCE_ACCOUNT_ID:root"
         },
         "Action": "sts:AssumeRole",
         "Condition": {}
       }
     ]
   }
   ```

   Replace `SOURCE_ACCOUNT_ID` with the ID of the account that will assume the role.

4. **Optionally limit the trust to an OU:**
   If you want to limit access to accounts within a specific OU, you can add a condition to the trust policy like this:

   ```json
   {
     "Effect": "Allow",
     "Principal": {
       "AWS": "arn:aws:iam::SOURCE_ACCOUNT_ID:root"
     },
     "Action": "sts:AssumeRole",
     "Condition": {
       "StringEquals": {
         "aws:PrincipalOrgID": "o-xxxxxxxxxx"
       }
     }
   }
   ```

   Replace `o-xxxxxxxxxx` with your AWS organization ID.

#### **3. Create an IAM Policy in the Source Account**
In the source account, create an IAM policy that allows the necessary users or services to assume the role in the target account.

1. **Create or update an IAM policy:**
   The IAM policy should allow the users or groups to assume the role created in the target account.

   Example IAM policy in the source account:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "sts:AssumeRole",
         "Resource": "arn:aws:iam::TARGET_ACCOUNT_ID:role/TargetRoleName"
       }
     ]
   }
   ```

   Replace `TARGET_ACCOUNT_ID` with the target account’s ID, and `TargetRoleName` with the name of the role created in the target account.

2. **Attach this policy** to the user, group, or service in the source account that requires access.

#### **4. Assume the Role from the Source Account**
To assume the role in the target account, you can use the AWS CLI, SDK, or console.

- **CLI Command to Assume Role:**

   ```bash
   aws sts assume-role \
     --role-arn "arn:aws:iam::TARGET_ACCOUNT_ID:role/TargetRoleName" \
     --role-session-name "SessionName"
   ```

This command returns temporary security credentials that you can use to access resources in the target account.

#### **5. Test the Cross-Account Access**
- After setting up, test the setup by assuming the role and trying to access the resources in the target account from the source account.

### Example Use Case: Cross-OU S3 Access
Let’s say you want to allow users in Account A (in OU A) to access an S3 bucket in Account B (in OU B):

1. **In Account B (target):**
   - Create an IAM role with the trust relationship for Account A.
   - Attach an S3 access policy (e.g., `AmazonS3ReadOnlyAccess`) to the role.

2. **In Account A (source):**
   - Create an IAM policy allowing users to assume the role from Account B.
   - Attach the policy to users/groups who need access.

### Best Practices for Cross-OU IAM Roles
- **Use IAM Roles** instead of sharing long-term credentials.
- **Apply least privilege**: Only grant the necessary permissions to the IAM role in the target account.
- **Use external IDs** for additional security when allowing external account access.
- **Monitor cross-account role access** using CloudTrail to ensure secure access and auditing.

This approach ensures secure, auditable, and manageable cross-account access across OUs.
