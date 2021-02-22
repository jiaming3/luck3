import RPi.GPIO as gpio
import time


def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(27, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)


def reverse(tf):
    init()
    gpio.output(27, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(tf)
    
    gpio.output(27, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(0.025)
    
    gpio.cleanup()


def forward(tf):
    init()
    gpio.output(27, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(tf)
    
    gpio.output(27, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(tf)
    
    gpio.cleanup()


def stop(tf):
    init()
    gpio.output(27, False)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, False)
    time.sleep(tf)
    gpio.cleanup()

def water(tf):
    init()
    gpio.output(17, True)
    time.sleep(tf)
    gpio.cleanup()
    
    
def motor_right(tf):
    init()
    gpio.output(27, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(tf)
    
    gpio.output(27, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(0.025)
    gpio.cleanup()
