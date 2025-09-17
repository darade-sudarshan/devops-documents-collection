## Your App Works with ClusterIP but Fails with Ingress – How Do You Troubleshoot It?

### Question  
You’re able to access your app using its ClusterIP service internally, but it fails when accessed via Ingress. How do you troubleshoot the issue?

### Short explanation of the question  
This scenario tests your practical knowledge of Kubernetes networking, particularly around Ingress controllers and how Ingress routing works.

---

### Answer  
I would check if the Ingress controller is installed and running, verify the ingress rules, confirm DNS or host header matches, and review logs and service connectivity. Most often, the issue lies in incorrect rules, missing annotations, or DNS misconfiguration.

---

### Detailed explanation of the answer for readers’ understanding

---

### 🔍 Step-by-Step Troubleshooting Process

---

#### ✅ 1. **Check if Ingress Controller is Installed and Running**

Ingress resources only work if there’s a controller (e.g., NGINX, Traefik, AWS ALB Controller) running in the cluster.

```bash
kubectl get pods -n ingress-nginx
```

Make sure it’s in a `Running` state.

---

#### ✅ 2. **Check the Ingress Resource Definition**

```bash
kubectl describe ingress <ingress-name>
```

- Are the rules defined correctly?
- Are you using correct **`host`** or **`path`**?
- Does the `serviceName` and `port` match your ClusterIP service?

---

#### ✅ 3. **Check Annotations and Class**

Ensure the Ingress has the correct controller class:

```yaml
metadata:
  annotations:
    kubernetes.io/ingress.class: nginx
```

Or for newer versions:

```yaml
spec:
  ingressClassName: nginx
```

---

#### ✅ 4. **Check DNS or Host Header Configuration**

If you're using a host-based rule like `app.example.com`, make sure:

- DNS points to the ingress controller’s external IP.
- Or you’ve added a line in `/etc/hosts`:

```bash
<ingress-external-ip>  app.example.com
```

If you hit the IP directly but the app uses host-based routing, it may return `404`.

---

#### ✅ 5. **Check Logs of the Ingress Controller**

```bash
kubectl logs -n ingress-nginx <controller-pod-name>
```

Common errors include:

- `default backend - 404`
- `no matching path rule`
- TLS errors

---

#### ✅ 6. **Check Backend Service and Pod Health**

Sometimes, the Ingress forwards correctly, but the backend service is broken:

```bash
kubectl get endpoints <service-name>
```

Ensure there are endpoints (pods) behind the service.

---

#### ✅ 7. **Check TLS/HTTPS Configuration**

If using HTTPS, verify:

- TLS secret is valid.
- Rules include `tls` section.
- Ingress controller supports HTTPS.

---

### 🧪 Real-World Example

> “Our app worked internally via ClusterIP but gave a 404 over Ingress. It turned out we had a missing `ingressClassName` field, so the resource wasn’t being picked up by the NGINX controller at all.”

---

### 🔄 Summary Table

| Check                           | Description                                        |
|----------------------------------|----------------------------------------------------|
| Ingress Controller Running       | Must be deployed for Ingress to work              |
| Ingress Rules & Paths            | Must match service correctly                      |
| Hostname or Path Match           | Ensure DNS or `/etc/hosts` is correctly configured|
| Logs of Ingress Controller       | Debug routing errors                              |
| Backend Service & Endpoints      | Ensure pods are reachable                         |

---

### Key takeaway  

> If your app works via ClusterIP but not Ingress, the issue is often with the **Ingress configuration**, missing annotations, DNS setup, or **controller not handling the resource**.
