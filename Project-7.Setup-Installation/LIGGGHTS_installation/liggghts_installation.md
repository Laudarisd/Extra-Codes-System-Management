Compile `LIGGGHTS` in ubuntu 20.04 with python
===============================================

Install necessary packages

```
$ sudo apt-get install ffmpeg 
$ sudo apt install openmpi-bin
$ sudo apt install git
```

Clone the  repository
======================

```
$ git clone https://github.com/CFDEMproject/LIGGGHTS-PUBLIC.git
```

Install prerequisties before building liggghts
==================================================

```
$ sudo apt-get install openmpi-bin libopenmpi-dev libvtk6.3 libvtk6-dev
```

```
$ sudo apt install cmake libavcodec-dev libavformat-dev libavutil-dev libboost-dev libdouble-conversion-dev libeigen3-dev libexpat1-dev libfontconfig-dev libfreetype6-dev libgdal-dev libglew-dev libhdf5-dev libjpeg-dev libjsoncpp-dev liblz4-dev liblzma-dev libnetcdf-dev libnetcdf-cxx-legacy-dev libogg-dev libpng-dev libpython3-dev libqt5opengl5-dev libqt5x11extras5-dev libsqlite3-dev libswscale-dev libtheora-dev libtiff-dev libxml2-dev libxt-dev qtbase5-dev qttools5-dev zlib1g-dev
```

**Step 1**

Go to `LIGGGHTS-PUBLIC > src` directory 

```
$ make auto
```
If it doesn't compile and says that some thing is missing  then run the following command:

```
$ make makeshlib
$ make auto
```

`Note: If vtk , mpi are not installed before compiling, then we have to change required lines in makefile`


In `src` directory:

```
$ gedit MAKE/Makefile.user
```

**Step2**


```
$ make -f Makefile.shlib auto
```
**Step3**

Now we can install required setup for python file.

Go to `LIGGGHTS-PUBLIC - pyhton`

Based on `install.py` file in `python` folder

run the follwing command:

```
$ sudo python install.py ~/.local/lib ~/.local/lib/python3.8/site-packages/
```

or 

If all the packages and path are correct then just run:

```
$ sudo python install.py
```


It might say that `LD_LIBRARY` path can't check because of different python version.

 so it's better to add `LD_Library` path in bash file

```
$ sudo gedit ~/../../etc/bash.bashrc
```
add the following line at the last of the bashrc file

` export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/LIGGGHTS-PUBLIC/lib/vtk/install/lib/`

then repeat `step3`



 Use LIGGGHTS
 ===================

 In `src` directory, run:

 ```
 $ ipython
 ```

python shell will apeared.


Then follow the given steps inside of shell:

```
In [2] : import liggghts
In [3] : liggghts # This line will show liggghts path
In [4] : dem = liggghts.liggghts()                                               

# this will be the output, if not then LD_library path is not setup properly

LIGGGHTS (Version LIGGGHTS-PUBLIC 3.8.0, compiled 2020-10-29-19:31:46 by vision, git commit 3b38a7dbe22018f905d4c5f792ab5ce644ef594e)

In [5]: dem.command('atom_style granular')  

# change the directory based on input file. I am using example that comes with LIGGGHT. 

In [6]: 
In [7]: cd /home/vision/my_project/project/LIGGGHTS-PUBLIC/examples/LIGGGHTS/Tutorials_public/insert_stream  
  
# we can see following files;

In [8]: ls                                                                      
in.insert_stream  in.insert_stream_reset_timestep  meshes/  post/  postscript*

# to run the simulation, we need `in.insert_stream` file.So:

In [9]: dem.file('in.insert_stream') 

If everything is okay, then we can see training 
```


