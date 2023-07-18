import RPi.GPIO as GPIO
import time
import gps
import cv2

# Set up GPIO pins 
servo_pin = 12
motor_pin = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(motor_pin, GPIO.OUT)

# Set up GPS and OpenCV
gpsd = gps.gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
cap = cv2.VideoCapture(0)
bgsub = cv2.createBackgroundSubtractorMOG2()

# Motor functions
def drive_motor(direction):
  if direction == FORWARD:
    GPIO.output(motor_pin, GPIO.HIGH)
  elif direction == BACKWARD:
    GPIO.output(motor_pin, GPIO.LOW)
  else:
    GPIO.output(motor_pin, GPIO.LOW) # STOP
  
# Servo functions
def steer_servo(angle):
  duty_cycle = (angle / 18) + 2
  GPIO.output(servo_pin, GPIO.HIGH)
  time.sleep(duty_cycle)
  GPIO.output(servo_pin, GPIO.LOW)
  
# OpenCV obstacle detection  
def detect_obstacle():
  frame = get_video_frame()
  fgmask = bgsub.apply(frame)

  contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  obstacles = []
  for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 500:
      obstacles.append(cnt)

  if len(obstacles) > 0:
    return True
  else: 
    return False

# Avoid obstacle
def avoid_obstacle():
  
  drive_motor(BACKWARD)
  time.sleep(1)
  
  steer_servo(90)
  time.sleep(0.5)

  drive_motor(FORWARD)
  time.sleep(1)
  
# Define navigation function
def navigate(coord1, coord2, coord3, coord4):

  report = gpsd.next()
  current_lat = report['lat']
  current_lon = report['lon']

  path = [coord1, coord2, coord3, coord4]

  for next_coord in path:
  
    next_lat = next_coord[0]
    next_lon = next_coord[1]

    # Calculate bearing    
    bearing = calc_bearing(current_lat, current_lon, next_lat, next_lon)
   
    # Steer servo & drive motor
    steer_servo(bearing)
    drive_motor(FORWARD)

    # Update current location
    current_lat = next_lat
    current_lon = next_lon

    # Avoid obstacles if detected
    if detect_obstacle():
      avoid_obstacle()

  drive_motor(STOP)

# Example coordinates  
coord1 = (45.51, -122.67)
coord2 = (45.52, -122.68) 
coord3 = (45.53, -122.69)
coord4 = (45.54, -122.70)

# Run navigation 
navigate(coord1, coord2, coord3, coord4)
