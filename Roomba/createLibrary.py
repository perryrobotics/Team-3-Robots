#!/usr/bin/python
import os, sys
from wallaby import *
from createLibrary import *
from effectors import *

def forward(speed, distance):
	set_create_distance(0)
 	create_drive_straight(-speed)
 	while get_create_distance() > -distance:
		pass
	create_stop()
        
def backward(speed, distance):
	set_create_distance(0)
 	create_drive_straight(speed)
 	while get_create_distance()< distance:
		pass
	create_stop()
            
def turn_CW(speed, angle):
 	target_angle=get_create_total_angle()-angle
	create_spin_CW(speed)
 	while get_create_total_angle() > target_angle:
		pass
	create_stop()
            
def turn_CCW(speed, angle):
	target_angle=get_create_total_angle()+angle
    
	create_spin_CCW(speed)
	while get_create_total_angle() < target_angle:
		pass
	create_stop()