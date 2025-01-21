# Git User and SSH Key Setup Guide

This guide provides step-by-step instructions for managing GitHub users, switching accounts, creating branches, and setting up SSH keys for multiple GitHub accounts on Windows.

---

## **1. Check GitHub User and Email**

### **Instructions**
To verify the currently configured GitHub user and email, run:
```bash
# Check Git user
git config --global user.name

# Check Git email
git config --global user.email
```

### **Explanation**
These commands display the globally configured Git username and email associated with your commits. If these values don’t match the desired GitHub account, you’ll need to switch users.

---

## **2. Switch User to Desired One**

### **Instructions**
To switch the Git user for your current project:
```bash
# Set user for the current repository
cd /path/to/your/repository

git config user.name "DesiredUsername"
git config user.email "desired-email@example.com"
```

If you want to switch the global user (applies to all repositories):
```bash
git config --global user.name "DesiredUsername"
git config --global user.email "desired-email@example.com"
```

### **Explanation**
Setting the user and email locally ensures commits in the current repository are associated with the desired GitHub account. Setting them globally applies to all repositories.

---

## **3. Create Main and Dev Branches**

### **Instructions**
1. To create and switch to a new branch `dev`:
   ```bash
   git checkout -b dev
   ```

2. Push the `dev` branch to GitHub:
   ```bash
   git push -u origin dev
   ```

3. To ensure you have a `main` branch:
   ```bash
   git checkout main
   git push -u origin main
   ```

### **Explanation**
The `checkout -b` command creates and switches to a new branch. Pushing the branch with `-u` sets the upstream tracking branch on GitHub.

---

## **Issue 1: Setting Up SSH Key for Multiple GitHub Accounts**

### **Instructions**
1. **Generate a New SSH Key for Each Account**:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "work-email@example.com"
   ```
   - Save the key with a unique name (e.g., `id_rsa_work`):
     ```
     C:\Users\username\.ssh\id_rsa_work
     ```

2. **Add the Key to the SSH Agent**:
   ```bash
   Start-Service ssh-agent
   ssh-add C:\Users\username\.ssh\id_rsa_work
   ```

3. **Add the Public Key to GitHub**:
   - Copy the public key:
     ```bash
     cat C:\Users\username\.ssh\id_rsa_work.pub
     ```
   - Go to **GitHub > Settings > SSH and GPG keys > New SSH Key**.
   - Paste the copied key and save.

4. **Configure SSH for Multiple Accounts**:
   Edit the SSH config file:
   ```bash
   notepad C:\Users\username\.ssh\config
   ```

   Add the following:
   ```
   # Work account
   Host github-work
       HostName github.com
       User git
       IdentityFile ~/.ssh/id_rsa_work

   # Personal account
   Host github-personal
       HostName github.com
       User git
       IdentityFile ~/.ssh/id_rsa
   ```

5. **Update Repository Remote URLs**:
   For the work repository:
   ```bash
   git remote set-url origin git@github-work:organization/repository.git
   ```
   For the personal repository:
   ```bash
   git remote set-url origin git@github-personal:username/repository.git
   ```

---

## **Issue 2: Saving and Generating Keys**

### **Example Commands**
1. **Generate Key**:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "example-email@example.com"
   ```
   Save with a custom filename (e.g., `id_rsa_example`).

2. **Add Key to SSH Agent**:
   ```bash
   ssh-add C:\Users\username\.ssh\id_rsa_example
   ```

3. **Check SSH Keys**:
   ```bash
   ssh-add -l
   ```

4. **Test SSH Connection**:
   ```bash
   ssh -T github-work
   ssh -T github-personal
   ```

---

## **Issue 3: Check Git User and Test Credentials**

### **Instructions**
1. **Verify the Configured User**:
   ```bash
   git config user.name
   git config user.email
   ```

2. **Test Repository Access**:
   ```bash
   ssh -T git@github.com
   ```
   For specific accounts:
   ```bash
   ssh -T github-work
   ssh -T github-personal
   ```

3. **Push Changes**:
   ```bash
   git push origin branch-name
   ```

### **Explanation**
Testing ensures that the correct SSH key and credentials are being used for the intended account and repository.

---

This guide helps you manage multiple GitHub accounts and ensure seamless switching and access control. Copy this to your GitHub repository for quick reference!
