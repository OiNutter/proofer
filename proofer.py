import os
import json

from guizero import App, Text, PushButton, Box
from probe import read_temp
from relay import turn_on, turn_off
from threading import Thread
import switches

SETTINGS_FILE = 'settings.json'

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

# Set Defaults
settings = {
    'desired_temp': 24.0
}

if os.path.exists(SETTINGS_FILE) and os.path.isfile(SETTINGS_FILE):
    with open(SETTINGS_FILE, 'r') as f:
        try:
            settings = json.load(f)
        except Exception as e:
            print("got %s on json.load()" % e)

current_temp = 20.0

blue = "#00ffff"
green = "#00ff33"
red = "#f90004"
white = "#ffffff"
grey = "#cccccc"

app = App(
    bg = grey
)

def check_temp():
    global current_temp
    current_temp = read_temp()
    current_temperature_label.value = u"Current: %.2f\u00B0C" % current_temp
    toggle_heater()

def toggle_heater():
    if current_temp < (settings['desired_temp']-0.5):
        app.bg = blue
        turn_on()
        print("%d - cold" % current_temp)
    elif current_temp > (settings['desired_temp'] + 0.5):
        app.bg = red
        turn_off()
        print("%d - warm" % current_temp)
    else:
        app.bg = green
    print("%d - perfect" % current_temp)

def adjust_temp(change):
    global settings
    settings['desired_temp'] += change
    print ("TARGET: %d" % settings['desired_temp'])
    desired_temperature_label.value = u"%d\u00B0C" % settings['desired_temp']
    save_settings()
    t = Thread(target=check_temp)
    t.start()

def save_settings():
    with open(SETTINGS_FILE, 'w+') as f:
        json.dump(settings, f)

app.set_full_screen()

left_box = Box(app, align="left", width="fill", height="fill");
Box(left_box, align="top", width="fill", height=10)

title_label = Text(
    left_box,
    text="Proofer",
    align="top",
    size=50,
    color=white
)
Box(left_box, align="top", width="fill", height=50)

current_temperature_label = Text(
    left_box,
    text=u"Current: %.2f\u00B0C" % current_temp,
    align="top",
    width="fill",
    size = 30,
    color = white
)
current_temperature_label.repeat(30000, check_temp)
Box(left_box, align="top", width="fill", height=10)

desired_temperature_label = Text(
    left_box,
    text=u"%d\u00B0C" % settings['desired_temp'],
    align="top",
    width="fill",
    size=125,
    color = white
)

right_box = Box(app, align="right", height="fill", width=200)

temp_up = PushButton(
    right_box,
    text="▲",
    command=adjust_temp,
    args=[1],
    width = "fill",
    height = "fill"
)

temp_up.text_size = 50
temp_up.text_color = white

temp_down = PushButton(
    right_box,
    text="▼",
    command=adjust_temp,
    args=[-1],
    width = "fill",
    height = "fill"
)
temp_down.text_size = 50
temp_down.text_color = white

check_temp()
app.display()
