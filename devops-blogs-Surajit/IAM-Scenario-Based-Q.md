100 scenario-based interview questions for AWS Identity and Access Management (IAM).

### 1. **Scenario:** You need to ensure that an IAM user can only view EC2 instances but not modify or delete them.
   - **Answer:** Create an IAM policy that grants `DescribeInstances` permissions for EC2 but denies actions like `TerminateInstances`, `StartInstances`, and `StopInstances`.

### 2. **Scenario:** How would you implement a policy that allows a user to manage S3 buckets but not access the objects within?
   - **Answer:** Create a policy with `s3:ListBucket`, `s3:CreateBucket`, and `s3:DeleteBucket` permissions but exclude `s3:GetObject`, `s3:PutObject`, and `s3:DeleteObject` actions.

### 3. **Scenario:** An IAM user needs temporary access to AWS resources. How would you implement this?
   - **Answer:** Use AWS Security Token Service (STS) to create a temporary session token with limited permissions and set a time limit for this token.

### 4. **Scenario:** How do you restrict an IAM user from accessing specific regions?
   - **Answer:** Implement a policy with a `Condition` key `aws:RequestedRegion` to limit access to only certain regions or deny access to others.

### 5. **Scenario:** You need to grant a third-party application limited access to your AWS resources. What would you do?
   - **Answer:** Create a role with specific permissions and allow the third party to assume the role using STS with a trust policy that allows the external entity to assume the role.

### 6. **Scenario:** How would you handle the situation where multiple IAM users require the same level of access?
   - **Answer:** Create an IAM group with the required policies and add the users to this group, thereby granting them the necessary permissions collectively.

### 7. **Scenario:** A user needs access to S3, but only to a specific bucket. How would you set this up?
   - **Answer:** Attach a policy to the user that grants `s3:*` actions on a specific bucket using a resource ARN like `arn:aws:s3:::example-bucket/*`.

### 8. **Scenario:** How would you enforce MFA (Multi-Factor Authentication) for sensitive operations?
   - **Answer:** Implement a policy with the `Condition` element requiring `aws:MultiFactorAuthPresent` for critical actions.

### 9. **Scenario:** How do you ensure an IAM user can only change their password and not any other credentials?
   - **Answer:** Attach a policy with `iam:ChangePassword` permission and deny actions like `iam:UpdateLoginProfile`.

### 10. **Scenario:** How do you grant an IAM user access to CloudWatch logs but restrict access to creating or deleting log groups?
   - **Answer:** Create a policy allowing `logs:PutLogEvents` and `logs:DescribeLogGroups` while denying `logs:CreateLogGroup` and `logs:DeleteLogGroup`.

### 11. **Scenario:** How would you audit the actions performed by IAM users?
   - **Answer:** Enable AWS CloudTrail to log all actions performed by IAM users across your account.

### 12. **Scenario:** How can you implement a policy that allows only read access to RDS databases?
   - **Answer:** Attach a policy that includes `rds:DescribeDBInstances` and `rds:DescribeDBClusters` while excluding any write operations.

### 13. **Scenario:** How would you allow access to the AWS Management Console for only specific services?
   - **Answer:** Create a policy that grants console access to only specific services like EC2, S3, etc., using service-specific actions like `ec2:DescribeInstances` and `s3:ListBucket`.

### 14. **Scenario:** You need to revoke all active IAM sessions for a compromised user account. How would you do it?
   - **Answer:** Use the `aws iam delete-access-key` command to deactivate the access keys, or create a policy that denies all permissions temporarily.

### 15. **Scenario:** How do you prevent an IAM user from accidentally deleting CloudFormation stacks?
   - **Answer:** Attach a policy that explicitly denies `cloudformation:DeleteStack`.

### 16. **Scenario:** A user must be able to manage IAM users but not groups. How would you configure this?
   - **Answer:** Attach a policy with permissions like `iam:CreateUser`, `iam:DeleteUser`, and `iam:UpdateUser` but deny actions related to groups like `iam:CreateGroup`, `iam:DeleteGroup`.

### 17. **Scenario:** How would you allow a developer to deploy code to AWS Lambda but restrict them from managing IAM roles?
   - **Answer:** Attach a policy allowing `lambda:CreateFunction`, `lambda:UpdateFunctionCode`, and similar actions but deny `iam:PassRole` and `iam:CreateRole`.

### 18. **Scenario:** How do you enforce a naming convention on IAM roles and users?
   - **Answer:** Use a combination of AWS Config rules and policies with `Condition` elements to check and enforce naming patterns.

