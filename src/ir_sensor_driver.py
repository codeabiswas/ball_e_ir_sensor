import time

import Jetson.GPIO as gpio

gpio.setmode(gpio.BOARD)

sensor_output = 35

gpio.setup(sensor_output, gpio.IN)

counter = 1

try:
    while True:
        if gpio.input(sensor_output) == 1:
            print('{}: Found something!'.format(counter))
            time.sleep(1)
            counter+=1
        # print(gpio.input(sensor_output))
        # time.sleep(1)
finally:
    gpio.cleanup()
    print('cleaned up')

