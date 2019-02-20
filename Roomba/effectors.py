#!/usr/bin/python
import os, sys
from wallaby import *
from createLibrary import *
from effectors import *

ARM_PORT = 0
ARM_UP = 600
ARM_MID = 1250
ARM_BACK = 2050
ARM_DOWN = 120
    
CLAW_PORT = 3
CLAW_OPEN = 0
CLAW_CLOSED = 1200
HALF_CLOSE = 750
HALF_OPEN = 600
    
    
def move_servo_slow(port, start, end, step):
	if end < start:
		step = -step
	for pos in range(start, end, step):
		set_servo_position(port, pos)
 		msleep(75)
 	set_servo_position(port, end)
            
def arm_back(step):
	start = get_servo_position(ARM_PORT)
	move_servo_slow(ARM_PORT, start, ARM_BACK,step)
        
def arm_middle(step):
	start = get_servo_position(ARM_PORT)
	move_servo_slow(ARM_PORT, start, ARM_MID,step)

def arm_down(step):
	start = get_servo_position(ARM_PORT)
	move_servo_slow(ARM_PORT, start, ARM_DOWN, step)
        
def arm_up(step):
	start = get_servo_position(ARM_PORT)
	move_servo_slow(ARM_PORT, start, ARM_UP, step)
        
def claw_open(step):
	start = get_servo_position(CLAW_PORT)
	move_servo_slow(CLAW_PORT, start, CLAW_OPEN, step)

def claw_close(step):
	start = get_servo_position(CLAW_PORT)
	move_servo_slow(CLAW_PORT, start, CLAW_CLOSED, step)
        
def claw_half(step):
	start = get_servo_position(CLAW_PORT)
	move_servo_slow(CLAW_PORT, start, HALF_CLOSE, step)

def claw_half_open(step):
	start = get_servo_position(CLAW_PORT)
	move_servo_slow(CLAW_PORT, start, HALF_OPEN, step)