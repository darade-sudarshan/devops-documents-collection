## Question  
How do you configure Artifactory for your application in Maven?

### 📝 Short Explanation  
To publish or retrieve artifacts from Artifactory using Maven, you need to configure **authentication credentials** and **repository endpoints** in `settings.xml` and your project's `pom.xml`.

## ✅ Answer  

We configure Maven to work with Artifactory by:

1. **Defining credentials** in `settings.xml`.
2. **Referencing the Artifactory repository** in `pom.xml`.

---

### ⚙️ Step 1: Update `settings.xml`

Located at: `~/.m2/settings.xml`

```xml
<settings>
  <servers>
    <server>
      <id>artifactory</id>
      <username>my-artifactory-user</username>
      <password>my-artifactory-password</password>
    </server>
  </servers>
</settings>
```

🔐 For security: use Maven’s built-in `mvn --encrypt-password` and store the encrypted password here.

---

### ⚙️ Step 2: Configure `pom.xml` to Use Artifactory

Add this to your Maven project’s `pom.xml`:

```xml
<distributionManagement>
  <repository>
    <id>artifactory</id>
    <name>Company Release Repo</name>
    <url>https://artifactory.example.com/artifactory/libs-release-local</url>
  </repository>
  <snapshotRepository>
    <id>artifactory</id>
    <name>Company Snapshot Repo</name>
    <url>https://artifactory.example.com/artifactory/libs-snapshot-local</url>
  </snapshotRepository>
</distributionManagement>
```

Make sure the `<id>` matches the one in `settings.xml`.

---

### 🚀 Deploy Command

Once configured, deploy your build to Artifactory using:
```bash
mvn clean deploy
```

---

### ✅ What This Achieves

- Pulls dependencies from Artifactory (if configured in `<repositories>`).
- Pushes your built artifacts (`.jar`, `.war`, etc.) to Artifactory.
- Supports release and snapshot repositories.

---

> Summary:  
> To integrate Maven with Artifactory, we configure `settings.xml` with credentials and `pom.xml` with repository URLs. This allows secure and automated artifact publishing as part of CI/CD pipelines.

---
