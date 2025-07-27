#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import Spawn
from turtlesim.srv import TeleportAbsolute, SetPen
from std_srvs.srv import Empty, EmptyResponse
import math

class PenColor:
    def pen_down(self):
        rospy.wait_for_service('/turtle1/set_pen')
        set_pen = rospy.ServiceProxy('/turtle1/set_pen', SetPen)
        set_pen(200,190,105,1,0)
        
    def pen_up(self):
        rospy.wait_for_service('/turtle1/set_pen')
        set_pen = rospy.ServiceProxy('/turtle1/set_pen', SetPen)
        set_pen(99,102,106,0,0)

class Draw:
    def __init__(self):
        rospy.init_node('draw_N', anonymous=False)
        p = PenColor()

        # initial position
        rospy.wait_for_service('/turtle1/teleport_absolute')
        teleport_turtle = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)

        self.v = Twist()
        self.pi = 3.1416
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(20)
        self.x = 0
        self.y = 0
        self.theta = 0
        
        # changing bg_colour
        rospy.set_param('/turtlesim/background_r', 99)
        rospy.set_param('/turtlesim/background_g', 102)
        rospy.set_param('/turtlesim/background_b', 106)

        # letter A
        p.pen_up()
        teleport_turtle(1.5, 7, 10)
        p.pen_down()
        self.face_NE()
        self.move_forward(40)
        self.face_SE()
        self.move_forward(40)
        self.move_back(20)
        self.face_west()
        self.move_forward(35)
        self.halt()

        # letter B
        p.pen_up()
        teleport_turtle(4.5, 7, 10)
        p.pen_down()
        self.face_north()
        self.move_forward(30)
        self.face_east()
        self.clockwise(60)
        self.face_east()
        self.clockwise(60)
        self.halt()

        # letter N
        p.pen_up()
        teleport_turtle(5.5, 7, 10)
        p.pen_down()
        self.face_north()
        self.move_forward(30)
        self.face_SE()
        self.move_forward(40)
        self.face_north()
        self.move_forward(30)
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

    def clockwise(self, c=0):
        g_count = 0
        while g_count <= c:
            self.v.linear.x = 0.39
            self.v.angular.z = -1.0
            self.pub.publish(self.v)
            g_count += 1
            self.rate.sleep()

    def counter_clockwise(self, c=0):
        g_count = 0
        while g_count <= c:
            self.v.linear.x = 1.0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            g_count += 1
            self.rate.sleep()

    def move_forward(self, c=0):
        g_count = 0
        while g_count <= c:
            self.v.linear.x = 1.0
            self.v.angular.z = 0
            self.pub.publish(self.v)
            g_count += 1
            self.rate.sleep()

    def move_back(self, c=0):
        g_count = 0
        while g_count <= c:
            self.v.linear.x = -1.0
            self.v.angular.z = 0
            self.pub.publish(self.v)
            g_count += 1
            self.rate.sleep()

    def face_SE(self):
        while abs((self.theta + self.pi * 0.25)) > 0.05:
            self.se = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()
            
        self.v.linear.x = 0
        self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_SW(self):
        while abs(self.theta - (self.pi * 1.25)) > 0.05:
            self.sw = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()
            
        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_NE(self):
        while abs(self.theta - (self.pi / 4)) > 0.05:
            self.sw = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()
            
        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_NW(self):
        while abs(self.theta - self.pi * 0.75) > 0.05:
            self.nw = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()

        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_west(self):
        while abs(self.theta - self.pi) > 0.05:
            self.nw = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()

        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_north(self):
        while abs(self.theta - (self.pi / 2)) > 0.05:
            self.s1 = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v) 
            self.rate.sleep()

        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_east(self):
        while abs(self.theta) > 0.08:
            self.s3 = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()
    
        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_south(self):
        while abs(self.theta + 0.5 * self.pi) > 0.05:
            self.s4 = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()

    def get_initial_pose(self):
        start = [0, 0]
        count = 0
        while count <= 2:
            self.s2 = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
            start[0] = self.x
            start[1] = self.y
            count += 1
            self.rate.sleep()
            return start


if __name__ == '__main__':
    D = Draw()