### 19. **Scenario:** A user should only have read access to DynamoDB tables. How do you achieve this?
   - **Answer:** Attach a policy with `dynamodb:GetItem`, `dynamodb:Query`, and `dynamodb:Scan` actions on the specific table(s).

### 20. **Scenario:** How do you ensure an IAM user can only access EC2 instances tagged with a specific key-value pair?
   - **Answer:** Use a policy with a `Condition` element that matches the `ec2:ResourceTag` key to the specific value required.

### 21. **Scenario:** How would you create an IAM role that can only be assumed by certain trusted AWS accounts?
   - **Answer:** Define a trust policy for the role that specifies the trusted AWS accounts under the `Principal` element.

### 22. **Scenario:** How do you prevent an IAM user from creating IAM roles with administrative access?
   - **Answer:** Use a policy that denies `iam:CreateRole` or `iam:PutRolePolicy` when the role policy contains actions like `*`.

### 23. **Scenario:** How can you ensure all IAM policies in your account are reviewed before being used?
   - **Answer:** Use AWS Config with a custom rule to evaluate IAM policies for compliance before they are attached to any IAM entity.

### 24. **Scenario:** How would you implement a policy that only allows access to resources during business hours?
   - **Answer:** Create a policy with a `Condition` key `aws:RequestTime` to restrict access to specific hours of the day.

### 25. **Scenario:** How do you restrict access to AWS resources based on the source IP address?
   - **Answer:** Implement a policy with a `Condition` key `aws:SourceIp` to allow or deny access based on the IP address or range.

### 26. **Scenario:** How would you allow an IAM user to view billing information but not make any changes?
   - **Answer:** Attach a policy with `aws-portal:ViewBilling` permission and explicitly deny actions like `aws-portal:ModifyBilling`.

### 27. **Scenario:** How do you ensure that a user can only manage their own EC2 instances and not those of others?
   - **Answer:** Use a policy with a `Condition` element that limits actions based on the `ec2:ResourceTag/User` key.

### 28. **Scenario:** How do you allow an IAM user to access the AWS CLI but restrict their access to the AWS Management Console?
   - **Answer:** Attach a policy that allows CLI actions but restricts console login actions like `iam:CreateLoginProfile`.

### 29. **Scenario:** A user requires access to an S3 bucket, but you want to log every action they perform. What would you do?
   - **Answer:** Enable S3 bucket logging and CloudTrail to track all actions performed on the bucket by the user.

### 30. **Scenario:** How would you create a policy that denies access to all actions unless specifically allowed?
   - **Answer:** Create a policy with a default deny (`Deny` on `*:*`), and then allow specific actions or resources as required.

### 31. **Scenario:** How do you prevent an IAM user from accidentally deleting their own access keys?
   - **Answer:** Attach a policy that denies `iam:DeleteAccessKey` if the `aws:username` condition matches their own username.

### 32. **Scenario:** How can you restrict a user from launching specific types of EC2 instances?
   - **Answer:** Use a policy with a `Condition` element restricting `ec2:InstanceType` to certain allowed values.

### 33. **Scenario:** How would you ensure an IAM user can only upload objects to S3 but cannot delete them?
   - **Answer:** Attach a policy allowing `s3:PutObject` but denying `s3:DeleteObject` actions on the bucket.

### 34. **Scenario:** How do you allow a user to create VPCs but prevent them from deleting existing ones?
   - **Answer:** Attach a policy allowing `ec2:CreateVpc` but denying `ec2:DeleteVpc`.

### 35. **Scenario:** How would you grant an IAM user access to an RDS instance but only through a specific IP address?
   - **Answer:** Implement a policy with a `Condition` key `aws:SourceIp` to restrict access based on the specific IP address.

### 36. **Scenario:** How do you audit access to IAM roles across your AWS

 environment?
   - **Answer:** Use AWS IAM Access Analyzer to monitor and audit access to roles, and review CloudTrail logs for role assumption actions.

### 37. **Scenario:** How would you enforce the use of strong passwords for all IAM users?
   - **Answer:** Implement an IAM password policy that requires a minimum length, complexity, and rotation.

### 38. **Scenario:** How do you ensure that only IAM roles, not users, can access certain S3 buckets?
   - **Answer:** Use a policy that denies access to S3 unless the principal is an IAM role by checking the `aws:PrincipalType` condition.

### 39. **Scenario:** How do you prevent users from accidentally escalating their privileges?
   - **Answer:** Implement a policy that denies actions like `iam:PutRolePolicy` or `iam:AttachUserPolicy` if they would grant broader permissions.

