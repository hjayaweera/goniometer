#!/usr/bin/env python3
from goniometer_lib_1 import *
protocole_file_name="file2.csv"
sample_name="test"
#####################################################
BP=init_motors()
camera = init_cam()
protocole=read_csv(protocole_file_name)
path1=make_folder(sample_name)
save_csv(path1,protocole)
fileNameSufix=0
welcome()
for d in protocole:
    print("Exposure {} ms, ISO {}, light source {} polarizer {} sample {}".format(d[0],d[1],d[2],d[3],d[4]))
    led(BP,int(d[2]))
    polarizer(BP,int(d[3]))
    sample(BP,int(d[4]))
    sleep(.1)
    capture_cam(camera, int(d[0]),int(d[1]),path1+sample_name+"{:04d}.bmp".format(fileNameSufix))
    fileNameSufix=fileNameSufix+1
print("Finished, the files are saved in "+path1)
camera.close()
