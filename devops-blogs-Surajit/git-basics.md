# GIT Imp Questions
---

### **1. General Git Questions**

#### Q1: What is the difference between `git commit` and `git commit --amend`?
**Answer:**
- **`git commit`:** Creates a new commit from the staged changes.
- **`git commit --amend`:** Modifies the most recent commit, combining any staged changes with the previous commit. This is often used to correct mistakes like a typo in the commit message or missed changes.
- Example:
  ```bash
  git commit -m "Initial commit"
  git add forgotten-file
  git commit --amend --no-edit
  ```
  This updates the previous commit to include `forgotten-file`.

---

#### Q2: How does Git differ from centralized version control systems like SVN?
**Answer:**
- **Distributed nature:** Every developer has a full copy of the repository in Git, allowing offline access and reducing dependency on a central server.
- **Branching and merging:** Git offers lightweight branching and advanced merge strategies, making it better for collaboration.
- **Speed:** Local operations in Git are faster since no server communication is required.
- **Snapshots vs versions:** Git tracks file changes as snapshots, while SVN maintains changes as deltas.

---

### **2. Branching Strategies**

#### Q3: Explain Git Flow and its advantages and disadvantages.
**Answer:**
**Git Flow** is a branching model that organizes work into:
1. **Main Branches:**
   - `main`: Represents production-ready code.
   - `develop`: Represents integration of features for the next release.
2. **Supporting Branches:**
   - `feature`: Created from `develop` to add a new feature.
   - `release`: Created from `develop` for release preparation.
   - `hotfix`: Created from `main` to quickly patch production issues.

**Advantages:**
- Clear structure for large teams.
- Supports parallel development and stable releases.

**Disadvantages:**
- Overhead for small teams.
- Merge conflicts may occur if not managed properly.

---

#### Q4: How does GitHub Flow differ from Git Flow?
**Answer:**
**GitHub Flow** is simpler, focusing on:
1. **Main branch only:** All deployable code resides in `main`.
2. **Feature branches:** Created for each task/bug/feature and merged into `main` after approval.
3. **Continuous Deployment:** `main` is always production-ready.

**Comparison:**
- **Git Flow** is suited for structured release cycles.
- **GitHub Flow** is better for continuous deployment and smaller teams.

---

#### Q5: How would you design a branching strategy for a team following CI/CD practices?
**Answer:**
1. **Main Branch:** Always production-ready.
2. **Feature Branches:** For new features or fixes, created from `main`.
3. **Pull Request (PR):** Code is reviewed and tested through PR pipelines before merging into `main`.
4. **Release Branches (Optional):** For scheduled releases.
5. **Hotfix Branches:** For critical production issues.

- **Automation:** Implement CI/CD pipelines to test and deploy feature branches upon merging.
- **Protection:** Enforce branch protection rules (e.g., require PR reviews and status checks).

---

### **3. Collaboration**

#### Q6: How do you use Git hooks to enforce code quality in a team?
**Answer:**
Git hooks are scripts triggered by Git events (e.g., commits, pushes).

1. **Pre-commit Hook:** Check for code quality, run linters or formatters.
   ```bash
   # pre-commit hook example
   eslint src/**/*.js
   if [ $? -ne 0 ]; then
       echo "Linting failed. Fix issues before committing."
       exit 1
   fi
   ```

2. **Pre-push Hook:** Run tests before code is pushed.
   ```bash
   npm test
   if [ $? -ne 0 ]; then
       echo "Tests failed. Push aborted."
       exit 1
   fi
   ```

3. **Client-side or server-side:** Use client-side hooks for local checks and server-side hooks for centralized enforcement.

---

#### Q7: How would you manage a code review process in GitHub?
**Answer:**
1. **Create Pull Requests:**
   - Developers open a PR for their feature branches.
   - Include a detailed description of changes and testing details.

2. **Set Review Rules:**
   - Require at least two reviewers.
   - Use **CODEOWNERS** to assign specific reviewers for certain files.

3. **Enforce Quality:**
   - Enable CI checks (e.g., automated testing).
   - Use GitHub Actions for additional validation.