### 40. **Scenario:** How do you allow an IAM user to assume a role only within certain hours of the day?
   - **Answer:** Use a policy with a `Condition` key `aws:RequestTime` that allows role assumption only during the specified hours.

### 41. **Scenario:** How can you restrict an IAM user’s access to S3 objects based on the object’s tag?
   - **Answer:** Implement a policy with a `Condition` key that checks for the `s3:ExistingObjectTag` key-value pair.

### 42. **Scenario:** How would you limit a user’s access to AWS resources based on the AWS Organization they belong to?
   - **Answer:** Use a policy with a `Condition` key `aws:PrincipalOrgID` to restrict access based on the organization ID.

### 43. **Scenario:** How do you allow an IAM user to access only a specific Lambda function?
   - **Answer:** Attach a policy granting permissions like `lambda:InvokeFunction` on the specific Lambda function’s ARN.

### 44. **Scenario:** How would you allow an IAM user to manage only specific RDS instances based on their tags?
   - **Answer:** Implement a policy with a `Condition` key `rds:ResourceTag` that limits actions to instances with specific tags.

### 45. **Scenario:** How do you prevent IAM users from creating EC2 instances in a particular region?
   - **Answer:** Attach a policy that denies `ec2:RunInstances` for the specified region using the `aws:RequestedRegion` condition.

### 46. **Scenario:** How would you enforce role-based access control (RBAC) for multiple IAM users?
   - **Answer:** Create roles with specific permissions and assign IAM users to these roles using the `AssumeRole` permission.

### 47. **Scenario:** How do you ensure IAM users cannot modify security groups beyond a certain set of rules?
   - **Answer:** Attach a policy that denies actions like `ec2:AuthorizeSecurityGroupIngress` and `ec2:RevokeSecurityGroupIngress` if they do not match specific conditions.

### 48. **Scenario:** How would you allow a third-party vendor to access an S3 bucket while ensuring their access is logged?
   - **Answer:** Create a cross-account role that allows S3 access, ensure CloudTrail is enabled, and that logging is active for the bucket.

### 49. **Scenario:** How do you ensure that only approved AWS services can be launched by IAM users?
   - **Answer:** Implement a policy with a `Condition` key `ec2:ResourceTag` or `service:tag` to restrict launching services based on approved tags.

### 50. **Scenario:** How do you allow an IAM user to rotate their access keys but not create additional keys?
   - **Answer:** Attach a policy allowing `iam:UpdateAccessKey` but denying `iam:CreateAccessKey`.

### 51. **Scenario:** How do you restrict an IAM user’s access to EC2 instances based on instance state?
   - **Answer:** Implement a policy with a `Condition` element based on `ec2:InstanceState` to restrict actions based on the state of the instance.

### 52. **Scenario:** How do you allow an IAM user to assume a role only if MFA is enabled?
   - **Answer:** Create a policy that requires `aws:MultiFactorAuthPresent` in the `Condition` element for assuming the role.

### 53. **Scenario:** How do you grant a user access to S3 but restrict them from listing all buckets?
   - **Answer:** Attach a policy allowing specific S3 actions on certain buckets but denying `s3:ListAllMyBuckets`.

### 54. **Scenario:** How would you restrict an IAM user’s access to certain EC2 instance types?
   - **Answer:** Implement a policy that allows `ec2:RunInstances` only if the `ec2:InstanceType` condition matches specific allowed types.

### 55. **Scenario:** How do you ensure an IAM user can only manage CloudWatch alarms for specific metrics?
   - **Answer:** Attach a policy allowing actions like `cloudwatch:PutMetricAlarm` but restrict it to specific metrics using a `Condition` element.

### 56. **Scenario:** How do you enforce access to a DynamoDB table based on the items’ attributes?
   - **Answer:** Implement a policy with a `Condition` key that restricts access based on the `dynamodb:LeadingKeys` condition.

### 57. **Scenario:** How would you allow an IAM user to access only specific services in the AWS Management Console?
   - **Answer:** Attach a policy with service-specific permissions and restrict console access to only those services.

### 58. **Scenario:** How do you ensure IAM users can only access S3 buckets in a specific AWS region?
   - **Answer:** Use a policy with a `Condition` key `aws:RequestedRegion` to restrict access to S3 buckets based on the region.

### 59. **Scenario:** How would you allow a user to manage Lambda functions but restrict them from managing API Gateway?
   - **Answer:** Attach a policy that allows Lambda actions like `lambda:CreateFunction` but denies API Gateway actions like `apigateway:*`.

