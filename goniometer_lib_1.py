#!/usr/bin/env python3
from time import sleep, strftime
import os
from picamera import PiCamera
from datetime import datetime
from csv import reader,writer
import brickpi3

def init_motors():
    BP=brickpi3.BrickPi3()

    BP.set_motor_limits(BP.PORT_D, 60, 720)
    BP.set_motor_limits(BP.PORT_B, 60, 720)
    BP.set_motor_limits(BP.PORT_C, 60, 720)
    
    BP.set_motor_position(BP.PORT_D, 0)
    BP.set_motor_position(BP.PORT_B, 0)
    BP.set_motor_position(BP.PORT_C, 0)
    return BP
  
def sample(BP,angle):
    BP.set_motor_position(BP.PORT_B, angle*3.0)

def polarizer(BP,angle):
    BP.set_motor_position(BP.PORT_D, angle*3.75)
    
def led(BP,angle):
    BP.set_motor_position(BP.PORT_C, angle*(140.0/12.0))
    
def read_csv(file_name):
    csvfile1= open(file_name,'r', newline='')
    reader1 = reader(csvfile1,dialect='excel')
    rows=[]
    for row in reader1:
        rows.append(row)
    return rows 

def make_folder(sample_name):
    dir_name=sample_name+"_"+strftime("%Y%m%d_%H%M%S")
    os.makedirs(dir_name)
    return os.getcwd()+os.sep+dir_name+os.sep

def save_csv(folder,matrix):
    csvfile2=open(folder+'protocole.csv','w', newline='')
    writer2=writer(csvfile2)
    for row in matrix:
        writer2.writerow(row)
    csvfile2.close()

def read_csv(file_name):
    csvfile1= open(file_name,'r', newline='')
    reader1 = reader(csvfile1,dialect='excel')
    rows=[]
    for row in reader1:
        rows.append(row)
    return rows 

def my_delay(seconds):
    animation = "|/-\\"
    idx = 0
    while idx<seconds*10:
        print(animation[idx % len(animation)], end="\r")
        idx += 1
        sleep(0.1)

def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
           ______ _____ _____ _   _                                            
     /\   |  ____/ ____|_   _| \ | |                                           
    /  \  | |__ | (___   | | |  \| |                                           
   / /\ \ |  __| \___ \  | | | . ` |                                           
  / ____ \| |    ____) |_| |_| |\  |                                           
 /_/____\_\_|   |_____/|_____|_| \_|        _              ____       _        
  / ____|           (_)                    | |            |  _ \     | |       
 | |  __  ___  _ __  _  ___  _ __ ___   ___| |_ ___ _ __  | |_) | ___| |_ __ _ 
 | | |_ |/ _ \| '_ \| |/ _ \| '_ ` _ \ / _ \ __/ _ \ '__| |  _ < / _ \ __/ _` |
 | |__| | (_) | | | | | (_) | | | | | |  __/ ||  __/ |    | |_) |  __/ || (_| |
  \_____|\___/|_| |_|_|\___/|_| |_| |_|\___|\__\___|_|    |____/ \___|\__\__,_|

""")
def init_cam():
    camera = PiCamera()
    camera.resolution =(1024, 768)#(3280, 2464)#(1024, 768)
    camera.framerate = 1
    camera.awb_mode ='off'
    camera.awb_gains =(1,1)  #(red,blue) values in between 0.8 and 9 
    camera.drc_strength="off" #dynamic range compression
    camera.exposure_mode="off"
    camera.iso =800 #[100, 200, 320, 400, 500, 640, 800]
    camera.exif_tags['IFD0.Copyright'] = 'Copyright (c) 2019 AFSIN'
    return camera

def capture_cam(camera, shutter, iso, fileName):
    camera.start_preview()
    #my_delay(0.1)#sleep(.1)
    camera.shutter_speed = shutter
    camera.capture(fileName,format="bmp",use_video_port =False,bayer=True)
    #my_delay(1)#sleep(1)
    camera.capture(fileName,format="bmp",use_video_port =False,bayer=True )
    my_delay(2)#sleep(2)
    print("File saved: "+fileName)