4. **Collaborative Feedback:**
   - Reviewers provide comments inline.
   - Author addresses changes and resolves discussions.

5. **Merge After Approval:**
   - Enforce squash merging to maintain clean commit history.

---

#### Q8: How would you implement collaboration for multiple teams in GitHub?
**Answer:**
1. **Repository Structure:**
   - Use mono-repos for shared code or multi-repos for team isolation.
   - Define a common `main` branch for cross-team collaboration.

2. **Access Controls:**
   - Use GitHub teams for managing permissions.
   - Implement branch protection rules to prevent unauthorized changes.

3. **Workflow Standardization:**
   - Enforce naming conventions for branches (`feature/`, `bugfix/`).
   - Use templates for PRs and issues to streamline contributions.

4. **Documentation:**
   - Maintain a `CONTRIBUTING.md` file outlining the collaboration process.
   - Use GitHub Wikis or READMEs for additional guidance.

---

### **4. Advanced Scenarios**

#### Q9: How would you resolve a merge conflict between two branches?
**Answer:**
1. **Identify Conflict:**
   ```bash
   git merge branch-name
   ```

2. **Locate Conflicts:**
   - Git marks conflicting sections in files with `<<<<<<<`, `=======`, and `>>>>>>>`.

3. **Resolve Conflicts:**
   - Edit files to resolve conflicts manually.
   - Use tools like `git mergetool` for assistance.

4. **Mark as Resolved:**
   ```bash
   git add resolved-file
   ```

5. **Complete the Merge:**
   ```bash
   git commit
   ```

---

#### Q10: How would you revert a problematic commit in production?
**Answer:**
1. **Identify Commit:**
   ```bash
   git log
   ```

2. **Revert Commit:**
   - Create a new commit that undoes changes:
     ```bash
     git revert <commit-hash>
     ```

3. **Push Changes to Production:**
   ```bash
   git push origin main
   ```

4. **Alternative (if the branch is not shared):**
   ```bash
   git reset --hard <commit-hash>
   git push --force
   ```
   Use this cautiously as it rewrites history.

---

#### Q11: What are some best practices for Git commit messages?
**Answer:**
1. **Use Conventional Commits Format:**
   - Structure: `<type>(<scope>): <subject>`
   - Example: `feat(auth): add login endpoint`

2. **Keep It Short:**
   - Limit the subject to 50 characters.

3. **Explain Why:**
   - Use the body to describe **why** changes were made.

4. **Reference Issues or Tickets:**
   - Include issue numbers or links, e.g., `Closes #123`.

5. **Avoid Redundant Words:**
   - E.g., "Added login endpoint" instead of "This commit adds login endpoint."

---

### **1. How does `git stash` work, and when would you use it?**  
**Answer:**  
`git stash` temporarily saves uncommitted changes without adding them to a commit.  
- **Usage Scenarios:**  
  - Switching branches while preserving work in progress.  
  - Testing a different commit or branch.  
- **Commands:**  
  ```bash
  git stash        # Save current changes
  git stash list   # View saved stashes
  git stash apply  # Reapply changes from stash
  git stash drop   # Remove stash after applying
  ```  
  Example:  
  - Work on `feature1`, stash changes, switch to `main`, and return later to `feature1`.

---

### **2. What is a rebase, and how is it different from a merge?**  
**Answer:**  
- **Rebase:** Moves commits from one branch to another base, creating a linear history.  
- **Merge:** Combines branches, preserving their commit history (non-linear).  
- **Differences:**  
  - Rebase rewrites history, merge does not.  
  - Rebase is cleaner for linear workflows; merge is better for preserving context.  
- **Rebase Command:**  
  ```bash
  git checkout feature  
  git rebase main
  ```

---

### **3. How would you squash multiple commits into one?**  
**Answer:**  
1. Start an interactive rebase:  
   ```bash
   git rebase -i HEAD~<number-of-commits>
   ```  
2. Mark commits to squash (`pick` → `squash`).  
3. Edit the commit message.  
4. Save and complete the rebase.  
- **Use Case:** Clean up commit history before merging.  

