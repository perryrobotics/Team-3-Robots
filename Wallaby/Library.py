3#!/usr/bin/python
import os, sys
from wallaby import *
Lmotor = 3
Rmotor = 0
    
Arm = 3
Arm_back = 2000
Arm_up = 500
Arm_down = 250
    
Claw = 2
Claw_open = 2000
Claw_close = 1100
    
Box = 0
Box_back = 1100
Box_down = 450

Touch_port = 0
Line_port = 0
Thresh = 3000
    
def move(speed, ticks):
	cmpc(Lmotor)
	mav(Lmotor, speed);
	mav(Rmotor, speed);
	while gmpc(Lmotor) < ticks:
		pass
	ao()
            
def move_back(speed, ticks):
	cmpc(Lmotor)
	mav(Lmotor, -speed);
	mav(Rmotor, -speed);
	while gmpc(Lmotor) > -ticks:
		pass
	ao()

def move_left(speed, ticks):
	cmpc(Rmotor)
  	cmpc(Lmotor)
	mav(Lmotor,-speed)
	mav(Rmotor, speed)
	while gmpc(Rmotor) < ticks:
		pass
	ao()

def move_right(speed, ticks):
	cmpc(Lmotor)
	mav(Lmotor, speed)
	mav(Rmotor, -speed)
	while gmpc(Lmotor) < ticks:
		pass
	ao()
  
def drive_to_black(speed):
	mav(Rmotor, speed)
  	mav(Lmotor, speed)
  	while analog(Line_port) < Thresh:
		pass
	ao()
            
def drive_to_white(speed):
	mav(Rmotor, speed)
  	mav(Lmotor, speed)
  	while analog(Line_port) > Thresh-1000:
		pass
	ao()    
   
def move_to_hit(speed):
	mav(Rmotor, speed)
  	mav(Lmotor, speed)
	while digital(Touch_port) ==0:
		pass
	ao()
            
def right_to_black(speed):
	mav(Lmotor, speed)
	mav(Rmotor, -speed)
	while analog(Line_port) < Thresh:
		pass
	ao()   
            
def move_servo_slow(port, start_pos, end_pos, step):
	if  end_pos < start_pos:
		step=-step
  	for pos in range(start_pos, end_pos, step):
		set_servo_position(port, pos)
		msleep(50)
 	set_servo_position(port, end_pos)
            
##############################            

def arm_back(step):
	move_servo_slow(Arm, get_servo_position(Arm), Arm_back, step)
	msleep(750)
    
def arm_up(step):
	move_servo_slow(Arm, get_servo_position(Arm), Arm_up, step)

def arm_down(step):
	move_servo_slow(Arm, get_servo_position(Arm), Arm_down, step)


#############################


        
def open_claw(step):
	move_servo_slow(Claw, get_servo_position(Claw), Claw_open, step)
   
def close_claw(step):
  	move_servo_slow(Claw, get_servo_position(Claw), Claw_close, step)

        
############################
        
def move_box(position):
	set_servo_position(Box, position)
	msleep(750)
        
def carry_box(step):
	move_servo_slow(Box,get_servo_position(Box), Box_back, step)
        
def down_box(step):
	move_servo_slow(Box,get_servo_position(Box), Box_down, step)