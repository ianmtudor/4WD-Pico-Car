import pico_4wd as car
import time
import math

MOTOR_POWER = 100
car.GRAYSCALE_LINE_REFERENCE = 700
angle = -15
testSeconds = 30

def main():
    car.set_light_bottom_color([255,255,255])
    #car.set_light_rear_color([200,0,0])
    #distance = car.sonar.get_distance()
    distance = car.get_radar_distance_at(angle)
    print(distance, type(distance))
    
    timeout = time.time() + testSeconds
    
    #to remove timer, set to "while True:"
    while time.time() < timeout:    
    #while True:
        #distance = car.sonar.get_distance()
        distance = car.get_radar_distance_at(angle)
        car.set_light_rear_color([15,0,0])
        gs_data = car.get_greyscale_status()
        grayValue = car.get_grayscale_values()
        print('left:%d, middle:%d, right:%d' %(grayValue[0], grayValue[1], grayValue[2]))
        print(distance)
        
        if math.isclose(distance, 15) or (distance < 15):
        #if distance < 20:
            #car.set_light_rear_color([255,0,0])
            car.set_light_rear_color([255,0,0])
            #car.set_motor_power(0, 0, 0, 0)
            car.move("stop")
            print("stopped")
            time.sleep(2)
            
        elif math.isclose(distance, 60) or (distance < 60):
        #if distance < 20:
            MOTOR_POWER = 20
            car.set_light_rear_color([0,0,255])
            #car.set_light_rear_color([20,0,0])
            
        else:
            MOTOR_POWER = 100
            car.set_light_rear_color([0,255,0])
            
        if gs_data == [0, 1, 0]:
            car.set_motor_power(MOTOR_POWER, MOTOR_POWER, MOTOR_POWER, MOTOR_POWER)
            print('middle: ', grayValue[1])
            #car.set_light_bottom_color([0, 100, 0])
        elif gs_data == [0, 1, 1]:
            car.set_motor_power(MOTOR_POWER, 0, MOTOR_POWER, 0)
            #car.set_light_off()
            #car.set_light_bottom_left_color([50, 50, 0])
        elif gs_data == [0, 0, 1]:
            car.set_motor_power(MOTOR_POWER, -MOTOR_POWER, MOTOR_POWER, -MOTOR_POWER)
            #car.set_light_off()
            #car.set_light_bottom_left_color([100, 5, 0])
        elif gs_data == [1, 1, 0]:
            car.set_motor_power(0, MOTOR_POWER, 0, MOTOR_POWER)
            #car.set_light_off()
            #car.set_light_bottom_right_color([50, 50, 0])
        elif gs_data == [1, 0, 0]:
            car.set_motor_power(-MOTOR_POWER, MOTOR_POWER, -MOTOR_POWER, MOTOR_POWER)
            #car.set_light_off()
            #car.set_light_bottom_right_color([100, 0, 0])
try:
    time.sleep(3)
    main()
finally:
    car.move("stop")
    car.set_light_off()

def get_distance(self):
    self.trig.low()
    time.sleep(0.01)
    self.trig.high()
    time.sleep(0.000015)
    self.trig.low()
    pulse_end = 0
    pulse_start = 0
    timeout_start = time.time()
    while self.echo.value()==0:
        pulse_start = time.time()
        if pulse_start - timeout_start > self.timeout:
            return -1
    while self.echo.value()==1:
        pulse_end = time.time()
        if pulse_end - timeout_start > self.timeout:
            return -2
    during = pulse_end - pulse_start
    cm = round(during * 340 / 2 * 100, 2)
    print(cm)
    return cm
