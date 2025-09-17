## Question  
A teammate accidentally committed a Kubernetes Secret (base64 encoded) to Git. What should you do?

### 📝 Short Explanation  
This scenario tests how you respond to a security breach and how well you understand Git history rewriting, sensitive data handling, and Kubernetes secrets management.

## ✅ Answer  
Immediately remove the secret from the Git history using tools like `git filter-repo` or `BFG`, rotate the compromised secret, and enforce better secret management policies (e.g., use sealed secrets or external secret stores).

### 📘 Detailed Explanation  

When a Kubernetes Secret (even base64-encoded) is committed to Git, it becomes publicly visible to:
- Everyone with repo access
- Anyone who forked or cloned the repo before removal
- CI/CD systems that fetch the repo

### 🛠️ Step-by-Step Response:

---

#### ✅ Step 1: Rotate the compromised secret  
Whether it’s an API key, database password, or token — assume it’s compromised.

- Create a new secret value (e.g., generate a new DB password or token).
- Update the Kubernetes Secret:
  ```bash
  kubectl create secret generic my-secret --from-literal=password=newpassword --dry-run=client -o yaml | kubectl apply -f -
  ```
- Update any workloads consuming the old secret.

---

#### ✅ Step 2: Remove the secret from Git history  
Base64 encoding is **not encryption**. Anyone can decode it.

If it was recently committed:
```bash
git reset HEAD~1
git restore --staged secret.yaml
rm secret.yaml
git commit -m "Remove secret from repo"
```

But this only removes it from the latest commit. To fully remove it from **entire history**:

Use [`git filter-repo`](https://github.com/newren/git-filter-repo) (preferred over `filter-branch`):
```bash
git filter-repo --path secret.yaml --invert-paths
```

Or use **BFG Repo-Cleaner**:
```bash
bfg --delete-files secret.yaml
```

Then force-push:
```bash
git push --force
```

> Everyone with clones will need to re-clone or follow special instructions to realign their history.

---

#### ✅ Step 3: Prevent it from happening again  
- Add sensitive files to `.gitignore`
  ```
  secrets.yaml
  *.key
  ```
- Use tools like [git-secrets](https://github.com/awslabs/git-secrets) or [pre-commit](https://pre-commit.com/) to scan commits for secrets.
- Educate team members that **Kubernetes Secrets are not encrypted by default in Git**, even though they look scrambled (base64).

---

### 🚫 Why This Matters  
Hardcoded secrets in Git are one of the most common security missteps. Even private repos can be compromised. This situation reflects your ability to respond quickly, contain damage, and improve team practices.

> Summary:  
> Rotate → Remove → Recommit safely → Enforce policies.

---