### 60. **Scenario:** How do you restrict IAM users from accessing AWS resources after working hours?
   - **Answer:** Implement a policy with a `Condition` key `aws:RequestTime` to deny access during off-hours.

### 61. **Scenario:** How would you ensure an IAM user can only assume roles that are tagged with specific values?
   - **Answer:** Use a policy with a `Condition` key `iam:ResourceTag` to restrict role assumption based on tags.

### 62. **Scenario:** How do you prevent IAM users from creating new VPCs?
   - **Answer:** Attach a policy that denies `ec2:CreateVpc`.

### 63. **Scenario:** How do you restrict an IAM user’s access to S3 objects based on the object size?
   - **Answer:** Use a policy with a `Condition` key `s3:ContentLength` to restrict access based on the size of the objects.

### 64. **Scenario:** How would you allow an IAM user to only view the contents of an S3 bucket?
   - **Answer:** Attach a policy granting `s3:ListBucket` and `s3:GetObject` permissions for the specific bucket.

### 65. **Scenario:** How do you prevent an IAM user from attaching policies that contain full administrative access?
   - **Answer:** Attach a policy that denies actions like `iam:PutUserPolicy` if the policy contains `*` permissions.

### 66. **Scenario:** How would you enforce a limit on the number of IAM users in your account?
   - **Answer:** Use AWS Config with a custom rule to monitor and alert when the number of IAM users exceeds a certain threshold.

### 67. **Scenario:** How do you ensure IAM users can only manage CloudFormation stacks tagged with a specific value?
   - **Answer:** Implement a policy with a `Condition` key `cloudformation:ResourceTag` to restrict management based on tags.

### 68. **Scenario:** How do you allow a user to access EC2 instances only if they are part of a specific Auto Scaling group?
   - **Answer:** Use a policy with a `Condition` key `ec2:ResourceTag/AutoScalingGroupName` to restrict access based on the Auto Scaling group name.

### 69. **Scenario:** How would you restrict access to AWS resources based on the requester's account ID?
   - **Answer:** Implement a policy with a `Condition` key `aws:PrincipalAccount` to allow or deny access based on the account ID.

### 70. **Scenario:** How do you allow an IAM user to access only S3 buckets that they have created?
   - **Answer:** Use a policy with a `Condition` key `aws:ResourceTag/CreatedBy` that allows access based on the creator’s identity.

### 71. **Scenario:** How do you prevent IAM users from modifying the root account’s credentials?
   - **Answer:** Implement a policy that denies actions like `iam:UpdateLoginProfile` and `iam:CreateAccessKey` for the root account.

### 72. **Scenario:** How would you enforce the use of SSL/TLS for accessing S3 buckets?
   - **Answer:** Use a policy with a `Condition` key `aws:SecureTransport` that requires SSL/TLS for accessing S3.

### 73. **Scenario:** How do you ensure that IAM users can only assume roles within their own account?
   - **Answer:** Implement a policy that allows role assumption only if the `aws:PrincipalAccount` matches the account ID.

### 74. **Scenario:** How do you allow an IAM user to access only specific resources within a CloudFormation stack?
   - **Answer:**

 Attach a policy with specific resource ARNs for the resources within the CloudFormation stack.

### 75. **Scenario:** How do you prevent an IAM user from creating new IAM policies?
   - **Answer:** Attach a policy that denies `iam:CreatePolicy`.

### 76. **Scenario:** How do you allow an IAM user to launch EC2 instances but only from specific AMIs?
   - **Answer:** Use a policy with a `Condition` key `ec2:ImageId` to restrict instance launches to specific AMIs.

### 77. **Scenario:** How would you restrict an IAM user’s access to S3 objects based on their content type?
   - **Answer:** Implement a policy with a `Condition` key `s3:ContentType` to allow or deny access based on the object’s content type.

### 78. **Scenario:** How do you allow an IAM user to manage EC2 key pairs but prevent them from viewing private keys?
   - **Answer:** Attach a policy allowing `ec2:CreateKeyPair` and `ec2:DeleteKeyPair` but denying actions like `ec2:DescribeKeyPairs` if it includes private key access.

### 79. **Scenario:** How do you ensure that only IAM roles can be used to launch certain EC2 instances?
   - **Answer:** Use a policy with a `Condition` key `aws:PrincipalType` to restrict launching EC2 instances to IAM roles only.

### 80. **Scenario:** How do you prevent IAM users from attaching policies that grant access to all resources?
   - **Answer:** Attach a policy that denies actions like `iam:AttachUserPolicy` if the policy grants `*:*` permissions.

