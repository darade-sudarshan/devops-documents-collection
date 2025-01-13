# Below is the Jenkins Console Walkthrough for better understanding each feature.


### I. Login Screen
In this page we need to entire credentials and login to the Jenkins dashboard. Default Jenkins port is 8080. 

Learning: As we are aware on restart of EC2, the public IP changes, so our Jenkins URL also changes. Thus, the Jenkins becomes slow. To resolve this issue we need to replace the old public ip with the new one in 'System Configuration > System'.

<img width="896" alt="image" src="https://github.com/user-attachments/assets/056d3ba3-f40c-4c1d-8c43-53046253313d">

### II. Home Page

When we login we are redirected to the dashboard of the Jenkins. Here we see below stuffs - 
1. In Top Panel where we see which user is logged in(username)
2. In Left Panel we see a) 'New Item' link for creating new pipeline. b) 'Manage Jenkins' Link to do admin related changes.
3. In Center page, we see a) 'Start building your software project' notes we can start creating our pipeline from there as well. b) 'Set up a distributed build', from here we can add nodes for managing traffic among multiple instances.

<img width="944" alt="image" src="https://github.com/user-attachments/assets/184784f7-a009-4d63-97b5-34daae6ffe27">

### III. Adding Node

1. From the dashboard's center page, inside 'Set up a distributed build', we click on 'setup a agent'.
<img width="867" alt="image" src="https://github.com/user-attachments/assets/450f8587-90c5-4d35-9aaa-b3e2ba5a5408">

2. Next we will get the below page where we can give our Node name & type as 'permanent agent' and click on CREATE.
<img width="587" alt="image" src="https://github.com/user-attachments/assets/07d2335c-4e4d-4cf1-a6d2-b7fe0461f6f7">

3. Finally we will be redirected to a form where we need to fill few details and some of the important details are 'Number of executors', 'Remote root directory', 'Labels', 'Usage', 'Launch method', 'Availability', etc. Fill them and click on SAVE.
<img width="1500" alt="image" src="https://github.com/user-attachments/assets/1f3ee0e4-c200-4594-b730-d2c94f24b1c2">

Note: In the Launch Method, if we use Launch via SSH, we need to give the node host and add the credentials and refer here. To add credentials, watch section V.

4. Check if the added node is visible and live or not.
If the node is available it should NOT have cross(X) in the 1st column of the Nodes.

<img width="955" alt="image" src="https://github.com/user-attachments/assets/dfb221ad-7e16-4f32-872f-cf853d8d65e4">

### IV. Navigating 'Manage Jenkins'

As shown below, 'Manage Jenkins' contains 5 sub catagories - 

1. System Configuration - As the name suggests all the system related configurations are done from this section.

   a) Systems - Here we can do all the global settings for our builds related to the Jenkins Node.
   
   b) Tools - Here we can do the configuration regarding installed utilities and plugins.

   c) Plugins - We can download the required plugins from this section.

   d) Nodes - We can add nodes as we seen in section-II.

   e) Cloud - We congiure cloud instances to provision agents on-demand. 

   f) Appearance - We can change the colour of the Jenkins console.

   <img width="692" alt="image" src="https://github.com/user-attachments/assets/7162ea23-c26f-45ee-902d-822ea12c498c">

2. Security -

      a) Security - It secures Jenkins; defines who is allowed to access what.
 
      b) Credentials - In this section, we configure credentials of all the resources which we need to integrate with Jenkins.    

      c) Credentials Providers - Configures the credential provider and type.

      d) Users - Used to create, Delete and Manage users.

   <img width="698" alt="image" src="https://github.com/user-attachments/assets/2200deb4-f9d1-4a25-b836-ce50a979b92e">

3. Status Information -

      a) System Information - 

      b) System Logs - All Jenkins logs are recorded here.

      c) Load Statistics - It shows us the stats of how resources are utilized. 4 Parameters measured resources are - i) Number of online executors, ii) Number of busy executors, iii) Number of available executors, iv) Queue length.

      d) About Jenkins -

   <img width="688" alt="image" src="https://github.com/user-attachments/assets/27261f7d-8840-4651-ac57-263ef06b259f">

4. Troubleshooting - 

      a) Manage Old Data

   <img width="355" alt="image" src="https://github.com/user-attachments/assets/0bd8d582-6c11-4356-a2a0-44c8cfd21cc6">

5. Tools and Actions -

      a) Reload Configuration from Disk - Discard all the loaded data in memory and reload everything from file system. Useful when you modified config files directly on disk.

      b) Jenkins CLI - You can access various features in Jenkins through a command-line tool. Refer: https://www.jenkins.io/doc/book/managing/cli/

      c) Script Console - Executes arbitary scripts for admin/troubleshooting/diagnostics purpose. Type in an arbitrary (in Groovy script) and execute it on the server. Use the ‘println’ command to see the output (if you use System.out, it will go to the server’s stdout, which is harder to see).

   Example: println(Jenkins.instance.pluginManager.plugins)

      d) Prepare for Shutdown - To shutdown Jenkins.

<img width="692" alt="image" src="https://github.com/user-attachments/assets/fb1e39f6-352f-4641-a3dc-eb2b8a91df56">



