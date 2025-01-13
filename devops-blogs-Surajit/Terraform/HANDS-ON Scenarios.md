# Terraform Use-Case

### I. Create and AWS 3 tier Architecture Infra with below details -
	1. Create a VPC with 3 Subnets(1 public and 2 Private), IGW, NGW, and routes for Private Subnets and Public Subnets in Mumbai Region.
	2. Create httpd web server in public subnet, Application server in private subnet 1 and DB in  Private Subnet 2.
	3. Create 4 security groups	-
		i) App Srv which will have inbound access for Web Server port only.
		ii) DB sg which will have inbound access for app srv
		iii) ALB SG which will have IP and Port allowed of SG only.
	4. Create ALB with HTTP listner redirects to web server and HTTPS Listner redirects to DNS(multicloudyug.com)
	5. Store the DB secrets in AWS Secrets Manager.
	6. Encrypt the Root EBS volumens. Use AWS Managed KMS Key for EBS root vol.

### II. Use Terraform Modules as per industry standards by maintaining each services in different modules for reusability.

### III. Create the infra for DEV, UAT and PROD environment using Terraform Workspaces.

### IV. Check-in the entire code in GitHub(except statefile and lock). Store the State file remotely in S3 Bucket and Lock in DynamoDB.
