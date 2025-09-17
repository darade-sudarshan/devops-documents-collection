## Question  
A developer pushes a feature branch, but the pipeline doesn’t trigger in GitHub Actions. What could be wrong?

### 📝 Short Explanation  
If a GitHub Actions pipeline doesn’t trigger when a branch is pushed, it's usually due to **misconfigured trigger rules**, **file path filters**, or **workflow scope issues**.

## ✅ Answer  

When this happens, I check the following areas step-by-step to isolate and fix the issue.

---

### 🧭 Step-by-Step Troubleshooting

#### 1. 🔍 **Check the `on:` Section in the Workflow**
- GitHub Actions triggers are defined under the `on:` field. Make sure it includes `push` and relevant branches.

**Example of incorrect config (only main branch will trigger):**
```yaml
on:
  push:
    branches:
      - main
```

**Fix: include `feature/*` pattern or all branches:**
```yaml
on:
  push:
    branches:
      - main
      - 'feature/*'
      - 'dev'
```

---

#### 2. 📁 **Check `paths` Filter (if used)**
If the workflow has a `paths:` filter, it will only trigger if specific files are changed.

```yaml
on:
  push:
    paths:
      - 'src/**'
```

If a developer changed a file outside the listed paths, the pipeline won’t trigger.

---

#### 3. 🧪 **Check if the Workflow File is on Default Branch**
- Workflows stored in `.github/workflows/` must exist on the **default branch** (usually `main`) to trigger from other branches.

If the workflow file was only added in the `feature/xyz` branch, it won’t trigger on push unless merged to the main branch.

---

#### 4. 🔒 **Check Branch Protection or Permissions**
- If GitHub Actions is disabled for the repo or workflow permissions are restricted (`Settings → Actions → General`), it may block pipeline execution.

---

#### 5. 🧼 **Verify `.github/workflows/*.yml` File Validity**
- Run `act` locally or use the **GitHub Actions → Logs** to check for YAML syntax errors.
- A broken workflow file might silently fail to register triggers.

---

### 🧠 Real-World Fix

A developer pushed to `feature/payment-refactor`, but the workflow didn’t run.  
We found that:
- The `on.push.branches` section only had `main` and `develop`.
- After updating it to include `'feature/*'`, it started working as expected.

---

> Summary:  
> If GitHub Actions doesn’t trigger on feature branch push:
> - Check `on.push.branches` config
> - Ensure no blocking `paths:` filter
> - Confirm workflow file exists on default branch
> - Validate repo settings and workflow file syntax

---
