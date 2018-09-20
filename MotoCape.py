#!/usr/bin/python

from flask import Flask, render_template
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time

motorOne = "P8_18"
#motorTwo = "P8_16"
motorThree = "P8_14"
#motorFour = "P8_26"

GPIO.setup("P8_18", GPIO.OUT)
#GPIO.setup("P8_16", GPIO.OUT)
GPIO.setup("P8_14", GPIO.OUT)
#GPIO.setup("P8_26", GPIO.OUT)

GPIO.output("P8_18", GPIO.LOW)
#GPIO.output("P8_16", GPIO.LOW)
GPIO.output("P8_14", GPIO.LOW)
#GPIO.output("P8_26", GPIO.LOW)

dirOne = "P9_16"
#dirTwo = "P9_14"
dirThree = "P8_13"
#dirFour = "P8_19"

app = Flask(__name__)
@app.route("/")
@app.route("/<state>")

def updates(state=None):
    if state == "F":
        print "Robot Moving Forward"
        PWM.start(dirOne, 100)
        PWM.start(dirThree, 100)
        GPIO.output("P8_18", GPIO.HIGH)
        #GPIO.output("P8_16", GPIO.LOW)
        GPIO.output("P8_14", GPIO.HIGH)
        #GPIO.output("P8_26", GPIO.LOW)
        #PWM.start(dirOne, 75)
        #PWM.start(dirThree, 75)
        time.sleep(.2)
    if state == "R":
        print "Robot Turning Right"
        PWM.start(dirOne, 100)
        GPIO.output("P8_18", GPIO.HIGH)
        #GPIO.output("P8_16", GPIO.LOW)
        GPIO.output("P8_14", GPIO.LOW)
        #GPIO.output("P8_26", GPIO.LOW)
        #PWM.start(dirOne, 75)
        time.sleep(.2)
    if state == "L":
        print "Robot Turning Left"
        PWM.start(dirThree, 100)
        GPIO.output("P8_18", GPIO.LOW)
        #GPIO.output("P8_16", GPIO.LOW)
        GPIO.output("P8_14", GPIO.HIGH)
        #GPIO.output("P8_26", GPIO.LOW)
        #PWM.start(ledThree, 0)
        time.sleep(.2)
    if state == "S":
        print "Robot Stopped"
        PWM.start(dirOne, 0)
        PWM.start(dirThree, 0)
        GPIO.output("P8_18", GPIO.LOW)
        #GPIO.output("P8_16", GPIO.LOW)
        GPIO.output("P8_14", GPIO.LOW)
        #GPIO.output("P8_26", GPIO.LOW)
        time.sleep(.2)
    template_data = {
        "title" : state,
    }
    return render_template("boboJackson.html", **template_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