---

### **4. What is `git cherry-pick`, and when would you use it?**  
**Answer:**  
`git cherry-pick` applies a specific commit from one branch to another.  
- **Use Case:**  
  - Apply a bug fix from `main` to a feature branch without merging the entire branch.  
- **Command:**  
  ```bash
  git cherry-pick <commit-hash>
  ```

---

### **5. How do you enforce Git commit conventions in a project?**  
**Answer:**  
1. **Pre-commit Hook:**  
   - Use a Git hook to check commit messages.  
     Example (pre-commit hook):  
     ```bash
     #!/bin/sh
     if ! grep -qE '^(feat|fix|docs|style|refactor|test|chore)\:' "$1"; then
         echo "Commit message must follow the convention: <type>: <message>"
         exit 1
     fi
     ```
2. **Linting Tools:**  
   - Tools like **Commitlint** validate messages based on defined rules.  

---

### **6. How would you design a collaborative Git workflow for geographically distributed teams?**  
**Answer:**  
1. Use a **main branch** for production-ready code.  
2. Use **feature branches** for tasks, ensuring local testing.  
3. Implement **Pull Requests (PRs)** for code reviews.  
4. Automate CI/CD pipelines to validate PRs.  
5. Enforce branch protection and require code reviews for merges.  
6. Use tools like **GitHub Actions** to standardize workflows.

---

### **7. What is the `git bisect` command, and how do you use it?**  
**Answer:**  
`git bisect` identifies a commit that introduced a bug by performing a binary search.  
- **Steps:**  
  1. Start bisect:  
     ```bash
     git bisect start
     git bisect bad            # Mark the current commit as bad
     git bisect good <commit>  # Mark an earlier commit as good
     ```  
  2. Test each commit until the bad commit is found.  
  3. End bisect:  
     ```bash
     git bisect reset
     ```  

---

### **8. What is the difference between `git pull` and `git fetch`?**  
**Answer:**  
- **`git fetch`:** Downloads updates from the remote repository but doesn’t merge them into the local branch.  
- **`git pull`:** Combines `git fetch` and `git merge` to update the local branch with remote changes.  
- **Best Practice:** Use `git fetch` and review changes before merging.

---

### **9. How can you ensure code consistency across branches?**  
**Answer:**  
1. Enforce CI checks for testing, linting, and formatting during PRs.  
2. Use branch protection rules to prevent direct commits to `main`.  
3. Periodically rebase or merge `main` into long-lived feature branches to keep them updated.  
4. Use tools like **SonarQube** to enforce coding standards.

---

### **10. How do you handle large binary files in Git?**  
**Answer:**  
- Use **Git LFS (Large File Storage):**  
  - Tracks binary files without bloating the repository.  
  - Example:  
    ```bash
    git lfs install
    git lfs track "*.png"
    git add .gitattributes
    git commit -m "Track binary files with LFS"
    ```
- Store large files in a dedicated storage solution (e.g., S3) and reference them in the codebase.

---

### **11. What is `git reset`, and what are the three modes of reset?**  
**Answer:**  
- `git reset` moves the current branch to a specific commit.  
- **Modes:**  
  1. **Soft:** Keeps changes staged.  
     ```bash
     git reset --soft HEAD~1
     ```
  2. **Mixed (default):** Unstages changes but keeps them in the working directory.  
     ```bash
     git reset HEAD~1
     ```
  3. **Hard:** Discards changes entirely.  
     ```bash
     git reset --hard HEAD~1
     ```

---

### **12. How would you recover a deleted branch in Git?**  
**Answer:**  
1. Find the commit hash of the deleted branch:  
   ```bash
   git reflog
   ```  
2. Recreate the branch:  
   ```bash
   git checkout -b branch-name <commit-hash>
   ```

---

### **13. How do you handle submodules in Git?**  
**Answer:**  
- **Add Submodule:**  
  ```bash
  git submodule add <repository-url>
  ```
- **Initialize and Update Submodules:**  
  ```bash
  git submodule update --init --recursive
  ```
