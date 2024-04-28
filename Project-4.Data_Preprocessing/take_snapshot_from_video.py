#take snapshot from a video
#install opencv


#import library

import cv2
import os
import time



#Read the video from local pc
video = cv2.VideoCapture('./11.mp4')

save_path = "./snapshots/"
try:
    if not os.path.exists(save_path):
        os.mkdir(save_path)
        
except OSError:
    print("Error: Problem while creating save path")
    
    
#frame

currentframe = 0


while(True):
    time.sleep(5) # take snapshot every after 20 seconds
    # read from frame
    ret, frame = video.read()
    
    if ret:
        # if video is stillleft continue creating images
        name = save_path + str(currentframe) + ".jpg"
        print("Creating ..." + name)
    #writing the extracted images
        cv2.imwrite(name, frame)
        
        currentframe += 1
        
    else:
        break
        
        
        
video.release()
cv2.destroyAllWindows()
    
