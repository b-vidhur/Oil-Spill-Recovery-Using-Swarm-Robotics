# Oil-Spill-Recovery-Using-Swarm-Robotics
This project uses a Raspberry Pi to control an autonomous boat using GPS waypoint navigation and OpenCV obstacle avoidance.
Slideshow Link: https://docs.google.com/presentation/d/1TNRVQgga95SjSYI0z23x8nXT5OPPlpjpX_dsgEiv3xM/edit?usp=sharing

PATENT PENDING (Full reasearch paper and code will be released pending approval of patent)

# Hardware
Raspberry Pi
GPIO pins for motor and servo control
Motor driver for propulsion motor
RC servo for steering
GPS module
Pi camera for OpenCV
Water sensor

# Software
Python 3
RPi.GPIO
gps
OpenCV

Custom Python modules:
- motor.py - motor control functions
- servo.py - servo control functions
- opencv.py - OpenCV obstacle detection
- navigate.py - main navigation script

# Usage
To run the boat:
Configure waypoints in navigate.py
Run:
<!---->
Copy code
python navigate.py
This will start the navigation routine to the defined waypoints while avoiding obstacles.

# Navigation
The navigate() function handles the core navigation logic:
Get current GPS position
Calculate bearing to next waypoint
Control servo to steer
Drive motor forward
Use OpenCV to detect and avoid obstacles
Obstacle Avoidance
opencv.py contains functions to detect obstacles using OpenCV and background subtraction.
If an obstacle is detected, the avoid_obstacle() function will reverse, turn, and go around the obstacle.

# To Do
Add smoothing to steering
Integrate mapping and path planning
Improve obstacle avoidance technique
