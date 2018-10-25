#!/usr/bin/python3

from flask import Flask, render_template
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time

motorOne = "P8_18"
motorFour = "P8_26"

GPIO.setup("P8_18", GPIO.OUT)
GPIO.setup("P8_26", GPIO.OUT)


GPIO.output("P8_18", GPIO.LOW)
GPIO.output("P8_26", GPIO.LOW)


dirOne = "P9_16"
dirFour = "P8_19"

app = Flask(__name__)
@app.route("/")
@app.route("/<state>")

def updates(state=None):

    if state == "F":
        PWM.start(dirOne, 100, 2000, 0)
        PWM.start(dirFour, 100, 2000, 0)
        GPIO.output("P8_18", GPIO.HIGH)
        GPIO.output("P8_26", GPIO.HIGH)

    if state == "R":
        PWM.start(dirOne, 75, 2000, 0)
        PWM.start(dirFour, 0, 2000, 0)
        GPIO.output("P8_18", GPIO.HIGH)
        GPIO.output("P8_26", GPIO.LOW)

    if state == "L":
        PWM.start(dirOne, 0, 2000, 0)
        PWM.start(dirFour, 75, 2000, 0)
        GPIO.output("P8_18", GPIO.LOW)
        GPIO.output("P8_26", GPIO.HIGH)

    if state == "S":
        PWM.start(dirOne, 0, 2000, 0)
        PWM.start(dirFour, 0, 2000, 0)
        GPIO.output("P8_18", GPIO.LOW)
        GPIO.output("P8_26", GPIO.LOW)

    if state == "REV":
        PWM.start(dirOne, 80, 2000, 1)
        PWM.start(dirFour, 80, 2000, 1)
        GPIO.output("P8_18", GPIO.HIGH)
        GPIO.output("P8_26", GPIO.HIGH)

    if state == "REV_L":
        PWM.start(dirOne, 0, 2000, 1)
        PWM.start(dirFour, 75, 2000, 1)
        GPIO.output("P8_18", GPIO.LOW)
        GPIO.output("P8_26", GPIO.HIGH)

    if state == "REV_R":
        PWM.start(dirOne, 75, 2000, 1)
        PWM.start(dirFour, 0, 2000, 1)
        GPIO.output("P8_18", GPIO.HIGH)
        GPIO.output("P8_26", GPIO.LOW)

    template_data = {
        "title" : state,
    }
    return render_template("bobo.html", **template_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
