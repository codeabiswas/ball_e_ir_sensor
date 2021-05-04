"""
ir_sensor_driver.py
---
This file contains the main method to get information from the IR sensor.
NOTE: This is not being used and has not been developed much because the sensors themselves do not work very well and given how the mechanical build is for the feed and how the entire system has been programmed, this sensor is not needed.
---

Author: Andrei Biswas (@codeabiswas)
Date: May 4, 2021
Last Modified: May 04, 2021
"""

import time

import Jetson.GPIO as gpio

def main():
    """Main prototype/testing area. Code prototyping and checking happens here."""

    gpio.setmode(gpio.BOARD)

    # Set the sensor output pin
    sensor_output = 35
    gpio.setup(sensor_output, gpio.IN)

    # Counter for how many times an object is detected
    counter = 1

    # Loop until the user exits the loop manually using <C(trl)-c>
    try:
        while True:
            if gpio.input(sensor_output) == 1:
                print('{}: Found Something!'.format(counter))
                time.sleep(1)
                counter+=1
    # If loop is exited, clean the pins for future use
    finally:
        gpio.cleanup()
        print('Cleaned Up')

if __name__ == "__main__":
    # Run the main function
    main()

