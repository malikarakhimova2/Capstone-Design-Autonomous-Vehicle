# Lane Tracing in Gazebo Simulation Using Image Processing
This project implements an autonomous lane tracing system in a Gazebo simulation environment using ROS. It uses image processing techniques for lane detection, traffic light recognition, and sign recognition, enabling a TurtleBot3 to navigate a predefined map and complete mission objectives such as parking and obstacle avoidance.

## Features

- Lane Detection using color filtering and perspective transformation.
- Traffic Light Detection for stop-and-go control.
- Sign Recognition for navigation decisions.
- Obstacle Handling to avoid collisions.
- ROS Integration for real-time control in Gazebo simulation.

## Implementation Details

- Visual Sensing: Implemented using OpenCV and ROS image topics
- Camera Calibration: Adjusted using intrinsic and extrinsic calibration for accurate perception
- Control Logic: Lane following achieved by adjusting linear and angular velocity based on image feedback
- Packages Used: [TurtleBot3 AutoRace](https://github.com/ROBOTIS-GIT/turtlebot3_autorace_2020) as the base framework

