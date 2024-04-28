# CUDA-installation-guide
Remove, Install nvidia drivers , cuda


###### To remove cuda, nvidia drivers 

```
$ sudo apt-get --purge -y remove 'cuda*'   

or

$ sudo apt-get autoremove --purge cuda  

or

$ sudo apt remove --autoremove nvidia-cuda-toolkit

$ sudo apt-get --purge -y remove 'nvidia*'
```

After this `$sudo reboot` 


###### To install nvidia drivers
```
$ sudo ubuntu-drivers autoinstall

```

* Check version 

```

$ nvidia-smi

```

###### To install Cuda toolkits-nvcc

```
$  sudo apt install nvidia-cuda-toolkit
```
* Check version 
```
$ nvcc --version
```

###### To unistall cuda

```
$ sudo apt-get purge nvidia*
$ sudo apt-get autoremove
$ sudo apt-get autoclean
$ sudo rm -rf /usr/local/cuda*
```
