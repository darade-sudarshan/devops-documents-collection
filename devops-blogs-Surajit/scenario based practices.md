# BASIC

 1. VPC Setup and Configuration[DONE]
   - Create a custom VPC with public and private subnets across multiple Availability Zones. Set up route tables, Internet Gateways, and NAT Gateways to allow instances in the private subnet to access the internet.

 2. EC2 Auto Scaling[DONE]
   - Configure an Auto Scaling Group that launches EC2 instances based on CPU utilization. Test the scaling policies by generating load on the instances.

 3. Load Balancer Configuration[DONE]
   - Set up an Application Load Balancer to distribute traffic across multiple EC2 instances in different Availability Zones. Configure health checks and SSL termination.

 4. IAM Policies and Roles[DONE]
   - Create and attach custom IAM policies to users, groups, and roles. Set up a role for an EC2 instance to access S3 and DynamoDB.

 5. S3 Bucket Policies and Lifecycle Management[DONE]
   - Create an S3 bucket and configure bucket policies for public and private access. Set up lifecycle policies to automatically move objects to different storage classes and delete them after a specified time.

 6. CloudFront Distribution with S3 Origin[Done]
   - Configure a CloudFront distribution to serve content from an S3 bucket. Set up custom error pages and enable logging.

 7. RDS Multi-AZ Deployment[Done]
   - Launch an RDS instance with Multi-AZ failover. Simulate a failover and verify the high availability of the database.

 8. DynamoDB with Global Tables[Done]
   - Create a DynamoDB table with global tables enabled across multiple AWS regions. Insert data and verify its replication across regions.

 9. AWS Lambda with API Gateway
   - Create a Lambda function triggered by an API Gateway endpoint. Set up the API Gateway to handle different HTTP methods and pass data to the Lambda function.

 10. Elastic Beanstalk Deployment
   - Deploy a web application using AWS Elastic Beanstalk. Configure environment variables, scaling policies, and monitor the health of the environment.

 11. SQS and SNS Integration
   - Set up an SQS queue and SNS topic. Create a subscription to the SNS topic that sends messages to the SQS queue, and trigger an event using an SNS topic.

 12. EFS with EC2 Instances
   - Create an EFS file system and mount it to multiple EC2 instances. Test read/write access and file sharing between instances.

 13. Route 53 DNS Management
   - Configure a Route 53 hosted zone and create DNS records for a domain. Set up health checks and weighted routing policies.

 14. AWS Config with Compliance Rules
   - Enable AWS Config in your account and set up compliance rules for S3 bucket encryption and EC2 instance types. Monitor non-compliant resources.

 15. AWS Systems Manager Parameter Store
   - Store and retrieve configuration data and secrets using AWS Systems Manager Parameter Store. Use them in an EC2 instance or Lambda function.

 16. AWS Backup for RDS and EC2
   - Set up AWS Backup to automatically back up RDS instances and EC2 volumes. Test the restore process by restoring a backup.

 17. AWS Transit Gateway
   - Set up a Transit Gateway to connect multiple VPCs across different regions. Test connectivity between instances in different VPCs.

 18. AWS Security Hub
   - Set up AWS Security Hub to aggregate and prioritize security findings from multiple AWS services. Investigate and remediate findings.


