Installing Visual Studio Code with apt
=======================================

**Update the packages index and install the dependencies**

```
$ sudo apt update
$ sudo apt install software-properties-common apt-transport-https wget
```

**Import the Microsoft GPG key using the following wget command :**

```
$ wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
```

**Inable the Visual Studio Code repository by typing:**

```
$ sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
```


**O*nce the apt repository is enabled , install the Visual Studio Code package**

```
$ sudo apt install code
```

When a new version is released you can update the Visual Studio Code package through your desktop standard Software Update tool or by running the following commands in your terminal:

```
$ sudo apt update
$ sudo apt upgrade
```


---------------------------------------------------------------

If vs opens files in a single tab
==================================

Go to : file >- preferences >- settings >- users setting 

then change this line to false in setting.js file 

```
workbench.editor.enablePreview": false

or 

workbench.editor.enablePreviewFromQuickOpen": false
```


Uninstall
===============

```
$ sudo apt purge code
$ sudo apt autoremove
```