## Question  
When using `curl`, the request works with an IP address but fails when using the domain name.

**Task:**  
Explain why this might happen and how you would troubleshoot it.

### 📝 Short Explanation  
This scenario points to a **DNS resolution problem** — your system can reach the server IP directly, but it cannot translate the domain name into an IP.

## ✅ Answer  

If `curl http://<IP>` works but `curl http://example.com` fails, the issue is most likely **DNS-related**.

---

### 📘 Detailed Explanation

#### 🔍 Common Causes:

1. **DNS Not Resolving**
   - Your system cannot resolve `example.com` to its IP.
   - Run:
     ```bash
     nslookup example.com
     dig example.com
     ```
   - If these fail, DNS is the root issue.

---

2. **Wrong or Missing DNS Configuration**
   - Check `/etc/resolv.conf` (Linux) to ensure a valid DNS nameserver (e.g., `8.8.8.8`) is present.
   - Your system might not be using any DNS server or is using one that's unreachable.

---

3. **Firewall or Network Blocking DNS**
   - Port **53** (used for DNS) might be blocked.
   - Test with:
     ```bash
     dig example.com @8.8.8.8
     ```

---

4. **Domain Doesn't Exist or Typo**
   - Confirm the domain name is correct and publicly registered.
   - Try visiting it from another network or use `whois`:
     ```bash
     whois example.com
     ```

---

5. **Host File Override**
   - Check `/etc/hosts` for incorrect entries:
     ```bash
     cat /etc/hosts
     ```
   - Remove or correct any conflicting lines.

---

6. **Internal DNS Only**
   - If the domain is internal (e.g., `myapp.internal.local`), and your DNS server isn't set up or reachable, it won't resolve externally.
   - Make sure you're connected to the appropriate VPN or internal network.

---

### ✅ How to Fix

- Add a DNS server like Google DNS:
  ```bash
  echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null
  ```

- Or temporarily test with:
  ```bash
  curl --resolve example.com:80:<IP> http://example.com
  ```

---

> Summary:  
> When `curl` works with an IP but fails with a domain, it’s almost always a **DNS resolution problem**. Use `dig`, `nslookup`, and check `/etc/resolv.conf` or `/etc/hosts` to debug and fix it.

---
