import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep

from hal import hal_led as led
from hal import hal_input_switch as switch

def init():
    GPIO.setmode(GPIO.BCM) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(22,GPIO.IN) #set GPIO 22 as input
    GPIO.setup(24,GPIO.OUT)

led.init()
switch.init()


def read_slide_switch():
    ret = 0

    if GPIO.input(22):
        ret = 1
        led.set_output(0,1)

    return ret

if __name__ == "__main__":
    main()