## How various components of Kubernetes interact when you run `kubectl apply` (Pod)

### Question  
What happens behind the scenes when you run `kubectl apply -f pod.yaml` to deploy a pod in Kubernetes?

### Short explanation of the question  
This question checks whether you understand the full control flow and the interaction between the Kubernetes components — from API request to pod scheduling and execution on a node.

---

### Answer  
When you run `kubectl apply -f pod.yaml`, the request is sent to the API server, which stores the desired state in etcd. The scheduler then selects a node for the pod, and the kubelet on that node pulls the image and starts the container using the container runtime.

---

### Detailed explanation of the answer for readers’ understanding

Let’s break it down step-by-step:

---

## 🧾 Step 1: `kubectl apply -f pod.yaml`

You define a Pod manifest like this:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp
spec:
  containers:
  - name: app
    image: nginx
```

You run:

```bash
kubectl apply -f pod.yaml
```

This sends a REST request to the Kubernetes API server.

---

## 🔐 Step 2: API Server receives and validates the request

- The `kube-apiserver` is the front-end of the control plane.
- It authenticates and validates the request.
- If valid, it stores the desired state of the Pod object in **etcd**, the cluster’s key-value store.

---

## 🧠 Step 3: Controllers monitor etcd state

- The **scheduler** constantly watches for unscheduled pods via the API server.
- It sees that your pod has no assigned node.

---

## ⚖️ Step 4: Scheduler picks a suitable node

- It considers available resources, taints, affinities, and other rules.
- It assigns the pod to a specific node by updating the pod spec with `nodeName`.

---

## 🔧 Step 5: kubelet on the selected node takes over

- The **kubelet** on that node:
  - Sees the updated pod spec.
  - Pulls the `nginx` image from the registry.
  - Uses the **container runtime** (like containerd) to start the container.

---

## 🔌 Step 6: kube-proxy handles networking

- **kube-proxy** sets up networking rules to route traffic to the pod if it's part of a Service.
- DNS resolution (via CoreDNS) also becomes available.

---

## ✅ Step 7: Pod is now running

You can check it using:

```bash
kubectl get pods
kubectl describe pod myapp
```

---

### 🔄 Summary of Interactions

| Component        | Role in the Flow |
|------------------|------------------|
| `kubectl`        | Sends request to API |
| `kube-apiserver` | Validates & stores the object |
| `etcd`           | Stores desired state |
| `kube-scheduler` | Chooses node for pod |
| `kubelet`        | Pulls image and starts container |
| `containerd`     | Runs the actual container |
| `kube-proxy`     | Sets up network rules |
| `CoreDNS`        | Resolves internal DNS |

---

### 🧠 Real-world Insight

> “We faced an issue where pods remained in `Pending` state. On investigating, we found that the scheduler couldn’t place the pod due to node taints. Understanding this internal flow helped us fix the issue quickly.”

---

### Key takeaway

> "Running `kubectl apply` kicks off a coordinated flow involving the API server, etcd, scheduler, kubelet, and container runtime — all working together to ensure your pod reaches its desired state."
