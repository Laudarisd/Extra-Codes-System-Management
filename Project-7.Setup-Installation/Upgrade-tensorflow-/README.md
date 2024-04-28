# Upgrade-tensorflow-
To upgrade tensorflow, follow following process

- pip3 install --user --upgrade tensorflow


- pip3 install --user --upgrade tensorflow-gpu    # install in gpu

Note: use pip3.
If pip version is not upgraded then upgrade it before upgrading tensorflow
# check pip version 
pip --version  
-to upgrade pip: pip version upgrade sudo -H   
                  pip3 install --upgrade pip   
                  sudo -H pip install --upgrade pip   
                  
                  
                 
-If it throws error while up grading, follow the following process

$ pip3 install --upgrade tensorflow==2.0.0  
$ pip3 install --upgrade tensorflow-gpu==2.0.0 



# Remove Tensorflow completely

**Check tensorflow list in local device**
- `pip list|grep tensorflow`
- After that run the following commands one by one by adding all tensorflow files
  `pip3 uninstall .....`
  
      or 
      
   `sudo pip3 uninstall .......`
   
   
   
# Install tensorflow GPU

`sudo pip3 install tensorflow-gpu==2.0`

**check**

`import tensorflow as tf
tf.test.is_gpu_available(
    cuda_only=False,
    min_cuda_compute_capability=None
)`


or   


`tf.test.is_gpu_available()`




