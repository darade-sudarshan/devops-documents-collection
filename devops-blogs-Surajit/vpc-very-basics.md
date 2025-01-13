### 1. Understanding CIDRs - It has 2 components
	i) Base IP - Represents the IP range(xx.xx.xx.xx). Ex: 10.21.2.101

	ii) Subnet Mask - Defines how many bits can change in the IP. Ex: /0, /16, /24, /32
		./8 - 255.0.0.0
		./16 - 255.255.0.0
		./24 - 255.255.255.0
		./32 - 255.255.255.255

### 2. DNS Resolution in VPC
i)DNS Resolution(enableDnsSupport)
  Decides if DNS resolution from Route-53 resolver server is supported for the VPC.
 If true, then it queries the Amazon Provider DNS server at 169.254.169.253 or the reserved IP at the base of the VPC IPV4 network range plus 2

ii)DNS Hostname(enableDnsHostname)
If true, it assigns public hostname to ec2 instance if it has IPv4.

### 3. NACLs
  - NACLs are stateless whereas Security Groups are stateful(Traffic that comes in can as mentioned in inbound rule that can go out even if outbound is not mentioned).
  -Ephemeral Ports(random ports): 
	- For any 2 endpoints to establish communication we should have IP and Ports at both the end. 
	- So, if my system is connecting to a webserver, my system will be source and webserver will be destination and in this case, port which I am 	connecting to the server is called ephemeral port.
	- Port Range: Win10: 49152-65535 Linux: 32768-60999
		___________						___________
		|My System| IP-1.2.3.4,Port-50010 ----------------->  	|Webserver| IP-10.11.12.14, Port-443
		-----------						-----------
		
### 4. VPC Reachability Analyzer
-A network diagnostics tool that troubleshoots network connectivity between 2 endpoints in your VPC(s).

-It builds a model of the network configuration, then checks the reachability based on these configurations(it doesn't send packets)
