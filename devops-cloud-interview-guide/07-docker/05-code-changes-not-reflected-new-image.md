## You made change in your code, rebuilt the image, but the change isn't reflected?

### Question  
You made a change in your application code, rebuilt the Docker image, but the container still shows old behavior. What could be the issue?

### Short explanation of the question  
This scenario tests your understanding of Docker image layers, caching behavior during `docker build`, and volume mounting in development setups.

### Answer  
This usually happens due to either build caching or the container using a volume that overrides the updated code. I’d verify that the image was rebuilt correctly and ensure no volume is masking the changes.

### Detailed explanation of the answer for readers’ understanding

There are two common culprits for this issue:

---

### 🧱 1. **Docker build cache**

Docker caches image layers to speed up builds. If no changes are detected in a layer’s context, it reuses the cached layer. This can skip the step that copies new code into the image.

#### ✅ Fix

Use the `--no-cache` flag while building:

```bash
docker build --no-cache -t myapp:latest .
```

Also ensure that `COPY` instructions are placed **after** dependencies to avoid skipping due to unchanged upper layers.

```Dockerfile
# BAD: Code copied early, everything cached
COPY . .

# GOOD: Dependencies first, then app code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

---

### 📦 2. **Volume overwriting image content**

When you run a container with a volume mounted to a directory like `/app`, it **overrides** whatever was built into the image at that path.

```bash
docker run -v "$(pwd)":/app myapp
```

If you rebuild the image with updated code, but still mount your old source directory, the container sees your **local files**, not what's in the image.

#### ✅ Fix

- Either remove the volume mount
- Or update your local files too

---

### 🔍 Steps to verify

- Run a shell inside the image and check the file contents:
  ```bash
  docker run -it myapp:latest cat /app/main.py
  ```

- Check the list of running containers:
  ```bash
  docker ps
  ```

- Make sure you’re running the updated image:
  ```bash
  docker images | grep myapp
  ```

---

### 🧠 Real-world Insight

> “I once rebuilt a Node.js app image after updating source code. But due to a `-v "$(pwd)":/app` bind mount, it kept running the old code from my host system, not from the newly built image. Took me a while to realize the mount was masking the update.”

---

### Key takeaway

> "If Docker changes aren’t reflected, check for caching in `docker build` and make sure no local volumes are masking your image content."
