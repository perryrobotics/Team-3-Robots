#!/usr/bin/python
import os, sys
from wallaby import *
from createLibrary import *
from effectors import *
from sensors import *

def right_path():
    #Firemen path 2

	turn_CW(100, 20)
  	forward(100, 400)
  	arm_down(50)
  	claw_open(50)
	arm_up(50)
 	drive_to_bump(100)

  	"""
    drive_to_black(150)
    arm_down(50)
    forward(100,30)
    claw_close(50)
    arm_middle(50)
    turn_CW(150,67)
    forward(150,500)
    backward(150,50)
    arm_down(50)
    claw_open(50)   
    for x in range(5):
        arm_middle(50)
        turn_CW(150,23)
        turn_CW(150,180)
        forward(150,700)
        backward(50,90)
        turn_CCW(150,90)
        drive_to_black(150)
        turn_CW(150,200)
        arm_down(50)
        forward(50,70)
        claw_close(50)
        backward(50,70)
        arm_middle(50)
        turn_CW(150,67)
        forward(150,700)
        backward(150,50)
        arm_down(50)
        claw_open(50)
	"""