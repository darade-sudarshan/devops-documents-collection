1. RDS
-Managed RDBMS DB Service.
-Allows DB engines like;
	Postgres
	MySQL
	MariaDB
	Oracle
	MS SQL
	Aurora(AWS Owned DB)
-RDS vs EC2 server for DB
  Auto provisioning, OS Patching.
  Continuous backup and restore to specific timestamp(Point in Time Restore).
  Monitoring Dashboards.
  Read Replicas. 
  Multi AZ.
  Maintenance windows for upgrades.
  scaling capacity.
  storage backed by EBS.

-We cant SSH the RDS instance.

-Storage Auto scaling feature

-Read Replicas(15 read replicas allowed). Within same AZ, cross AZ or diff region.
-Async(not immediate) replication happens between the read replicas and RDS DB instance.
-Replicas can be promoted to own DB.
-explain with an example. reading analytical data.

-RDS Multi AZ(Sync replication)
-1 DNS name between primary and standby. auto app failover to standby.
-HA
-Only used for scaling.

Note - Create a DB client if u want.

-RDS Proxy.
  Why RDS Proxy is required?
  -Batch Example.(Lambda Function here).
  - Lambda function is executed outside your VPC so cannot access internal resources.
  -We will explicitly define a VPC and SG to the Lambda and it will create an ENI in the subnet and by this way the lambda function will have access to resources inside the VPC. Also, a AWSLambdaVPCAccessExecutionRole will be required.

  =RDS Proxy for Lambda
  -When using Lambda Functions with RDS, it will open and maintain DB connection and this will result in a "TooManyConnections" exception.
  -With RDS Proxy in between, Lambda functions will not go to DB instance directly instead they will go to rds proxy. RDS proxy has the capability to do conn cleanup.


=>RDS Parameters Groups

=> RDS Backup vs Snapshots
=> RDS Snapshots sharing
=> RDS Events and Event Subscriptions
=> RDS DB Logs
=> RDS CloudWatch logs
=> RDS Enhanced monitoring.
=> RDS Performance Insights.
	-By Waits => CPU, IO, locks, etc
	-By SQL stmts => sql stmts that creating issue.
	-By Hosts =>find the srv, that is using the most our DB
	-By Users =>find the usr, that is using the most our DB

2. Aurora
  -Engines
	MySQL
	Postgres

  -5x performance increment of aurora than RDS.
  -Storage automatically grows in increment of 10 GB upto 128TB.
  -15 Read replicas
  -failover in aurora is much faster than RDS.

  -Aurora High Availability and Read Scaling.
	6 copies of your data across 3 AZ


|	AZ1	| 	AZ2	|	AZ3	|
|		|		|		|
| [Write] [Read]|  [Read][Read]	|  [Read][Read]	|
|		|		|		|

  -If a master fails, Read Replicas have the capability to become master.
  -Aurora supports Cross Region Replication.
  -It has Writer Endpoint(connecting to the Master) and Reader Endpoint(Connecting to read replicas) to read and write data. the reader endpots are attached to load balancer and can dynamically scale as well.
  -Scaling can be done on CPU utilization or no. of connections.
  -Backups are automated and restoration in an single click restoration.
  -Aurora backtracking is a feature in Aurora which can rewind the DB cluster back and forth in time(upto 3days)


3. DynamoDB(Cloud owned DB)
  -Its No SQL DB.
  -Fully Managed.
  -Can handle Millions of requests per sec.
  -Can perform in single digit millisecond.

  -DynamoDB is made of table and not DBs. 
  -Each table will have primary key, items(rows) and attributes(columns).
  -Primary key consists of partition-key and sort-key.
  -unlike SQL DB, here columns(attributes) can be added over time and can be null.
  -Max Item size is 400kb.
  -Datatypes supported are - string, number, binary, Boolean, null, list,map, string set, number set, binary set, etc.

  -Read and Writes capacity
	1. Provisioned Mode
		-Used for predictive workloads.
		-we can specify the no. of reads and writes per sec.
		-we need to plan the capacity beforehand.
		-pay for provisioned RCU(Read Capacity Units) and WCU(Write Capacity Units).
		-We can include auto scaling to auto increase or decrease RCUs and WCUs.
	2. On-Demand Mode
		-Used for unpredictive workloads.
		-Payment to be done for no. of RCUs and WCUs done. Hence expensive.

  =DynamoDB Accelerator(DAX)
	-Fully-managed, HA and in-memory cache for dynamodb.
	-Helps solve read congestion by caching.
	-provides cached data with micro-seconds latency.
	-It has default 5 min TTL for cache and its editable.
	
  =DynamoDB Global Tables
	-Make a dynamodb tables accessible with low latency in multiple region.
	-Active-active replication.
	-Apps can read and write to the table in any region.

  =DynamoDB backups
	-Continous backups.
	-Ondemand backups.
