# ALB vs NLB

### 1. Layer in OSI Model
   - ALB (Application Load Balancer): Operates at Layer 7 (Application Layer).
     - Use Case: Ideal for load balancing HTTP/HTTPS traffic, where content-based routing is required (e.g., routing based on URL path, host header).
	 
   - NLB (Network Load Balancer): Operates at Layer 4 (Transport Layer).
     - Use Case: Ideal for handling low-latency, high-throughput TCP/UDP traffic, providing fast and stable connections.

### 2. Protocol Support
   - ALB:
     - Supports HTTP and HTTPS protocols.
     - WebSocket and HTTP/2 supported.
	 
   - NLB:
     - Supports TCP, UDP, TLS (Layer 4 protocols).
     - TLS termination supported for offloading SSL/TLS processing.

### 3. Routing & Target Types
   - ALB:
     - Supports host-based and path-based routing (route traffic based on URL path or host header).
     - Supports target groups based on IP addresses, EC2 instances, Lambda functions, and containers in ECS/EKS.
     - Can route traffic to multiple services running on the same EC2 instance using different paths.
	 
   - NLB:
     - Routes traffic to targets based on IP addresses or EC2 instances.
     - Does not support host-based or path-based routing, as it is not application-aware.
     - Provides static IPs for the load balancer, making it easier to set up DNS records for highly available services.

### 4. Performance
   - ALB:
     - Slightly slower compared to NLB due to the added Layer 7 processing (e.g., inspecting requests, routing based on application-level data).
     - Suitable for applications requiring advanced request handling.
   - NLB:
     - Optimized for ultra-low latency and high-throughput workloads.
     - Suitable for applications requiring extremely fast connections, such as gaming, real-time streaming, or financial applications.

### 5. Health Checks
   - ALB:
     - Supports HTTP/HTTPS health checks.
     - Provides deeper health checking capabilities by inspecting HTTP status codes (e.g., 200 OK).
   - NLB:
     - Supports TCP/UDP health checks.
     - Can only determine the health of a target by checking whether the TCP connection is open (for TCP-based health checks).

### 6. SSL/TLS Termination
   - ALB:
     - Supports SSL termination at the load balancer level, allowing HTTPS traffic to be decrypted at the ALB.
   - NLB:
     - Supports TLS termination, but typically used to pass-through encrypted traffic directly to the backend targets.

### 7. Scaling
   - ALB:
     - Scales based on request rate (number of new HTTP/HTTPS requests per second).
     - Automatically scales based on traffic patterns, and it is elastic.
   - NLB:
     - Scales based on connection rate (number of new TCP/UDP connections per second).
     - Can handle millions of requests per second and is optimized for handling volatile traffic patterns.

### 8. Pricing
   - ALB:
     - Charged based on the number of LCUs (Load Balancer Capacity Units), which are determined by new connections, active connections, and processed bytes.
   - NLB:
     - Pricing is based on the number of new connections, active connections, and data processed, but it also includes a static hourly charge, making it slightly more expensive if not fully utilized.
     - Typically less costly when handling a large volume of traffic with minimal routing logic.

### 9. IP Addressing
   - ALB:
     - Does not provide a static IP, but you can assign an Elastic IP through an AWS Global Accelerator.
     - DNS-based load balancing using AWS Route 53.
   - NLB:
     - Provides a static IP address per availability zone, making it easier to register DNS entries and simplifying configuration with firewalls.
     - Suitable for applications needing predictable IP addresses.

### 10. Sticky Sessions (Session Persistence)
   - ALB:
     - Supports sticky sessions using application-level cookies.
     - Commonly used for maintaining user sessions in web applications.
   - NLB:
     - Supports sticky sessions based on source IP.
     - Ensures that traffic from the same client IP is routed to the same target for the duration of the session.

### 11. Use Cases
   - ALB:
     - Web applications that require advanced request routing (e.g., microservices, container-based architectures).
     - APIs that need routing based on HTTP headers or path parameters.
     - Scenarios where detailed monitoring of HTTP-level traffic is required.
   - NLB:
     - Real-time applications that require high-throughput and low-latency (e.g., gaming, video streaming).
     - TCP/UDP-based services like databases, load balancing TCP traffic for RDS or in-memory databases (e.g., Redis).
     - Use cases needing static IP addresses (e.g., IP whitelisting by external services).

---

### Key Differences

| Feature                  | ALB (Application Load Balancer)        | NLB (Network Load Balancer)          |
|--------------------------|----------------------------------------|--------------------------------------|
| OSI Layer             | Layer 7 (Application Layer)            | Layer 4 (Transport Layer)            |
| Protocols Supported   | HTTP, HTTPS, WebSocket, HTTP/2         | TCP, UDP, TLS                       |
| Routing Type          | Path/Host-based, Header routing        | No routing, forwards traffic         |
| Performance           | Slower, application-aware              | Ultra-low latency, high throughput   |
| Health Checks         | HTTP/HTTPS-based                       | TCP/UDP-based                       |
| SSL/TLS Termination   | SSL Termination supported              | TLS termination & pass-through      |
| Scaling               | Request rate-based                     | Connection rate-based               |
| Pricing               | LCU-based                              | Connection-based + hourly charge    |
| IP Address            | DNS-based (Elastic IP via Global Accelerator) | Static IP provided           |
| Use Case              | Web apps, APIs, microservices          | High-throughput, real-time apps     |

---

### Summary
- Use ALB when you need advanced routing (e.g., microservices, APIs, content-based routing) or are dealing with web traffic (HTTP/HTTPS).
- Use NLB for performance-critical applications, real-time systems, or services that require low latency, high throughput, and static IP addresses (e.g., TCP/UDP services, databases).

