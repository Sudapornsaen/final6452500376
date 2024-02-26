#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

frame = Tk()
frame.title("REMOTE")
frame.geometry("200x300")

rospy.init_node("Remote")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)
pub2 = rospy.Publisher("chatter",String,queue_size=10)


# Initial ROS node and determine Publish or Subscribe action

def fw():
	print("fw")
	cmd = Twist()
	cmd.linear.x = 1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	pub2.publish("fw")
def bw():
	print("bw")
	cmd = Twist()
	cmd.linear.x = -1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	pub2.publish("bw")
def ll():
	print("ll")
	cmd = Twist()
	cmd.linear.y = 0
	cmd.angular.z= 1
	pub.publish(cmd)
	pub2.publish("ll")
def rr():
	print("rr")
	cmd = Twist()
	cmd.linear.y = 0
	cmd.angular.z= -1
	pub.publish(cmd)
	pub2.publish("rr")
def po():
	print("po")
	cmd = Twist()
	cmd.linear.y = 0
	cmd.angular.z= -1
	pub.publish(cmd)
	pub2.publish("po")
def pf():
	print("pf")
	cmd = Twist()
	cmd.linear.y = 0
	cmd.angular.z= -1
	pub.publish(cmd)
	pub2.publish("pf")

    

B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=20)

B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=130)

B3 = Button(text = "LL", command=ll)
B3.place(x=20, y=80)

B4 = Button(text = "RR", command=rr)
B4.place(x=128, y=80)

B5 = Button(text = "PO", command=rr)
B5.place(x=73, y=180)

B6 = Button(text = "PF", command=rr)
B6.place(x=73, y=230)

frame.mainloop()  
