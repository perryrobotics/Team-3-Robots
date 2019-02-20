#!/usr/bin/python
import os, sys
from wallaby import *
from createLibrary import *
from effectors import *
from sensors import *

def left_path():
	arm_down(50)
	claw_open(50)
    #getting firemen path 1 
 	for x in range(5):
  		arm_middle(50)
 		turn_CCW(150,(45-(3*x)))
 		claw_open(50)
 		arm_down(50)
 		forward(150,70)
		claw_close(50)
 		backward(150,70)
		turn_CW(150,(45-(3*x)))
 		claw_half_open(50)
 	#securing points
 	arm_middle(50)
 	claw_close(50)
  	turn_CCW(150,20)
 	arm_down(50)
 	turn_CW(150,15)
  	turn_CCW(150,50)
 	backward(150,130)
 	turn_CW(150,90)
 	forward(150, 170)
 	turn_CCW(150,35)