## Question  
When a build fails in Jenkins, how will you send an email?

### 📝 Short Explanation  
To notify stakeholders or developers about failed builds, Jenkins can send automated emails using the **Email Notification** or **Editable Email Notification** plugin.

## ✅ Answer  

When a Jenkins build fails, I configure it to **automatically send email alerts** using either the **built-in Email Notification** system or the **Email Extension Plugin** for more control.

---

### 🧭 Steps to Configure Email Notifications on Build Failure

#### 1. 🧩 **Install Email Extension Plugin**
- Go to **Manage Jenkins → Plugin Manager → Available**
- Search and install: `Email Extension Plugin`

---

#### 2. ⚙️ **Global Configuration**
Navigate to **Manage Jenkins → Configure System**  
- Set SMTP details:
  - SMTP server (e.g., `smtp.gmail.com`)
  - Use SSL/TLS
  - Port (typically 465 or 587)
  - Jenkins Email address (default sender)
- Set up authentication (username/password or app token)

✅ Example (for Gmail):
```text
SMTP Server: smtp.gmail.com
Use SSL: true
Port: 465
```

---

#### 3. 📤 **Configure Project to Send Emails**
In your Jenkins pipeline job or freestyle job:

- Scroll to **Post-build Actions**
- Add **Editable Email Notification**
  - **Project Recipient List:** e.g., `dev-team@example.com`
  - **Triggers:** Select **Failure - Send email on build failure**

✅ Optional Email Content:
- Subject: `$PROJECT_NAME - Build #$BUILD_NUMBER - FAILED!`
- Body:
```groovy
Build failed at $BUILD_URL
Triggered by: $CAUSE
```

---

#### 4. 🧪 **Testing**
Trigger a dummy failure and confirm that email notifications are received.

---

### 🧠 Real-World Example

In our Jenkins setup:
- We used the **Email Extension Plugin**
- Configured triggers for `FAILURE`, `UNSTABLE`, and `FIXED`
- Used custom HTML templates to include links to logs and commit diffs
- For pull requests, we added author-specific alerts using `git commit --author`

---

> Summary:  
> To notify on build failure:
> - Install and configure the Email Extension Plugin  
> - Set SMTP details under Jenkins global settings  
> - Enable email triggers in your job configuration  
> - Customize recipient list and email templates for clarity

---
