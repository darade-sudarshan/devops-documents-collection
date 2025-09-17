## Question  
How do you combine multiple commits into a single commit in Git?

### 📝 Short Explanation  
This question is meant to evaluate your understanding of Git history manipulation — especially around commit hygiene, squashing, and preparing a clean pull request.

## ✅ Answer  
I use **interactive rebase** to squash multiple commits into a single, meaningful commit before pushing my changes. This helps in keeping the Git history clean and easy to read.

### 📘 Detailed Explanation  
Let’s say I made 4 commits while working on a single feature:

```bash
git log --oneline
abc123 Fix typo  
def456 Add input validation  
ghi789 Update error message  
jkl012 Initial work on login form  
```

Before pushing or raising a PR, I might want to **combine them into a single commit** that says something like:  
`Add login form with validation and error handling`

#### ✅ Here’s how I do it:

```bash
git rebase -i HEAD~4
```

This opens an editor with the last 4 commits:
```text
pick jkl012 Initial work on login form
pick ghi789 Update error message
pick def456 Add input validation
pick abc123 Fix typo
```

I change all but the first `pick` to `squash` or `s`:
```text
pick jkl012 Initial work on login form
squash ghi789 Update error message
squash def456 Add input validation
squash abc123 Fix typo
```

Then I write a new commit message when prompted, save, and exit.

Finally:
```bash
git push origin branch-name --force
```

> Note: You only force-push if the commits were already pushed to remote. Otherwise, a normal push is fine.

---

### 🧠 Why This Is Useful  
- Keeps Git history clean and easier to understand
- Combines all related changes into one atomic commit
- Helpful for reviewers and future debugging
- Commonly used before merging a feature branch into `main`

> This is often referred to as **squashing commits**, and it's a best practice when preparing PRs or fixing review feedback across multiple small commits.

---
