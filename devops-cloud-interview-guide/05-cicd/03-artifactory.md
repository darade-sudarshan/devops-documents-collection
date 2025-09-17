## Question  
Which artifact repository do you use for builds?

### 📝 Short Explanation  
An artifact repository is a storage system where you can **publish**, **store**, and **retrieve** build artifacts like `.jar`, `.war`, Docker images, etc. It’s crucial in modern CI/CD pipelines for dependency management and versioning.

## ✅ Answer  

In our organization, we use **JFrog Artifactory** as our primary artifact repository for builds.

---

### 📘 Why JFrog Artifactory?

- **Supports multiple package formats** (Maven, npm, Docker, PyPI, Helm, etc.)
- **Integration with Jenkins & GitHub Actions** for publishing artifacts during CI/CD.
- **Proxying public repositories** like Maven Central or Docker Hub to improve speed and reliability.
- **Access control and security** via RBAC for different teams and projects.
- **Retention policies** to clean up outdated builds automatically.

---

### 🔄 Typical Workflow

1. Developer commits code to GitHub.
2. Jenkins triggers a build and packages the application using Maven.
3. The artifact is pushed to Artifactory using `mvn deploy`.
4. Later stages (like deployment) pull the artifact from Artifactory.

---

### 🧠 Alternatives I've worked with:
- **Sonatype Nexus Repository** – Lightweight and easy to set up for Maven-only use cases.
- **AWS CodeArtifact** – Great for AWS-native environments.
- **GitHub Packages** – Useful for open-source projects or tight GitHub integrations.

---

> Summary:  
> My go-to artifact repository is **JFrog Artifactory** due to its versatility, wide ecosystem support, and strong integration with CI/CD pipelines.

---
