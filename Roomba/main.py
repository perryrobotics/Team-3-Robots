#!/usr/bin/python
import os, sys
from wallaby import *
from createLibrary import *
from effectors import *
from sensors import *
from left_path import *
from right_path import *

#Startup and get into start position
enable_servos()
create_connect()
arm_middle(100)
msleep(5000)
#GO!!!
turn_CCW(100,90)
forward(100, 360)#hit pipe
drive_to_black(150)
turn_CW(150,140)
#Facing pile
arm_up(50)
claw_open(75)
forward(150,325)
arm_down(25)
forward(100,90)
claw_close(50)
#Got pile
#arm_up(50)
arm_back(30)
claw_open(50)
#Pile in start
turn_CW(150,50)
drive_to_bump(150)
forward(150,100)
turn_CW(150,100)
arm_middle(50)
drive_to_black(150) 
turn_CW(150,200)
    
#facing fire station path 1
drive_to_black(150)
arm_down(50)
forward(100,30)
claw_close(50)
arm_middle(50)
turn_CW(150,45)
forward(150,220)
backward(150,50)
right_path()
#left_path()
    
    
    
    
"""    
forward(150,800)
forward(100,280)
CW_to_white(150)
forward(100,280)
CCW_to_black(150)
forward(100,240)
CW_to_white(150)

#forward(100,1140) #go down black line getting pckages
#GRAB LAST PACKAGE
claw_open(150)
turn_CW(50,10)
arm_down(50)
msleep(500)
claw_close(50)
msleep(500)
arm_middle(150)
#GOT IRST POM, NOW GO SCORE THINGS!!
turn_CCW(85,105)
forward(150, 650)
drive_to_black(150)
backward(250,200)
arm_up(50)
claw_open(150) #SCORED ALL POMS!!
#claw_close(150)

turn_CCW(85,90)
backward(150,370)
turn_CW(150,90)
forward(150,450) #hit pipe to align
backward(150,160)
turn_CW(150,90) #facing fire station
#claw_open(150)
arm_down(50)
forward(150,20)
claw_half(50)
arm_middle(50)
turn_CW(150,45)
forward(50,100)
#HERE IS WHERE CAMERA CODE GOES!!!!
#left_path()
"""

    
    