### 81. **Scenario:** How do you allow a user to manage AWS budgets but restrict them from accessing billing information?
   - **Answer:** Attach a policy allowing `budgets:*` actions but denying `aws-portal:*` actions.

### 82. **Scenario:** How do you restrict an IAM user’s access to S3 objects based on the object’s encryption status?
   - **Answer:** Use a policy with a `Condition` key `s3:x-amz-server-side-encryption` to allow or deny access based on whether the object is encrypted.

### 83. **Scenario:** How do you allow an IAM user to create CloudFormation stacks but restrict them from deleting them?
   - **Answer:** Attach a policy allowing `cloudformation:CreateStack` but denying `cloudformation:DeleteStack`.

### 84. **Scenario:** How would you restrict access to AWS resources based on the time of year?
   - **Answer:** Use a policy with a `Condition` key `aws:RequestDate` to allow or deny access based on the time of year.

### 85. **Scenario:** How do you ensure that only IAM roles tagged with specific values can access certain resources?
   - **Answer:** Implement a policy with a `Condition` key `aws:ResourceTag` that restricts access based on the role’s tags.

### 86. **Scenario:** How do you allow an IAM user to access only specific VPC subnets?
   - **Answer:** Use a policy with a `Condition` key `ec2:Subnet` to restrict access to specific subnets.

### 87. **Scenario:** How do you prevent an IAM user from assuming roles in other AWS accounts?
   - **Answer:** Attach a policy that denies `sts:AssumeRole` unless the role is within the same account.

### 88. **Scenario:** How would you allow an IAM user to manage Elastic Load Balancers (ELBs) but restrict them from deleting them?
   - **Answer:** Attach a policy allowing ELB actions like `elasticloadbalancing:CreateLoadBalancer` but denying `elasticloadbalancing:DeleteLoadBalancer`.

### 89. **Scenario:** How do you allow an IAM user to access only S3 objects with a specific prefix?
   - **Answer:** Use a policy with a `Condition` key `s3:prefix` to restrict access based on the object’s prefix.

### 90. **Scenario:** How do you ensure IAM users cannot delete their own IAM policies?
   - **Answer:** Attach a policy that denies `iam:DeletePolicy` if the `aws:username` condition matches the policy creator.

### 91. **Scenario:** How do you allow an IAM user to access only a specific DynamoDB table?
   - **Answer:** Attach a policy with actions like `dynamodb:Query` and `dynamodb:Scan` for the specific table ARN.

### 92. **Scenario:** How do you restrict access to AWS resources based on the requester’s tag?
   - **Answer:** Implement a policy with a `Condition` key `aws:RequestTag` to allow or deny access based on the requester’s tags.

### 93. **Scenario:** How do you prevent IAM users from creating new IAM roles?
   - **Answer:** Attach a policy that denies `iam:CreateRole`.

### 94. **Scenario:** How do you ensure that only IAM roles with specific conditions can access your AWS resources?
   - **Answer:** Use a policy with a `Condition` key `aws:PrincipalTag` to restrict access based on the role’s tags.

### 95. **Scenario:** How do you allow an IAM user to access only specific API Gateway APIs?
   - **Answer:** Attach a policy granting actions like `execute-api:Invoke` for specific API Gateway resource ARNs.

### 96. **Scenario:** How do you ensure IAM users can only assume roles in a specific AWS account?
   - **Answer:** Implement a policy that restricts `sts:AssumeRole` to a specific account using the `aws:PrincipalAccount` condition.

### 97. **Scenario:** How do you allow an IAM user to manage SNS topics but restrict them from deleting topics?
   - **Answer:** Attach a policy allowing `sns:CreateTopic` and `sns:Subscribe` but denying `sns:DeleteTopic`.

### 98. **Scenario:** How do you restrict access to AWS resources based on the requester’s identity provider (IdP)?
   - **Answer:** Use a policy with a `Condition` key `aws:PrincipalArn` to restrict access based on the IdP’s ARN.

### 99. **Scenario:** How do you allow an IAM user to manage EC2 instances but restrict them from modifying instance metadata?
   - **Answer:** Attach a policy allowing EC2 actions like `ec2:StartInstances` but denying `ec2:ModifyInstanceMetadataOptions`.

### 100. **Scenario:** How do you ensure that IAM users can only access S3 buckets that are tagged with specific values?
   - **Answer:** Implement a policy with a `Condition` key `s3:ResourceTag` that restricts access based on the bucket’s tags.

These scenarios cover a wide range of IAM-related tasks and challenges, helping you prepare comprehensively for any IAM interview.
