#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import Spawn
from turtlesim.srv import TeleportAbsolute, SetPen
import math

class DrawD:
    def __init__(self):
        rospy.init_node('draw_frame', anonymous=False)

        # Spawn service initialization
        rospy.wait_for_service('spawn')
        spawn_turtle = rospy.ServiceProxy('spawn', Spawn)

        self.v = Twist()
        self.pi = 3.1416
        self.pub = rospy.Publisher('/turtle3/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(20)
        self.x = 0
        self.y = 0
        self.theta = 0
        
        # Frame
        spawn_turtle(10.5, 10.5, 4.712, 'turtle3') # Spawn turtle3
        self.face_south()
        self.move_forward(200)
        self.face_west()
        self.move_forward(195)
        self.face_north()
        self.move_forward(195)
        self.face_east()
        self.move_forward(195)

        self.halt()

        rospy.spin()

    def pose_callback(self, msg):
        self.x = msg.x
        self.y = msg.y
        self.theta = msg.theta 

    def halt(self):
        self.v.linear.x = 0
        self.v.angular.z = 0
        self.pub.publish(self.v)

    def move_forward(self, c=0):
        g_count = 0
        while g_count <= c:
            self.v.linear.x = 1.0
            self.v.angular.z = 0
            self.pub.publish(self.v)
            g_count += 1
            self.rate.sleep()

    def face_west(self):
        while abs(self.theta - self.pi) > 0.009:
            self.nw = rospy.Subscriber('/turtle3/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()

        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_north(self):
        while abs(self.theta - self.pi * 0.5) > 0.02498:
            self.s1 = rospy.Subscriber('/turtle3/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v) 
            self.rate.sleep()

        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_east(self):
        while abs(self.theta) > 0.009:
            self.s3 = rospy.Subscriber('/turtle3/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()
    
        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_south(self):
        while abs(self.theta + 0.5 * self.pi) > 0.05:
            self.s4 = rospy.Subscriber('/turtle3/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()

    def get_initial_pose(self):
        start = [0, 0]
        count = 0
        while count <= 2:
            self.s2 = rospy.Subscriber('/turtle3/pose', Pose, self.pose_callback)
            start[0] = self.x
            start[1] = self.y
            count += 1
            self.rate.sleep()
            return start


if __name__ == '__main__':
    # background color 
    D = DrawD()

