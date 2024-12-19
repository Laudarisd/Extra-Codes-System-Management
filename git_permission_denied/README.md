# Setting Up SSH Authentication for GitHub on Windows

This guide provides step-by-step instructions to set up SSH authentication for GitHub on a Windows machine, troubleshoot issues, and verify the setup.

---

## Step 1: Verify the SSH Keys

### Command (Same Tab):
```powershell
ls ~/.ssh/
```

### Expected Output:
```
    Directory: C:\Users\<username>\.ssh

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         <date>                     <size> config
-a----         <date>                     <size> id_rsa
-a----         <date>                     <size> id_rsa.pub
-a----         <date>                     <size> known_hosts
```

If no SSH keys exist (`id_rsa` and `id_rsa.pub` are missing), generate a new key pair using:

### Command (Same Tab):
```powershell
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
Follow the prompts and press Enter to accept the default file locations.

---

## Step 2: Start the SSH Agent

### Command (New Tab with Administrator Privileges):
1. **Open a new PowerShell tab as Administrator**:
   - Close the current PowerShell tab.
   - Right-click on PowerShell and select **Run as Administrator**.

2. **Run the following commands**:
```powershell
Set-Service -Name ssh-agent -StartupType Manual
Start-Service ssh-agent
```

If you encounter `Access is denied` or `Cannot start service ssh-agent` errors, retry these commands in the new Administrator tab.

### Verify the Service (Same Tab):
```powershell
Get-Service -Name ssh-agent
```

### Expected Output:
```
Status   Name               DisplayName
------   ----               -----------
Running  ssh-agent          OpenSSH Authentication Agent
```

---

## Step 3: Add the SSH Key to the Agent

### Command (Same Tab):
```powershell
ssh-add C:\Users\<username>\.ssh\id_rsa
```

### Expected Output:
```
Identity added: C:\Users\<username>\.ssh\id_rsa (your_email@example.com)
```

Verify the key:

### Command (Same Tab):
```powershell
ssh-add -l
```

### Expected Output:
```
4096 SHA256:<key_fingerprint> your_email@example.com (RSA)
```

---

## Step 4: Add the SSH Key to GitHub

1. Copy the public key:

### Command (Same Tab):
```powershell
cat C:\Users\<username>\.ssh\id_rsa.pub
```

2. Go to [GitHub SSH Key Settings](https://github.com/settings/keys).
3. Click **New SSH Key**.
4. Paste the copied key into the **Key** field and give it a meaningful title (e.g., "My Windows PC").
5. Click **Add SSH key**.

---

## Step 5: Test the SSH Connection

### Command (Same Tab):
```powershell
ssh -T git@github.com
```

### Expected Output:
If successful:
```
Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.
```

If you see `Permission denied (publickey)`, ensure the key is added to GitHub and restart the SSH agent:

### Commands (Same Tab):
```powershell
ssh-add C:\Users\<username>\.ssh\id_rsa
ssh -T git@github.com
```

---

## Step 6: Update Git Remote URL (if needed)

If you initially used HTTPS for your repository, switch to SSH:

### Command (Same Tab):
```powershell
git remote set-url origin git@github.com:<username>/<repository>.git
```

Verify the URL:

### Command (Same Tab):
```powershell
git remote -v
```

### Expected Output:
```
origin  git@github.com:<username>/<repository>.git (fetch)
origin  git@github.com:<username>/<repository>.git (push)
```

---

## Step 7: Perform Git Operations

Now, retry Git commands like `git fetch` or `git pull`:

### Commands (Same Tab):
```powershell
git fetch origin
git pull
```

### Expected Output:
Commands should execute without any errors.

---

## Troubleshooting

1. **Permission Denied (publickey)**:
   - Ensure the correct SSH key is added to the GitHub account.
   - Verify the key with:
     ```powershell
     ssh-add -l
     ```

2. **SSH Agent Issues**:
   - Ensure the SSH agent is running:
     ```powershell
     Get-Service -Name ssh-agent
     ```

3. **Key File Not Found**:
   - Use the full path to the `id_rsa` file:
     ```powershell
     ssh-add C:\Users\<username>\.ssh\id_rsa
     ```
