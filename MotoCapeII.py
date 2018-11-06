#!/usr/bin/python3

# w/ help from #beagle on Freenode

from flask import Flask, render_template
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time

class Motor:
    def __init__(self, dir_pin, pwm_pin, pwm_freq):
        self.dir_pin = dir_pin
        self.pwm_pin = pwm_pin
        self.value = 0

        PWM.start(pwm_pin, 0, pwm_freq)
        GPIO.setup(dir_pin, GPIO.OUT)

    def set(self, value):
        assert -100 <= value <= 100
        if (value < 0) != (self.value < 0):
            # changing direction
            PWM.set_duty_cycle(self.pwm_pin, 0)
            GPIO.output(self.dir_pin, value < 0)
        PWM.set_duty_cycle(self.pwm_pin, abs(value))
        self.value = value

motor1 = Motor(dir_pin="P8_18", pwm_pin="P9_16", pwm_freq=2000)
#motor2 = Motor(dir_pin="P8_16", pwm_pin="P9_14", pwm_freq=2000)
#motor3 = Motor(dir_pin="P8_14", pwm_pin="P8_13", pwm_freq=2000)
motor4 = Motor(dir_pin="P8_26", pwm_pin="P8_19", pwm_freq=2000)

app = Flask(__name__)
@app.route("/")
@app.route("/<state>")

def updates(state=None):
    if state == "F":
        motor1.set(100)
        motor4.set(100)
        time.sleep(.2)
    if state == "L":
        motor1.set(0)
        motor4.set(85)
        time.sleep(.2)
    if state == "R":
        motor1.set(85)
        motor4.set(0)
        time.sleep(.2)
    if state == "S":
        motor1.set(0)
        motor4.set(0)
        time.sleep(.2)
    if state == "REV":
        motor1.set(-75)
        motor4.set(-75)
        time.sleep(.2)
    if state == "REV_L":
        motor1.set(-75)
        motor4.set(0)
        time.sleep(.2)
    if state == "REV_R":
        motor1.set(0)
        motor4.set(-75)
        time.sleep(.2)

    template_data = {
        "title" : state,
    }
    return render_template("boboIII.html", **template_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
