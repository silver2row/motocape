#!/usr/bin/python

from flask import Flask, render_template
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time

motorOne = "P8_18"
motorThree = "P8_14"

GPIO.setup("P8_18", GPIO.OUT)
GPIO.setup("P8_14", GPIO.OUT)


GPIO.output("P8_18", GPIO.LOW)
GPIO.output("P8_14", GPIO.LOW)


dirOne = "P9_16"
dirThree = "P8_13"

app = Flask(__name__)
@app.route("/")
@app.route("/<state>")

def updates(state=None):

    if state == "F":
        PWM.start(dirOne, 100)
        PWM.start(dirThree, 100)
        GPIO.output("P8_18", GPIO.HIGH)
        GPIO.output("P8_14", GPIO.HIGH)

    if state == "R":
        PWM.start(dirOne, 75)
        PWM.start(dirThree, 0)
        GPIO.output("P8_18", GPIO.HIGH)
        GPIO.output("P8_14", GPIO.LOW)

    if state == "L":
        PWM.start(dirOne, 0)
        PWM.start(dirThree, 75)
        GPIO.output("P8_18", GPIO.LOW)
        GPIO.output("P8_14", GPIO.HIGH)

    if state == "S":
        PWM.start(dirOne, 0)
        PWM.start(dirThree, 0)
        GPIO.output("P8_18", GPIO.LOW)
        GPIO.output("P8_14", GPIO.LOW)

    #if state == "REV":
        #PWM.start(dirOne, 80, 1)
        #PWM.start(dirThree, 80, 1)
        #GPIO.output("P8_18", GPIO.HIGH)
        #GPIO.output("P8_14", GPIO.HIGH)

    template_data = {
        "title" : state,
    }
    return render_template("bobo.html", **template_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
