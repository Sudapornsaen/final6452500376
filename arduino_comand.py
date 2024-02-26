#!/usr/bin/env python3

from tkinter import *
import rospy
from std_msgs.msg import Int16

rospy.init node('arduino_comand')
rate = rospy.Rate(10)
rate.sleep()

pub = rospy.Publisher("pushed", Int16, queue_size = 10)

def Talker(val):
	cmd_val = Int16(val) 
	rospy.loginfo(cmd_val)
	pub.publish(cmd_val)

B1 = Button(frame, text = "ON", command = lambda: Talker(1))
B1.pack()
B1 = Button(frame, text = "OFF", command = lambda: Talker(0))
B1.pack()

frame.mainloop()