- **Remove Submodule:**  
  1. Delete the submodule from `.gitmodules` and `.git/config`.  
  2. Remove the submodule directory:  
     ```bash
     git rm --cached <submodule-path>
     rm -rf <submodule-path>
     ```

---

### **14. How do you prevent sensitive information from being committed to Git?**  
**Answer:**  
1. **Use `.gitignore`:**  
   - Exclude files containing sensitive data.  
     ```bash
     echo ".env" >> .gitignore
     git add .gitignore
     git commit -m "Add .gitignore"
     ```
2. **Pre-commit Hooks:**  
   - Scan commits for sensitive information.  
3. **Git Secrets:**  
   - Use tools like **Git-secrets** to prevent accidental commits.  

---

### **15. How do you efficiently manage multiple repositories in a project?**  
**Answer:**  
1. Use **Git Submodules** or **Git Subtrees** for dependencies.  
2. Use tools like **Terragrunt** to standardize workflows across repos.  
3. Implement a central CI/CD system to automate testing and deployments for all repos.  
4. Maintain a shared README or documentation for cross-repository guidelines.

---

### **1. What is GitHub Actions, and why is it important in a CI/CD pipeline?**  
**Answer:**  
GitHub Actions is a built-in automation tool in GitHub that allows you to define workflows triggered by GitHub events (e.g., push, pull requests).  
- **Importance:**  
  - Seamlessly integrates with GitHub repositories.  
  - Automates tasks like testing, building, and deploying.  
  - Scalable and supports custom runners.  
- **Example Workflow File:**  
  ```yaml
  name: CI Pipeline
  on: [push, pull_request]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - name: Run Tests
          run: npm test
  ```

---

### **2. How do you trigger a workflow only on changes to a specific file or directory?**  
**Answer:**  
You can define `paths` in the workflow trigger.  
- **Example:**  
  ```yaml
  on:
    push:
      paths:
        - "src/**"
        - "!docs/**"
  ```  
- **Use Case:** Run tests only when code changes, ignoring documentation updates.

---

### **3. How do you use GitHub Secrets in GitHub Actions?**  
**Answer:**  
GitHub Secrets securely store sensitive information (e.g., API keys, passwords).  
- **Steps:**  
  1. Add a secret in the repository settings under **Settings → Secrets and Variables**.  
  2. Reference the secret in workflows:  
     ```yaml
     jobs:
       deploy:
         steps:
           - name: Deploy to AWS
             env:
               AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
               AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
             run: aws deploy
     ```

---

