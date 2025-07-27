import rospy
from turtlesim.msg import Pose
from turtlesim.srv import Spawn

rospy.init_node('my_initials')

rospy.wait_for_service('spawn')
spawn_turtle = rospy.ServiceProxy('spawn', Spawn)
spawn_turtle(10.5, 10.5, 4.75, 'my_turtle1')

class MyTurtle:
    def __init__(self):
        self.pose = Pose()
        rospy.Subscriber('my_turtle5/pose', Pose, self.update_pose)

    def update_pose(self, data):
        self.pose = data
        self.theta = data.theta
        self.pi = 3.141592653589793

    def move(self):
        if abs(self.theta - self.pi * 0.75) < 0.1:
            # Face south-east
            turn_angle = self.pi * 0.25
            print(f"Turning {turn_angle} radians counterclockwise")
            # Code to turn the turtle goes here
        else:
            # Move forward
            print("Moving forward")
            # Code to move the turtle forward goes here
