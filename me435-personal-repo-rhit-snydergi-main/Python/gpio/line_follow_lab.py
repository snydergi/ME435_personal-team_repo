import gpiozero as gz
import time
import signal

def main():
    print("Tank Sensors")
    line_pin_right = 19
    line_pin_middle = 16
    line_pin_left = 20
    # line_sensor_events()
    # line_sensor_states()
    # ultrasonic_distance_sensor()
    follow_line_or_stop()

def follow_line_or_stop():
    print("FOLLOW THAT LINE")
    sensor = gz.DistanceSensor(echo=8,trigger=11)
    right_line_sensor = gz.LineSensor(20)
    middle_line_sensor = gz.LineSensor(16)
    left_line_sensor = gz.LineSensor(19)
    pinRightFWD = gz.DigitalOutputDevice(15)
    pinRightREV = gz.DigitalOutputDevice(14)
    enableRight = gz.PWMOutputDevice(4)
    pinLeftFWD = gz.DigitalOutputDevice(27)
    pinLeftREV = gz.DigitalOutputDevice(18)
    enableLeft = gz.PWMOutputDevice(17)
    while True:
        print('Distance: ', sensor.distance * 100)
        print('LLS :', left_line_sensor.value)
        print('MLS :', middle_line_sensor.value)
        print('RLS :', right_line_sensor.value)
        if sensor.distance * 100 < 10:
            stop(pinLeftFWD,pinLeftREV,enableLeft,pinRightFWD,pinRightREV,enableRight)
        elif middle_line_sensor.value == 1:
                goStraight(pinLeftFWD,pinLeftREV,enableLeft,pinRightFWD,pinRightREV,enableRight)
        elif right_line_sensor.value == 1:
                turnRight(pinLeftFWD,pinLeftREV,enableLeft,pinRightFWD,pinRightREV,enableRight)
        elif left_line_sensor.value == 1:
                turnLeft(pinLeftFWD,pinLeftREV,enableLeft,pinRightFWD,pinRightREV,enableRight)
        time.sleep(0.01)

def stop(lf,lr,le,rf,rr,re):
    lf.off()
    lr.off()
    le.value = 0.0
    rf.off()
    rr.off()
    re.value = 0.0

def goStraight(lf,lr,le,rf,rr,re):
    lf.on()
    lr.off()
    le.value = 1.0
    rf.on()
    rr.off()
    re.value = 1.0

def turnRight(lf,lr,le,rf,rr,re):
    lf.on()
    lr.off()
    le.value = 1.0
    rf.off()
    rr.on()
    re.value = 1.0

def turnLeft(lf,lr,le,rf,rr,re):
    lf.off()
    lr.on()
    le.value = 1.0
    rf.on()
    rr.off()
    re.value = 1.0

def ultrasonic_distance_sensor():
    print("Ultrasonic Distance Sensor")
    sensor = gz.DistanceSensor(echo=8,trigger=11)
    while True:
        print('Distance: ', sensor.distance * 100)
        time.sleep(1)

def line_sensor_states():
    print("Line Sensor States")
    starboard_line_sensor = gz.LineSensor(20)
    middle_line_sensor = gz.LineSensor(19)
    port_line_sensor = gz.LineSensor(16)
    while True:
         print(f"Starboard: {starboard_line_sensor.value} Middle: {middle_line_sensor.value} Port: {port_line_sensor.value}")
         # Black is value 1
         # White is value 2
         time.sleep()

def line_sensor_events():
    print("Line Sensor Events")
    starboard_line_sensor = gz.LineSensor(20)
    starboard_line_sensor.when_line = lambda : print("Starboard White Detected")
    starboard_line_sensor.when_no_line = lambda : print("Starboard Black Detected")

    port_line_sensor = gz.LineSensor(19)
    port_line_sensor.when_line = lambda : print("Port White Detected")
    port_line_sensor.when_no_line = lambda : print("Port Black Detected")

    middle_line_sensor = gz.LineSensor(16)
    middle_line_sensor.when_line = lambda : print("Middle White Detected")
    middle_line_sensor.when_no_line = lambda : print("Middle Black Detected")

    signal.pause()

main()