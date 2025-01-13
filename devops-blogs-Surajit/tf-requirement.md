I. Requirement - 
The requirement is that any laptop within clients internal network will be able to access a link/url that allows them to interact with the service hosted on this AWS instance.

II. Below tests done and still the requirement is not achieved - 
  - for testing purposes, I've set up a port so that anyone can send and receive curl commands to it, but I can't even send/recieve curl commands from the server. 
  - I've tried modifiying the inbound rules so at least my laptop's IP address should be allowed but even that hasn't worked.
  
III. My Questions 
Q1. Need to understand the exact issue?
Q2. Need to understand from which all places its working and from which all places the setup is not working?
Q3. 

IV. We need to troubleshoot on below points - 
1. Check the SG...inbound as well as outbound rule.
2. Check the NACLs
3. Check the Instance's Public or Private IP...
3. Check if the app is listening to the mentioned port or not.... netstat -tuln | grep <port-number>
4. Test CURL locally and externally(from laptop). curl <instance-public-ip>:<port>
5. Check app logs and c if the request from laptop is coming insde or not.

V. Solution -
