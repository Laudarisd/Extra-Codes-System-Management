import os



os.chdir('./exp67')


i=1



for file in os.listdir():
    src=file
    dst= str(i)+".png"
    os.rename(src,dst)
    i+=1
