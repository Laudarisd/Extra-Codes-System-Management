How to Install TexStudio 2.12.18 in Ubuntu:
==============================================

**Open terminal either by pressing `Ctrl+Alt+T` on keyboard or by searching for `terminal’`from software launcher. When it opens, run command:**

```
$ sudo add-apt-repository ppa:sunderme/texstudio
```

**If an old version was installed in your system, remove the texstudio-doc, texstudio-l10n (if any) package before upgrading the software**

```
$ sudo apt-get remove texstudio-doc texstudio-l10n
```


**Run commands in terminal to install or upgrade the software:**

```
$ sudo apt-get update && sudo apt-get install texstudio
```


Uninstall
===============

```
$ sudo apt-get remove --autoremove texstudio
$ sudo apt autoremove
```