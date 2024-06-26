from servo import Servo
import time
motor1=Servo(pin=13)
motor2=Servo(pin=12)
motor3=Servo(pin=14)
motor4=Servo(pin=27)

def S1():
    motor1.move(10)#Left
    time.sleep(1)
    motor1.move(165)#Right
    time.sleep(1)
def S2():  
    motor2.move(30)#Up
    time.sleep(1)
    motor2.move(90)#Down
    time.sleep(1)
def S3(): #Arm-2nd Servo  
    motor3.move(30)#Forward
    time.sleep(1)
    motor3.move(100)#Backward
    time.sleep(1)
def S4():
    motor4.move(100)#Open
    time.sleep(1)
    motor4.move(130)#Close
    time.sleep(1)

# motor1.move(90)
# motor2.move(90)
# motor3.move(90)
#motor4.move(90)



   
    
# motor2.move(80)
# #motor3.move(50)
# motor4.move(80)
# motor5.move(90)

while(1):# A changer selon la broche utilisée
#     motor1.move(0)
#     time.sleep(1)
#     motor1.move(200)
#     time.sleep(1)

     S1()
#     S2()
#     S3()
#     S4()
#     
    
 