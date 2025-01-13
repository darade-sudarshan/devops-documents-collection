Here’s a complex Kubernetes manifest file with multiple components: Deployment, Service, ConfigMap, Secret, HorizontalPodAutoscaler, PersistentVolumeClaim (PVC), and Ingress. Each section is explained in detail to help understand the purpose of the manifest components.

### Sample Kubernetes Manifest File

```yaml
---
# 1. ConfigMap: Stores non-sensitive configuration data
apiVersion: v1
kind: ConfigMap
metadata:
  name: myapp-config
  namespace: default
data:
  APP_ENV: "production"
  APP_PORT: "3000"
  DATABASE_URL: "postgres://db_user:db_password@db_host:5432/mydb"

---
# 2. Secret: Stores sensitive information like passwords
apiVersion: v1
kind: Secret
metadata:
  name: myapp-secret
  namespace: default
type: Opaque
data:
  POSTGRES_USER: dXNlcg==           # Base64 encoded "user"
  POSTGRES_PASSWORD: c2VjdXJlcGFzcw== # Base64 encoded "securepass"

---
# 3. PersistentVolumeClaim (PVC): Requests storage for a Pod
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myapp-pvc
  namespace: default
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi

---
# 4. Deployment: Manages the application Pods
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
  namespace: default
  labels:
    app: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 2
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: myapp-container
          image: myapp:latest
          ports:
            - containerPort: 3000
          envFrom:
            - configMapRef:
                name: myapp-config
            - secretRef:
                name: myapp-secret
          volumeMounts:
            - name: myapp-storage
              mountPath: /app/data
          livenessProbe:
            httpGet:
              path: /healthz
              port: 3000
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /ready
              port: 3000
            initialDelaySeconds: 10
            periodSeconds: 5
      volumes:
        - name: myapp-storage
          persistentVolumeClaim:
            claimName: myapp-pvc

---
# 5. Service: Exposes the application to external traffic
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
  namespace: default
spec:
  selector:
    app: myapp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
  type: ClusterIP

---
# 6. Ingress: Manages external HTTP/S traffic to the service
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
  namespace: default
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: myapp-service
                port:
                  number: 80

---
# 7. Horizontal Pod Autoscaler (HPA): Automatically scales the application
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp-hpa
  namespace: default
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Detailed Explanation of Each Component

---

#### 1. **ConfigMap**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: myapp-config
  namespace: default
data:
  APP_ENV: "production"
  APP_PORT: "3000"
  DATABASE_URL: "postgres://db_user:db_password@db_host:5432/mydb"
```
- **Purpose**: Stores non-sensitive configuration data in key-value pairs.
- **`data`**: Defines the configuration data. These values are referenced by the application running in Pods.
- In this example, we are storing environment variables like `APP_ENV`, `APP_PORT`, and `DATABASE_URL`.

---

#### 2. **Secret**
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: myapp-secret
  namespace: default
type: Opaque
data:
  POSTGRES_USER: dXNlcg==           # Base64 encoded "user"
  POSTGRES_PASSWORD: c2VjdXJlcGFzcw== # Base64 encoded "securepass"
```
- **Purpose**: Stores sensitive information such as passwords or API keys. Unlike ConfigMaps, secrets are stored in Base64-encoded form.
- **`data`**: Stores the secret values in Base64 format. Here, `POSTGRES_USER` and `POSTGRES_PASSWORD` store the username and password for a database.

---

#### 3. **PersistentVolumeClaim (PVC)**
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myapp-pvc
  namespace: default
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```
- **Purpose**: Requests persistent storage for a Pod. It is used when your application needs to persist data beyond the lifecycle of a Pod.
- **`accessModes`**: Defines how the volume can be accessed. `ReadWriteOnce` means it can be read and written by a single node.
- **`resources.requests.storage`**: Specifies the amount of storage requested, in this case, 1Gi.

---

#### 4. **Deployment**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
  namespace: default
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 2
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: myapp-container
          image: myapp:latest
          ports:
            - containerPort: 3000
          envFrom:
            - configMapRef:
                name: myapp-config
            - secretRef:
                name: myapp-secret
          volumeMounts:
            - name: myapp-storage
              mountPath: /app/data
          livenessProbe:
            httpGet:
              path: /healthz
              port: 3000
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /ready
              port: 3000
            initialDelaySeconds: 10
            periodSeconds: 5
      volumes:
        - name: myapp-storage
          persistentVolumeClaim:
            claimName: myapp-pvc
```
- **Purpose**: Manages a set of replicated Pods running an application. Deployments handle scaling, updates, and rollbacks.
- **`replicas`**: Defines the number of Pods to run (3 in this case).
- **`strategy`**: Uses a rolling update strategy to gradually replace old Pods with new ones.
  - `maxUnavailable`: Ensures that only 1 Pod can be unavailable during an update.
  - `maxSurge`: Allows 2 additional Pods to be created during an update.
- **`envFrom`**: References environment variables from both ConfigMaps and Secrets.
- **`volumeMounts`**: Mounts a PVC as a volume inside the Pod at `/app/data`.
- **`livenessProbe`** and **`readinessProbe`**: These are health checks to ensure the Pod is running and ready to serve traffic.

---

#### 5. **Service**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
  namespace: default
spec:
  selector:
    app: myapp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
  type: ClusterIP
```
- **Purpose**: Exposes the application to the network inside the Kubernetes cluster.
- **`selector`**: Defines which Pods the service applies to by matching the `app: myapp` label.
- **`ports`**: Specifies that the service listens on port `80` and forwards traffic to the application's container on port `3000`.
- **`type`**: Defines the service type. `ClusterIP` is the default, meaning the service is only accessible from within the cluster.

---

#### 6. **Ingress**
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
 

 name: myapp-ingress
  namespace: default
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: myapp-service
                port:
                  number: 80
```
- **Purpose**: Manages external HTTP/S access to services. Ingress allows you to expose services to external traffic and define routing rules.
- **`annotations`**: Add custom settings for the Ingress controller, such as the rewrite rule for Nginx.
- **`rules`**: Defines how incoming requests should be routed based on the host and path. In this case, traffic to `myapp.example.com` is routed to `myapp-service` on port `80`.

---

#### 7. **Horizontal Pod Autoscaler (HPA)**
```yaml
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp-hpa
  namespace: default
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```
- **Purpose**: Automatically scales the number of Pods in a Deployment based on resource usage.
- **`scaleTargetRef`**: Defines the resource to be scaled. In this case, it’s scaling the `myapp-deployment`.
- **`minReplicas`** and **`maxReplicas`**: Specifies the minimum and maximum number of replicas (2 to 10 in this case).
- **`metrics`**: Defines the metric that triggers scaling. Here, the HPA scales based on CPU usage, ensuring that CPU utilization is kept around 70%.

### Summary of Key Components:
1. **ConfigMap**: Stores non-sensitive configuration data.
2. **Secret**: Stores sensitive data like passwords in Base64.
3. **PersistentVolumeClaim (PVC)**: Requests storage for Pods.
4. **Deployment**: Manages replicated Pods and their lifecycle.
5. **Service**: Exposes Pods to internal traffic within the cluster.
6. **Ingress**: Manages external HTTP/S traffic and routing to services.
7. **Horizontal Pod Autoscaler (HPA)**: Automatically scales the number of Pods based on resource usage (e.g., CPU).
