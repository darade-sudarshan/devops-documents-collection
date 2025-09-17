## How can you restrict access to a DB pod to only one app in the same namespace?

### Question  
Explain how you would restrict traffic so that only a specific application (pod) can connect to a database pod within the same namespace.

### Short explanation of the question  
This checks your knowledge of Kubernetes **NetworkPolicies** (and optionally RBAC/ServiceAccounts) to enforce fine-grained, pod-level network security, even when resources share a namespace.

### Answer  
Create a **NetworkPolicy** that (1) selects the database pods and (2) allows **ingress** traffic only from pods with a specific label identifying the permitted app. All other traffic is denied by default once the policy is in place.

### Detailed explanation of the answer for readers’ understanding  

Kubernetes networking is open by default; any pod can talk to any other pod. NetworkPolicies let you **whitelist** traffic based on pod labels, namespaces, ports, and protocols.

---

#### 🛠 Step-by-step

1. **Label your pods**  
   ```bash
   kubectl label pods db-0 role=db
   kubectl label pods app-0 role=api
   ```
   - `role=db` for the database pod(s)  
   - `role=api` for the app allowed to connect

2. **Create a NetworkPolicy** (YAML below).  
   - **podSelector** matches the DB pods.  
   - **ingress** allows traffic **only** from pods with `role=api` on port 5432.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-app-to-db
  namespace: my-namespace
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: api
    ports:
    - protocol: TCP
      port: 5432
```

3. **Verify**  
   - `app-0` ➜ `db-0` on port 5432 ✅  
   - Any other pod ➜ `db-0` ❌ (connection refused / timed out)

---

#### 🔍 Why this works

| Component     | Purpose                                |
|---------------|----------------------------------------|
| `podSelector` | Targets the DB pods (`role=db`).       |
| `from`        | Whitelists only pods with `role=api`.  |
| `ports`       | Optional; further restricts to 5432.   |
| Default deny  | Once a policy exists, all other ingress traffic to the selected pods is blocked unless explicitly allowed. |

---

#### 🧠 Real-world Insight

> “We secured a PostgreSQL StatefulSet by labelling it `role=db` and applying an ingress NetworkPolicy. Only the `payments` deployment (labelled `role=payments-api`) could connect. QA pods in the same namespace no longer had DB access unless explicitly whitelisted.”

---

### Key takeaway  

> "Use a NetworkPolicy to _select_ the database pods and _allow_ ingress only from the intended app’s label. This whitelists traffic inside the namespace and blocks everything else by default."
