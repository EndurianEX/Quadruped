from motor import Servo
import time
import sys

frontRightFoot = Servo(pin=0)
frontRightHip = Servo(pin=1)
frontLeftFoot = Servo(pin=8)
frontLeftHip = Servo(pin=9)
backRightFoot = Servo(pin=4)
backRightHip = Servo(pin=5)
backLeftFoot = Servo(pin=12)
backLeftHip = Servo(pin=13)

while True:
    v = sys.stdin.readline().split(",")
    FRH_currentAngle = int(v[0])
    FRF_currentAngle = int(v[1])
    FLH_currentAngle = int(v[2])
    FLF_currentAngle = int(v[3])
    BRH_currentAngle = int(v[4])
    BRF_currentAngle = int(v[5])
    BLH_currentAngle = int(v[6])
    BLF_currentAngle = int(v[7])
            
            
    frontRightHip.move(FRH_currentAngle)
    frontRightFoot.move(FRF_currentAngle)
    frontLeftHip.move(FLH_currentAngle)
    frontLeftFoot.move(FLF_currentAngle)
    backRightHip.move(BRH_currentAngle)
    backRightFoot.move(BRF_currentAngle)
    backLeftHip.move(BLH_currentAngle)
    backLeftFoot.move(BLF_currentAngle)
