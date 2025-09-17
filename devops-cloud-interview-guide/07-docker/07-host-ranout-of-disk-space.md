## Docker host is running out of disk space. How do you clean up?

### Question  
Your Docker host is running out of disk space. What are the steps you'd take to clean up unused data and prevent this from happening again?

### Short explanation of the question  
This question checks your understanding of Docker’s local storage usage — including images, containers, volumes, and build cache — and how to manage them efficiently.

### Answer  
I would use Docker system prune commands to clean up unused containers, images, volumes, and networks. Then, I’d investigate large files under Docker’s storage directory and implement a cleanup policy going forward.

### Detailed explanation of the answer for readers’ understanding

Docker stores data in `/var/lib/docker` on Linux hosts. Over time, old images, stopped containers, and unused volumes accumulate and consume disk space.

---

### 🧹 Cleanup Steps

#### ✅ 1. **Prune unused Docker resources**

```bash
docker system df
```

Gives you an overview of space used.

```bash
docker system prune
```

This removes:

- Stopped containers
- Unused networks
- Dangling images (untagged)
- Build cache

For a deeper cleanup:

```bash
docker system prune -a --volumes
```

**Warning:** This deletes:
- All unused images (not just dangling ones)
- All unused volumes

---

#### 📦 2. **Remove unused volumes manually**

```bash
docker volume ls -f dangling=true
docker volume rm $(docker volume ls -qf dangling=true)
```

Or use `docker volume prune`.

---

#### 🧱 3. **Remove unused images selectively**

List large images:

```bash
docker images --format "{{.Repository}}:{{.Tag}}\t{{.Size}}"
```

Then remove by name:

```bash
docker rmi <image-id>
```

---

#### 🧊 4. **Investigate storage usage**

Use `du`:

```bash
sudo du -sh /var/lib/docker/*
```

This shows what’s taking up the most space.

---

### 🛡️ Preventive Actions

- Run a cron job to prune weekly:
  ```bash
  docker system prune -a --volumes -f
  ```

- Use smaller base images (`alpine`, `distroless`).
- Clean up intermediate build layers in Dockerfiles:
  ```Dockerfile
  RUN apt-get update && apt-get install -y something \
   && rm -rf /var/lib/apt/lists/*
  ```

---

### 🧠 Real-world Insight

> “One of our CI runners ran out of disk due to hundreds of dangling images and orphan volumes from builds. We added weekly `docker system prune` as a cron job and used multistage builds to reduce image size.”

---

### Key takeaway

> "Docker doesn't auto-clean. Regularly prune unused containers, images, and volumes to free disk space and avoid downtime."
