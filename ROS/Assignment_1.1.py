#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import String

from beginner_tutorials.msg import quaternions
from beginner_tutorials.msg import angles

def callback(data):
	w = data.w
	x = data.x
	y = data.y
	z = data.z
	ysqr = y * y
	zsqr = z * z
	xsqr = x * x

    	t0 = +2.0 * (w * x + y * z)
    	t1 = +1.0 - 2.0 * (x * x + ysqr)
    	X = np.degrees(np.arctan2(t0, t1))

    	t2 = +2.0 * (w * y - z * x)
    	t2 = np.where(t2>+1.0,+1.0,t2)
    	#t2 = +1.0 if t2 > +1.0 else t2

    	t2 = np.where(t2<-1.0, -1.0, t2)
    	#t2 = -1.0 if t2 < -1.0 else t2
    	Y = np.degrees(np.arcsin(t2))

    	t3 = +2.0 * (w * z + x * y)
    	t4 = +1.0 - 2.0 * (ysqr + z * z)
    	Z = np.degrees(np.arctan2(t3, t4))

        pub = rospy.Publisher('topic2', angles, queue_size=10)

        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
        	msg = angles()

        	msg.roll = X
        	msg.pitch = Y
        	msg.yaw = Z

        	pub.publish(msg)
        	rate.sleep()


def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("topic1", quaternions, callback)

	rospy.spin()

if __name__ =='__main__':

	listener()
