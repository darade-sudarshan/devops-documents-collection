## Deployment Strategies I've Used in the Past

### Question  
Explain the various deployment strategies you’ve used in your past roles. Why did you choose them, and what tools were involved?

### Short explanation of the question  
This helps the interviewer understand your experience with real-world release patterns, how you balance risk and velocity, and how you adapt based on the application’s nature and criticality.

---

### Answer  
In my experience, I’ve used multiple deployment strategies including **Rolling Updates**, **Blue-Green Deployments**, and **Canary Deployments**, based on the application's business impact, criticality, and maturity of observability tooling.

---

### Detailed explanation of the answer for readers’ understanding

---

### 1. 🔁 **Rolling Update** (Most Common)

#### What it is:
- Replaces old pods gradually with new ones.
- Ensures no downtime during the update.

#### Where I used it:
- For stateless microservices (e.g., product APIs, frontend apps).
- Deployed using Kubernetes native rolling updates.

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 1
    maxUnavailable: 1
```

#### Tools:  
- Kubernetes Deployments
- Argo CD
- GitHub Actions

#### Why:
- Simple to manage.
- Works well when monitoring is in place and rollback is quick (via GitOps).

---

### 2. 🟦🟩 **Blue-Green Deployment**

#### What it is:
- Deploy new version in parallel (green).
- Once validated, switch traffic from old (blue) to new.

#### Where I used it:
- For monolith applications with complex startup logic.
- Services that needed immediate rollback due to customer SLA.

#### Tools:
- AWS ALB + target groups
- Helm
- Jenkins pipelines

#### Why:
- Zero downtime.
- Quick rollback (just switch traffic back to blue).

---

### 3. 🧪 **Canary Deployment**

#### What it is:
- Gradually roll out the new version to a small % of users.
- Observe metrics before increasing traffic.

#### Where I used it:
- For payment services and high-risk business workflows.
- Used in combination with Prometheus-based health checks.

#### Tools:
- Argo Rollouts
- Flagger
- Prometheus + Grafana

#### Why:
- Safer than rolling update for mission-critical components.
- Helps catch errors before impacting all users.

---

