from motor import Servo
import time
import sys


# setting the servo pins, this may need an update based on robot used
frontRightFoot = Servo(pin=0)
frontRightHip = Servo(pin=1)
frontLeftFoot = Servo(pin=8)
frontLeftHip = Servo(pin=9)
backRightFoot = Servo(pin=4)
backRightHip = Servo(pin=5)
backLeftFoot = Servo(pin=12)
backLeftHip = Servo(pin=13)

# reading sent data from the Quadruped script
while True:
    """
    splits read string into 8 values between 0 and 7 and applies them to 8 abreviated angles for each limb
    F = front
    B = back
    R = right
    L = left
    H = hip
    F = foot

    EXAMPLE:
    FRH = frontRightHip
    """
    
    v = sys.stdin.readline().split(",") 
    FRH_currentAngle = int(v[0])
    FRF_currentAngle = int(v[1])
    FLH_currentAngle = int(v[2])
    FLF_currentAngle = int(v[3])
    BRH_currentAngle = int(v[4])
    BRF_currentAngle = int(v[5])
    BLH_currentAngle = int(v[6])
    BLF_currentAngle = int(v[7])
            
    # Apply angles to the move() function from the motor library
    frontRightHip.move(FRH_currentAngle)
    frontRightFoot.move(FRF_currentAngle)
    frontLeftHip.move(FLH_currentAngle)
    frontLeftFoot.move(FLF_currentAngle)
    backRightHip.move(BRH_currentAngle)
    backRightFoot.move(BRF_currentAngle)
    backLeftHip.move(BLH_currentAngle)
    backLeftFoot.move(BLF_currentAngle)
