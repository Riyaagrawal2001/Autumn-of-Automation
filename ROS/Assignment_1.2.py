#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def move(distance):
	speed = 20
	isForward = True

	vel_msg.linear.x = abs(speed)
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0

	
	t0 = rospy.Time.now().to_sec()
	current_distance = 0

	while(current_distance < distance):
		velocity_publisher.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		current_distance = speed*(t1-t0)

	vel_msg.linear.x = 0
	velocity_publisher.publish(vel_msg)

def rotate(angle):
	speed = 5
	clockwise = True

	angular_speed = speed*2*PI/360
	relative_angle = angle*2*PI/360

	vel_msg.linear.x = 0
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0

	vel_msg.angular.z = -abs(angular_speed)

	t0 = rospy.Time.now().to_sec()
	current_angle = 0

	while(current_angle < relative_angle):
		velocity_publisher.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		current_angle = angular_speed*(t1-t0)

	vel_msg.angular.z = 0
	velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
	rospy.init_node('robot_cleaner', anonymous=True)
    	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    	vel_msg = Twist()
    	rotate(90)
        move(2)
	rotate(180)
    	move(4)
    	rotate(90)
    	move(2)
    	rotate(90)
    	move(2)
    	rotate(90)
    	move(2)
    	rotate(225)
    	move(2)
