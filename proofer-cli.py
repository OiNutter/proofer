import time
from datetime import datetime
from probe import read_temp
from relay import turn_on, turn_off

desired_temp = 24
start = datetime.now()
state = 0

while True:
    current_temp = read_temp()
    print ("CURRENT TEMP: %f", current_temp)
    if current_temp < desired_temp:
        if state != 0:
            turn_on()
            state = 0
            now = datetime.now()
            diff = now - start
            start = datetime.now()
            print ("TIME TO COOL: %d" % diff.seconds)
        print ("TOO COLD")
    elif current_temp >= desired_temp:
        if state != 1:
            state = 1
            turn_off()
            now = datetime.now()
            diff = now - start
            start = datetime.now()
            print ("TIME TO HEAT: %d" % diff.seconds)
        print ("TOO HOT")

    time.sleep(30)