### **4. How do you test a GitHub Actions workflow before committing it?**  
**Answer:**  
1. **Use a local runner:** Tools like [act](https://github.com/nektos/act) simulate workflows locally.  
   ```bash
   act -j <job-name>
   ```  
2. **Debug with Workflow Logs:** Enable `ACTIONS_RUNNER_DEBUG`.  
   ```yaml
   steps:
     - run: echo "Debugging"  
       env:  
         ACTIONS_RUNNER_DEBUG: true
   ```

---

### **5. How do you create reusable workflows in GitHub Actions?**  
**Answer:**  
Reusable workflows allow defining common logic that multiple workflows can call.  
- **Steps:**  
  1. Define a reusable workflow (`.github/workflows/common.yml`):  
     ```yaml
     name: Reusable Workflow
     on:
       workflow_call:
         inputs:
           branch:
             required: true
     jobs:
       build:
         runs-on: ubuntu-latest
         steps:
           - run: echo "Building branch ${{ inputs.branch }}"
     ```  
  2. Reference it in another workflow:  
     ```yaml
     jobs:
       use-reusable:
         uses: ./.github/workflows/common.yml
         with:
           branch: main
     ```

---

### **6. How do you implement a branching strategy like GitHub Flow using GitHub Actions?**  
**Answer:**  
**GitHub Flow Strategy:**  
- A single `main` branch for production.  
- Feature branches for changes merged via Pull Requests (PRs).  
- Use GitHub Actions to automate:  
  - **On PR Creation:** Run tests.  
  - **On Merge:** Trigger a deployment workflow.  

**Example Workflow:**  
```yaml
name: GitHub Flow CI/CD
on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm test

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh
```

---

### **7. How can you optimize workflow execution in GitHub Actions?**  
**Answer:**  
1. **Use Caching:** Reduce redundant steps by caching dependencies.  
   ```yaml
   steps:
     - name: Cache Node Modules
       uses: actions/cache@v3
       with:
         path: node_modules
         key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
   ```  
2. **Matrix Builds:** Run jobs in parallel for different environments.  
   ```yaml
   strategy:
     matrix:
       os: [ubuntu-latest, windows-latest]
       node: [12, 14, 16]
   ```  
3. **Selective Triggers:** Use `paths` and `paths-ignore`.

---

### **8. How do you handle dependencies between jobs in GitHub Actions?**  
**Answer:**  
- Use `needs` to define job dependencies.  
- Example:  
  ```yaml
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - run: echo "Building code"
    test:
      runs-on: ubuntu-latest
      needs: build
      steps:
        - run: echo "Running tests"
  ```

---

### **9. How do you handle self-hosted runners in GitHub Actions?**  
**Answer:**  
1. Install a self-hosted runner on your infrastructure.  
   - Follow instructions under **Settings → Actions → Runners → Add Runner**.  
2. Use the runner in your workflow:  
   ```yaml
   jobs:
     custom-runner-job:
       runs-on: self-hosted
       steps:
         - run: echo "Running on self-hosted runner"
   ```  
- **Best Practices:** Ensure runner security, and isolate sensitive workloads.

---

### **10. How do you integrate GitHub Actions with external tools (e.g., Slack, Jira)?**  
**Answer:**  
1. Use marketplace actions (e.g., [Slack Notification](https://github.com/marketplace/actions/slack-notify)).  
   ```yaml
   steps:
     - name: Notify Slack
       uses: rtCamp/action-slack-notify@v2
       env:
         SLACK_CHANNEL: ${{ secrets.SLACK_CHANNEL }}
         SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
   ```  
2. Use REST APIs to send data from workflows to external tools.

---

### **11. How do you debug failing workflows in GitHub Actions?**  
**Answer:**  
1. **View Workflow Logs:** Check logs for each step.  
2. **Enable Debug Logs:**  
   ```yaml
   steps:
     - run: echo "Debugging..."  
       env: ACTIONS_STEP_DEBUG: true
   ```  
3. Use `continue-on-error: true` for non-blocking steps.

---

### **12. How would you implement a multi-environment deployment pipeline using GitHub Actions?**  
**Answer:**  
1. Define environment-specific jobs with deployment conditions.  
2. Use environment protection rules for approvals.  

**Example:**  
```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh dev
    environment:
      name: dev
  promote-to-prod:
    needs: deploy
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh prod
    environment:
      name: production
      environment_protection_rules:
        reviewers:
          - team-leads
```

---

### **13. What are concurrency and workflow queues in GitHub Actions?**  
**Answer:**  
- **Concurrency:** Prevents multiple runs of a workflow for the same branch.  
  ```yaml
  concurrency:
    group: ${{ github.ref }}
    cancel-in-progress: true
  ```  
- **Workflow Queues:** Jobs queued if concurrency rules block new runs.

---

### **14. How do you secure GitHub Actions workflows?**  
**Answer:**  
1. Use **GitHub Secrets** for sensitive data.  
2. Restrict workflow execution to trusted branches or users:  
   ```yaml
   on:
     push:
       branches:
         - main
   ```  
3. Validate third-party actions by pinning versions.

---

### **15. How do you manage monorepo workflows in GitHub Actions?**  
**Answer:**  
1. Use conditional steps to trigger workflows for specific directories:  
   ```yaml
   steps:
     - uses: actions/checkout@v3
     - run: |
         if [ "$(git diff --name-only HEAD~1 | grep '^service1/')" ]; then
           echo "Changes detected in service1"
           ./build-service1.sh
         fi
   ```  
2. Use matrix builds to run workflows per service in parallel.