# Advanced

 1. Building a Multi-Region Disaster Recovery Solution
   - Design and implement a multi-region disaster recovery (DR) solution using AWS services like Route 53 for DNS failover, RDS cross-region replication, and S3 cross-region replication.
   - Test failover scenarios and ensure minimal downtime.

 2. Implementing a Multi-Tier Architecture with Auto Scaling
   - Set up a multi-tier architecture with a web tier, application tier, and database tier.
   - Configure Auto Scaling Groups for the web and application tiers to handle traffic spikes.
   - Use Elastic Load Balancing (ELB) to distribute traffic across instances.

 3. Migrating a Legacy Application to AWS
   - Migrate a legacy on-premises application to AWS using the Application Migration Service.
   - Re-architect the application to take advantage of cloud-native services like RDS, Lambda, and API Gateway.

 4. Designing a Secure VPC with Private and Public Subnets
   - Create a VPC with private and public subnets across multiple Availability Zones.
   - Implement security groups and network ACLs to control traffic flow.
   - Deploy a NAT Gateway for instances in private subnets to access the internet securely.

 5. Automating Infrastructure with Terraform
   - Use Terraform to define and provision AWS infrastructure, including VPCs, EC2 instances, RDS databases, and IAM roles.
   - Implement state management and use modules for reusable code.

 6. Deploying a Serverless Application Using AWS Lambda
   - Develop a serverless application using AWS Lambda, API Gateway, DynamoDB, and S3.
   - Implement error handling, monitoring, and logging using CloudWatch and X-Ray.

 7. Implementing a CI/CD Pipeline with AWS CodePipeline
   - Set up a complete CI/CD pipeline using CodePipeline, CodeBuild, and CodeDeploy.
   - Integrate with GitHub for source control and deploy a sample application to EC2 instances or Lambda.

 8. Configuring AWS SSO for Multi-Account Access
   - Implement AWS Single Sign-On (SSO) to manage access across multiple AWS accounts.
   - Define permission sets and assign them to user groups.

 9. Creating a Centralized Logging Solution with ELK Stack
   - Deploy an ElasticSearch, Logstash, and Kibana (ELK) stack on AWS to collect and analyze logs from multiple sources.
   - Implement log ingestion from CloudWatch Logs, S3, and EC2 instances.

 10. Designing and Implementing a Data Lake on AWS
   - Create a data lake using S3, Glue, and Athena.
   - Set up data ingestion pipelines with Kinesis or Data Pipeline and configure data transformation with Glue jobs.

 11. Securing Sensitive Data with AWS KMS and IAM
   - Implement data encryption using AWS Key Management Service (KMS) for S3, EBS, and RDS.
   - Use IAM policies to control access to encryption keys and resources.

 12. Configuring AWS WAF and Shield for DDoS Protection
   - Deploy AWS WAF to protect a web application from common attacks like SQL injection and XSS.
   - Enable AWS Shield for advanced DDoS protection.

 13. Setting Up a Multi-Account AWS Organization
   - Create an AWS Organization and set up service control policies (SCPs) to manage access across multiple accounts.
   - Implement consolidated billing and shared services across the organization.

 14. Implementing Real-Time Data Streaming with Kinesis
   - Set up a real-time data streaming pipeline using Kinesis Data Streams, Firehose, and Analytics.
   - Process and analyze streaming data with Lambda and S3.

 15. Optimizing Costs with AWS Cost Explorer and Budgets
   - Use AWS Cost Explorer to analyze spending patterns and identify cost-saving opportunities.
   - Set up AWS Budgets to monitor costs and send alerts when spending exceeds predefined thresholds.

 16. Automating Backup and Disaster Recovery for RDS
   - Implement automated backups and snapshots for RDS instances.
   - Set up cross-region read replicas for disaster recovery.

 17. Deploying a Kubernetes Cluster on EKS
   - Set up an Amazon EKS cluster and deploy a containerized application.
   - Configure autoscaling for the Kubernetes cluster using Cluster Autoscaler and Horizontal Pod Autoscaler (HPA).

 18. Building a Highly Available WordPress Site
   - Deploy a WordPress site using EC2, RDS, and S3.
   - Implement high availability with ELB, Auto Scaling, and multi-AZ RDS.

 19. Setting Up a VPN Connection to an On-Premises Data Center
   - Configure a site-to-site VPN connection between an on-premises data center and AWS.
   - Implement routing and security rules to ensure secure communication.

 20. Creating a Hybrid Cloud Environment with AWS Direct Connect
   - Set up AWS Direct Connect to establish a dedicated network connection between your on-premises data center and AWS.
   - Configure a hybrid environment that uses both on-premises and cloud resources.

 21. Implementing AWS S3 Lifecycle Policies for Data Management
   - Create and apply lifecycle policies for S3 buckets to transition data between storage classes and automatically delete old data.
   - Implement cross-region replication for S3 buckets.

 22. Deploying an Elastic Beanstalk Application with Blue/Green Deployment
   - Deploy a web application using AWS Elastic Beanstalk.
   - Implement blue/green deployments to minimize downtime during updates.

 23. Monitoring and Logging with CloudWatch and CloudTrail
   - Set up CloudWatch metrics, alarms, and dashboards for EC2, RDS, and other AWS resources.
   - Enable CloudTrail for auditing API calls and track changes to your AWS environment.

 24. Building a Scalable Microservices Architecture
   - Design and deploy a microservices architecture using ECS or EKS, API Gateway, and Lambda.
   - Implement inter-service communication and scaling strategies.

 25. Creating a VPC Peering Connection Between Two VPCs
   - Set up VPC peering between two VPCs in the same or different AWS accounts.
   - Implement proper routing and security group settings to allow communication between resources in the peered VPCs.
