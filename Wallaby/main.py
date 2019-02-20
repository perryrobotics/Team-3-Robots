#!/usr/bin/python
import os, sys
from wallaby import *
from Library import *

#start and get into start position
enable_servos()
arm_back(20)
open_claw(20)
carry_box(100)
msleep(2000)
#into start position!  GO!!
shut_down_in(120)
#print("START!!!")    
drive_to_black(900)
drive_to_white(900)
drive_to_black(900)
move_left(900,900)
print("DONE!!!")
#to hospital
drive_to_black(900)  
move_right(900, 700)

#getting 1st ball
arm_down(20)
move(900,450)
move_right(300,100)
close_claw(35)
move_back(900, 150)
arm_back(50)
open_claw(50)

#next set of balls
move_right(700,300)
move(900,750)
arm_down(50)
move(900,400)
move_right(150,250)
msleep(1000)
close_claw(50)
arm_back(50)
open_claw(50)
    
#set 3 of balls
print("here")
move_right(900,1)
print("now here")
arm_up(50)
move(900,2000)
arm_down(50)
close_claw(50)
move_right(1000,20)
arm_back(50)
open_claw(50)
    
#set 4
move(900,2600)
move_left(450,50)
arm_down(50)
move_right(450,150)
close_claw(50)
arm_back(50)
open_claw(50)

#final set
print("final")
move(900,2100)
move_left(900,30)
arm_down(50)
move(900,700)
close_claw(50)
arm_back(50)
open_claw(50)

#going to dump balls
move_right(990,100)
move_to_hit(900)
move(900,100)
move_back(900,100)
move_right(900,950)
move_back(900,2000) 
drive_to_black(900)
msleep(100)
drive_to_white(900)
msleep(100)
print("I didnt skip")
drive_to_black(900)
move_right(900,900)
right_to_black(900)
#dumping
arm_up(50)
move_left(900,450)
move(900,200)
down_box(40)
for _ in range(20):
	print("vibrate!!!")
	set_servo_position(Box, 530)
  	msleep(100)
  	set_servo_position(Box, 450)
	msleep(100)
carry_box(50)
move(900,200)
arm_back(50)
move_right(900,1700)
move_back(900,1500)
close_claw(50)
arm_down(50)
move_right(600, 375)
arm_back(50)
open_claw(50)
arm_down(50)
move_right(900,100)
move(900,1100)
#electric lines
arm_back(50)
move_left(900,700)
move_back(900,200)
set_servo_position(3,1000)
msleep(500)
move(900,200)
move_right(500,500)

  
        
        
        
        
        
        
        
        
        