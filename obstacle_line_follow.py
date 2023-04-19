import pico_4wd as car
import time
import math

MOTOR_POWER = 100
car.GRAYSCALE_LINE_REFERENCE = 700
angle = -15
testSeconds = 30

def main():
    car.set_light_bottom_color([255,255,255])
    
    timeout = time.time() + testSeconds
    
    #to remove timer, set to "while True:"
    while time.time() < timeout:    
    #while True:
        distance = car.get_radar_distance_at(angle)
        print('left:%d, middle:%d, right:%d' %(grayValue[0], grayValue[1], grayValue[2]))
        print(distance)
        
        if math.isclose(distance, 15) or (distance < 15):
            car.set_light_rear_color([255,0,0])
            car.move("stop")
            print("stopped")
            continue 

        elif math.isclose(distance, 60) or (distance < 60):
            MOTOR_POWER = 20
            car.set_light_rear_color([0,0,255])
            
        else:
            MOTOR_POWER = 100
            car.set_light_rear_color([0,255,0])

        gs_data = car.get_greyscale_status()
        grayValue = car.get_grayscale_values()
        line_detection(MOTOR_POWER,gs_data,grayValue)


def line_detection(MOTOR_POWER,gs_data,grayValue):
    if gs_data == [0, 1, 0]:
        car.set_motor_power(MOTOR_POWER, MOTOR_POWER, MOTOR_POWER, MOTOR_POWER)
        print('middle: ', grayValue[1])
        
    elif gs_data == [0, 1, 1]:
        car.set_motor_power(MOTOR_POWER, 0, MOTOR_POWER, 0)
    elif gs_data == [0, 0, 1]:
        car.set_motor_power(MOTOR_POWER, -MOTOR_POWER, MOTOR_POWER, -MOTOR_POWER)

    elif gs_data == [1, 1, 0]:
        car.set_motor_power(0, MOTOR_POWER, 0, MOTOR_POWER)

    elif gs_data == [1, 0, 0]:
        car.set_motor_power(-MOTOR_POWER, MOTOR_POWER, -MOTOR_POWER, MOTOR_POWER)
    return None

try:
    time.sleep(3)
    main()
finally:
    car.move("stop")
    car.set_light_off()
