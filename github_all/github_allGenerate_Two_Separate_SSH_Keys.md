# Setting Up SSH Keys for Personal and Work GitHub Accounts

This guide explains how to configure separate SSH keys for personal and work GitHub accounts while keeping them distinct and avoiding conflicts.

---

## Step 1: Generate Two Separate SSH Keys

### Generate SSH Key for Personal Account
1. Open a terminal or PowerShell:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your-personal-email@example.com"
   ```
2. When prompted, save the key as:
   ```plaintext
   C:\Users\sudip\.ssh\id_rsa_personal
   ```
3. Set a passphrase if desired (optional).

### Generate SSH Key for Work Account
1. Generate the second key:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your-work-email@example.com"
   ```
2. Save the key as:
   ```plaintext
   C:\Users\sudip\.ssh\id_rsa_work
   ```
3. Set a passphrase if desired (optional).

---

## Step 2: Add Both Keys to the SSH Agent

1. Start the SSH agent:
   ```bash
   Start-Service ssh-agent
   ```
2. Add the personal key:
   ```bash
   ssh-add C:\Users\sudip\.ssh\id_rsa_personal
   ```
3. Add the work key:
   ```bash
   ssh-add C:\Users\sudip\.ssh\id_rsa_work
   ```

---

## Step 3: Configure the SSH `config` File

1. Navigate to the `.ssh` directory:
   ```bash
   cd ~/.ssh
   ```
2. Create or edit the `config` file:
   ```bash
   nano config
   ```
3. Add the following configuration:
   ```plaintext
   # Personal GitHub Account
   Host github-personal
       HostName github.com
       User git
       IdentityFile ~/.ssh/id_rsa_personal

   # Work GitHub Account
   Host github-work
       HostName github.com
       User git
       IdentityFile ~/.ssh/id_rsa_work
   ```
4. Save and exit the editor.
5. Set the correct permissions for the `config` file:
   ```bash
   chmod 600 ~/.ssh/config
   ```

---

## Step 4: Add the SSH Keys to Your GitHub Accounts

### For Personal Account
1. Display the public key:
   ```bash
   cat C:\Users\sudip\.ssh\id_rsa_personal.pub
   ```
2. Copy the output.
3. Go to [GitHub SSH Keys Settings](https://github.com/settings/keys).
4. Click **New SSH Key**.
5. Enter a title (e.g., "Personal SSH Key") and paste the key.
6. Save the key by clicking **Add SSH Key**.

### For Work Account
1. Display the public key:
   ```bash
   cat C:\Users\sudip\.ssh\id_rsa_work.pub
   ```
2. Copy the output.
3. Go to the **SSH Keys Settings** for your work account or organization.
4. Click **New SSH Key**.
5. Enter a title (e.g., "Work SSH Key") and paste the key.
6. Save the key by clicking **Add SSH Key**.

---

## Step 5: Set Up Git Remotes

### Personal Repository
Use the personal SSH alias:
```bash
git remote set-url origin git@github-personal:username/repo.git
```

### Work Repository
Use the work SSH alias:
```bash
git remote set-url origin git@github-work:organization/repo.git
```

---

## Step 6: Test the Setup

### Personal Account
Test the connection:
```bash
ssh -T github-personal
```
Expected output:
```
Hi <your-personal-username>! You've successfully authenticated, but GitHub does not provide shell access.
```

### Work Account
Test the connection:
```bash
ssh -T github-work
```
Expected output:
```
Hi <your-work-username>! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## Notes
- Use `github-personal` and `github-work` aliases in your Git operations to avoid conflicts.
- Ensure the correct `IdentityFile` is specified for each account in the SSH `config` file.

---

This guide ensures a clean and organized setup for managing multiple GitHub accounts using SSH.
