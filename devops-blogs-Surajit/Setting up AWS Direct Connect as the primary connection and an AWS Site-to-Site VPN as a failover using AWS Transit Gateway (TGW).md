Setting up AWS Direct Connect as the primary connection and an AWS Site-to-Site VPN as a failover using **AWS Transit Gateway (TGW)** is a more scalable solution for connecting multiple VPCs and on-premises environments. The Transit Gateway acts as a centralized router, simplifying network management across your infrastructure.

Here’s the step-by-step guide to setting up AWS Direct Connect with AWS Transit Gateway as the primary connection, and AWS Site-to-Site VPN as the failover.

### **Step-by-Step Guide: AWS Direct Connect + AWS Transit Gateway with VPN Failover**

#### **Prerequisites**
- AWS Account
- Access to AWS Management Console
- On-premises router that supports BGP for dynamic routing
- An AWS Direct Connect connection (either in place or ready to be ordered)
- VPN-compatible device on your on-premises network

### **1. Set up AWS Transit Gateway (TGW)**

#### **1.1. Create a Transit Gateway**
1. Go to **VPC Dashboard** > **Transit Gateways**.
2. Click on **Create Transit Gateway**.
3. Configure the following:
   - **Name**: Give the TGW a recognizable name.
   - **ASN**: Provide an ASN for the TGW (you can use the default 64512 or specify your own).
   - **Enable DNS support**, **ECMP**, and **VPN ECMP support** if needed.
4. Click **Create**.

#### **1.2. Attach VPCs to the Transit Gateway**
1. Go to **Transit Gateway Attachments** > **Create Attachments**.
2. Select your **Transit Gateway** and the **VPC** you want to attach.
3. Choose the **subnets** that will route traffic through TGW.
4. Click **Create attachment**.

   *Repeat this step for every VPC that will use the Transit Gateway for routing.*

### **2. Set up AWS Direct Connect (Primary)**

#### **2.1. Create Direct Connect connection**
1. Go to **Direct Connect Console** and click **Create a connection**.
2. Select an **AWS Direct Connect location** and specify the **port speed** (1 Gbps, 10 Gbps, etc.).
3. Once the connection is provisioned, you'll receive the **LOA-CFA** (Letter of Authorization and Connecting Facility Assignment) to give to your colocation provider.
4. Set up physical connectivity with the Direct Connect location.

#### **2.2. Set up a Direct Connect Gateway**
1. Go to the **Direct Connect Console** > **Direct Connect Gateways**.
2. Click **Create Direct Connect Gateway**, and give it a name.
3. Specify an **ASN** for your Direct Connect Gateway (use the same ASN as your TGW or configure routing as needed).
4. Click **Create Direct Connect Gateway**.

#### **2.3. Associate Direct Connect Gateway with Transit Gateway**
1. In the **Direct Connect Console**, click **Virtual Interfaces** > **Create Virtual Interface**.
2. Create a **Private Virtual Interface (VIF)**.
3. Select your **Direct Connect Gateway** as the target.
4. Provide the **BGP ASN** and VLAN information, then click **Create**.
5. Once the virtual interface is ready, associate the Direct Connect Gateway with your **Transit Gateway**:
   - Go to **Direct Connect Gateway** > **Actions** > **Associate Transit Gateway**.
   - Select the **Transit Gateway** created earlier.

#### **2.4. Configure BGP on your on-premises router**
1. Set up your on-premises router to use **BGP** to peer with the Direct Connect Gateway.
2. Establish a BGP session using the AWS-provided **ASN, IP ranges**, and **BGP attributes**.

### **3. Set up AWS Site-to-Site VPN (Failover)**

#### **3.1. Create a Virtual Private Gateway (VGW)** if not already done
1. Go to **VPC Dashboard** > **Virtual Private Gateways**.
2. Click **Create Virtual Private Gateway**.
3. Provide a **name** and **ASN** for the VGW, then click **Create**.
4. Attach the VGW to the appropriate VPCs.

#### **3.2. Set up Customer Gateway (CGW)**
1. Go to **VPC Dashboard** > **Customer Gateways**.
2. Click **Create Customer Gateway**.
3. Enter the **public IP** of your on-premises router.
4. Specify the **BGP ASN** of your on-premises network, then click **Create**.

#### **3.3. Create a Site-to-Site VPN connection**
1. Go to **VPC Dashboard** > **Site-to-Site VPN Connections**.
2. Click **Create VPN Connection**.
3. Select the **Transit Gateway** as the target, and choose the **Customer Gateway** you created.
4. Choose **Dynamic (BGP)** routing for automatic failover.
5. AWS will provide you with two VPN tunnel configurations, which you will use to configure your on-premises router.

#### **3.4. Configure your on-premises router**
1. Set up both VPN tunnels on your router using the configuration details provided by AWS.
2. Establish BGP sessions for each tunnel.
3. Configure BGP to prefer **Direct Connect** over the VPN (via **BGP weight** or **local preference**).

### **4. Configure Routing with Transit Gateway**

#### **4.1. Set up route tables for the Transit Gateway**
1. Go to **Transit Gateway** > **Route Tables** > **Create Route Table**.
2. Create a route table for your VPCs, and configure routes:
   - **Destination**: On-premises CIDR block.
   - **Target**: Direct Connect Gateway for Direct Connect traffic.
3. Create another route with the same destination but with a **Transit Gateway attachment to VPN** for failover.
4. Ensure that **Direct Connect** is the preferred route by setting **lower BGP metrics** or manipulating **route priorities**.

### **5. Test Failover Configuration**

#### **5.1. Simulate Direct Connect failure**
1. Disable the Direct Connect connection from your on-premises router.
2. Monitor whether the AWS Site-to-Site VPN takes over automatically.

#### **5.2. Verify traffic flow**
1. Use tools like `ping` or `traceroute` to check if traffic is routed via the VPN when Direct Connect is down.
2. Re-enable Direct Connect and ensure that traffic shifts back automatically to the Direct Connect path.

### **6. Monitor the Connections**

#### **6.1. CloudWatch Alarms**
- Set up **CloudWatch Alarms** to monitor **BGP sessions**, **Direct Connect status**, and **VPN tunnels**.
- Create notifications to alert you when failover occurs or when connections go down.

#### **6.2. Transit Gateway Route Monitoring**
- Use **Transit Gateway Route Tables** to view and monitor which paths traffic is using.
- Ensure that the Direct Connect path remains preferred when both Direct Connect and VPN are available.

By using **AWS Transit Gateway**, you centralize all routing between your on-premises environment, Direct Connect, and VPN failover paths. This setup ensures high availability and resilience by automatically switching traffic to the VPN when Direct Connect is unavailable.
