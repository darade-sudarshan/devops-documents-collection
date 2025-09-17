## Question  
How do you find and delete files larger than 100MB from a given directory?

### 📝 Short Explanation  
This question tests your ability to manage disk space and clean up large files using command-line tools — a frequent task for DevOps and Linux admins.

## ✅ Answer  

### 🖥️ Command (Using `find` and `-exec`)

```bash
find /path/to/directory -type f -size +100M -exec rm -f {} \;
```

---

### 📘 Detailed Explanation

#### 🔍 Breakdown:
- `find`: Linux command to search for files and directories.
- `/path/to/directory`: Replace with your target path (e.g., `/var/log`, `/tmp`).
- `-type f`: Limits results to files only.
- `-size +100M`: Matches files larger than 100 megabytes.
- `-exec rm -f {} \;`: Deletes each matched file:
  - `{}` is replaced by the filename.
  - `\;` ends the `-exec` command.

---

### ✅ Preview Without Deleting (Dry Run)

If you just want to see the files that would be deleted:

```bash
find /path/to/directory -type f -size +100M -exec ls -lh {} \;
```

This prints the size and path of each file over 100MB.

---

### ⚠️ Best Practices
- Always dry-run before deleting anything in production.
- Consider logging deletions or compressing instead of deleting if space permits.
- Automate safely with cron jobs for specific paths, e.g., `/tmp` or `/var/cache`.

> Summary:  
> Use `find` with `-size +100M` and `-exec rm` to clean up oversized files and free up space. Always preview first to avoid accidental deletion of important files.

---
