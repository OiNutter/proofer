import os
import RPi.GPIO as GPIO
from threading import Thread

BRIGHT_UP = 27
BRIGHT_DOWN = 23
TOGGLE_LIGHT = 22
REBOOT = 17
BACKLIGHT = 18

light_level = 100
light_step = 10
light_on = True

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(BRIGHT_UP,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BRIGHT_DOWN,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TOGGLE_LIGHT,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(REBOOT,GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(BACKLIGHT,GPIO.OUT)
#GPIO.output(BACKLIGHT, light_level)
p = GPIO.PWM(BACKLIGHT, 1000)
p.start(100)

def brightness_up(channel):
    global light_level
    print("BRIGHT UP")
    light_level += light_step
    if light_level > 100:
        light_level = 100

    p.ChangeDutyCycle(light_level)

def brightness_down(channel):
    global light_level
    print("BRIGHT DOWN")
    light_level -= light_step
    if light_level < 0:
        light_level = 0

    p.ChangeDutyCycle(light_level)

def toggle_light(channel):
    global light_level

    if light_level > 0:
        light_level = 0
    else:
        light_level = 100

    p.ChangeDutyCycle(light_level)

def reboot(channel):
    print ("REBOOT")
    os.system("reboot");

GPIO.add_event_detect(BRIGHT_UP,GPIO.RISING,callback=brightness_up, bouncetime=200)
GPIO.add_event_detect(BRIGHT_DOWN,GPIO.RISING,callback=brightness_down, bouncetime=200)
GPIO.add_event_detect(TOGGLE_LIGHT,GPIO.RISING,callback=toggle_light, bouncetime=200)
GPIO.add_event_detect(REBOOT,GPIO.RISING,callback=reboot, bouncetime=200)

p.ChangeDutyCycle(100)
