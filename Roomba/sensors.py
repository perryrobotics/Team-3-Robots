#!/usr/bin/python
import os, sys
from wallaby import *
from createLibrary import *
from effectors import *

TOP_HAT_CENTER = 0
TOP_HAT_LEFT = 1
TOP_HAT_RIGHT = 0

THRESH= 2500
THRESH_CENTER = 2500
    
def drive_to_black(speed):
	create_drive_straight(speed)
	while analog(TOP_HAT_CENTER) < THRESH_CENTER:
		pass
	create_stop()

def drive_to_white(speed):
	create_drive_straight(speed)
  	while analog(TOP_HAT_CENTER) > THRESH_CENTER:
		pass
	create_stop()
            
def drive_to_bump(speed):
	create_drive_straight(speed)
  	while get_create_lbump() == 0 and get_create_rbump() == 0:
		pass
 	create_stop()

def drive_to_white(speed):
    create_drive_straight(speed)
    while analog(TOP_HAT_CENTER) > THRESH_CENTER:
        pass
    create_stop()

def CW_to_black(speed):
	create_spin_CW(speed)
	while analog(TOP_HAT_CENTER) < THRESH_CENTER:
		pass
	create_stop()
            
def CCW_to_black(speed):
	create_spin_CCW(speed)
	while analog(TOP_HAT_CENTER) < THRESH_CENTER:
		pass
	create_stop()
            
def CW_to_white(speed):
	create_spin_CW(speed)
	while analog(TOP_HAT_CENTER) > THRESH_CENTER:
		pass
	create_stop()
            
def CCW_to_white(speed):
	create_spin_CCW(speed)
	while analog(TOP_HAT_CENTER) > THRESH_CENTER:
		pass
	create_stop()
            
def line_follow(distance):	
	set_create_distance(0)
  	while get_create_distance()<distance:
		if analog(TOP_HAT_LEFT) > THRESH:
			create_drive_direct(-100, -75)
		elif analog(TOP_HAT_RIGHT) > THRESH:
			create_drive_direct(-75, -100)
 		else:
			create_drive_straight(-100)
	create_stop()
		 