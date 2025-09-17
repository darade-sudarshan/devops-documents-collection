## Question  
Have you ever used Git tags? If yes, why?

### 📝 Short Explanation  
This question checks if you're familiar with versioning and release practices in Git. Tags are an important part of marking stable points in history — especially in CI/CD pipelines and production deployments.

## ✅ Answer  
Yes, I’ve used Git tags primarily to mark release versions of our applications. It helps track which commit corresponds to a production deployment, and makes it easier to roll back or audit changes when needed.

### 📘 Detailed Explanation  
In one of my recent projects, we followed a simple release process where every stable build that passed all stages in our CI/CD pipeline was tagged with a version number — like `v1.0.3`.

I used annotated tags to add context:

```bash
git tag -a v1.0.3 -m "Release version 1.0.3 with critical bug fixes"
git push origin v1.0.3
```

These tags were then picked up by Jenkins and used as part of the deployment name — so we always knew what version was running in production.

#### 🔍 Why Git Tags Are Useful:
- 🎯 **Marking release points:** Helps indicate stable or milestone commits
- 🔄 **Rollback support:** Easily check out a tag to return to a known good state
- 🧪 **Versioned builds:** Many CI systems trigger builds based on tags
- 🔖 **Consistent releases:** Tags act like bookmarks for deployments or patch notes

> In summary: I use Git tags to improve visibility, traceability, and control in software releases — they’re lightweight, powerful, and essential in production workflows.

---
