#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
from turtlesim.msg import Pose
from turtlesim.srv import TeleportAbsolute, SetPen
import math
 
class DrawD:
    def __init__(self):
        rospy.init_node('draw_digits', anonymous=False)
        self.v = Twist()
        self.pi = 3.1416
        self.pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(20)
        self.x = 0
        self.y = 0
        self.theta = 0

        # Spawn turtle 
        rospy.wait_for_service('spawn')
        spawn_turtle = rospy.ServiceProxy('spawn', Spawn)
        #self.pen_up()
        spawn_turtle(2.5, 4.5, 0, 'turtle2')

        # Teleport initializer
        rospy.wait_for_service('/turtle2/teleport_absolute')
        teleport_turtle = rospy.ServiceProxy('/turtle2/teleport_absolute', TeleportAbsolute)


        # Digit 2
        self.pen_down()
        self.face_east()
        self.move_forward(20)
        self.face_south()
        self.move_forward(15)
        self.face_west()
        self.move_forward(20)
        self.face_south()
        self.move_forward(15)
        self.face_east()
        self.move_forward(20)
        self.halt()

        # Digit 9
        self.pen_up()
        teleport_turtle(5.5, 3.7, 3)
        self.pen_down()
        self.face_west()
        self.move_forward(20)
        self.face_north()
        self.move_forward(15)
        self.face_east()
        self.move_forward(20)
        self.face_south()
        self.move_forward(32)
        self.face_west()
        self.move_forward(20)
        self.halt()

        # Digit 4
        self.pen_up()
        teleport_turtle(6.5, 4.5, 5)
        self.pen_down()
        self.face_south()
        self.move_forward(15)
        self.face_east()
        self.move_forward(20)
        self.face_north()
        self.move_forward(15)
        self.move_back(30)
        self.halt()
        rospy.spin()

    def pen_down(self):
        rospy.wait_for_service('/turtle2/set_pen')
        set_pen = rospy.ServiceProxy('/turtle2/set_pen', SetPen)
        set_pen(200,190,105,0,0)
        
    def pen_up(self):
        rospy.wait_for_service('/turtle2/set_pen')
        set_pen = rospy.ServiceProxy('/turtle2/set_pen', SetPen)
        set_pen(99,102,106,0,0)


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
            self.se = rospy.Subscriber('/turtle2/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()
            
        self.v.linear.x = 0
        self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_SW(self):
        while abs(self.theta - (self.pi * 1.25)) > 0.05:
            self.sw = rospy.Subscriber('/turtle2/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()
            
        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_NE(self):
        while abs(self.theta - (self.pi / 4)) > 0.05:
            self.sw = rospy.Subscriber('/turtle2/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()
            
        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_NW(self):
        while abs(self.theta - self.pi * 0.75) > 0.05:
            self.nw = rospy.Subscriber('/turtle2/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()

        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_west(self):
        while abs(self.theta - self.pi) > 0.05:
            self.nw = rospy.Subscriber('/turtle2/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()

        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_north(self):
        while abs(self.theta - (self.pi / 2)) > 0.05:
            self.s1 = rospy.Subscriber('/turtle2/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v) 
            self.rate.sleep()

        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_east(self):
        while abs(self.theta) > 0.08:
            self.s3 = rospy.Subscriber('/turtle2/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()
    
        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_south(self):
        while abs(self.theta + 0.5 * self.pi) > 0.05:
            self.s4 = rospy.Subscriber('/turtle2/pose', Pose, self.pose_callback)
            self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v)
            self.rate.sleep()

    def get_initial_pose(self):
        start = [0, 0]
        count = 0
        while count <= 2:
            self.s2 = rospy.Subscriber('/turtle2/pose', Pose, self.pose_callback)
            start[0] = self.x
            start[1] = self.y
            count += 1
            self.rate.sleep()
            return start


if __name__ == '__main__':

    D = DrawD()
