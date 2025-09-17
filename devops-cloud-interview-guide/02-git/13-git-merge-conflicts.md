## Question  
How do you handle merge conflicts in Git?

### 📝 Short Explanation  
Merge conflicts are a common part of collaborative Git workflows. This question is meant to test how calmly and effectively you resolve conflicts and whether you understand why they occur.

## ✅ Answer  
When I encounter a merge conflict, I pause to understand which files are affected, examine the conflicting changes, and manually resolve them using a visual diff tool or editor. Once resolved, I mark the conflicts as resolved, stage the changes, and complete the merge or rebase.

### 📘 Detailed Explanation  
Merge conflicts usually happen when:
- Two branches modify the same lines in a file
- One branch deletes a file the other modifies
- A rebase applies commits that overlap with existing changes

Here’s how I handle them:

#### 🔍 Step 1: Identify the conflict
Git clearly indicates the files with conflicts during a `git merge` or `git rebase`:
```bash
Auto-merging app.py  
CONFLICT (content): Merge conflict in app.py  
```

#### 🛠️ Step 2: Open and resolve the conflict
Conflicted files contain markers like:
```diff
<<<<<<< HEAD
print("Hello from main")
=======
print("Hello from feature-branch")
>>>>>>> feature-branch
```

I manually edit the file to reflect the correct final code, based on the intended logic. Sometimes I use tools like:
- `git diff` to understand the changes
- Visual Studio Code or GitKraken for visual resolution

#### ✅ Step 3: Mark as resolved
Once edited:
```bash
git add app.py
```

Then complete the merge:
```bash
git commit         # if using merge
# or
git rebase --continue  # if using rebase
```

> Merge conflicts aren’t errors — they’re just Git asking you to make a decision. Handling them well is part of being a collaborative engineer.

---
