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
        print ("Geaux Forward")
        PWM.start(dirOne, 100)
        PWM.start(dirThree, 100)
        GPIO.output("P8_18", GPIO.HIGH)
        GPIO.output("P8_14", GPIO.HIGH)
        time.sleep(.2)

    if state == "R":
        print ("Geaux Right")
        PWM.start(dirOne, 100)
        PWM.start(dirThree, 0)
        GPIO.output("P8_18", GPIO.HIGH)
        GPIO.output("P8_14", GPIO.LOW)
        time.sleep(.2)

    if state == "L":
        print ("Geaux Left")
        PWM.start(dirOne, 0)
        PWM.start(dirThree, 75) 
        GPIO.output("P8_18", GPIO.LOW)
        GPIO.output("P8_14", GPIO.HIGH)
        time.sleep(.2)

    if state == "S":
        print ("Stop!")
        PWM.start(dirOne, 0)
        PWM.start(dirThree, 0)
        GPIO.output("P8_18", GPIO.LOW)
        GPIO.output("P8_14", GPIO.LOW)
        time.sleep(.2)

    #if state == "REV":
        #print ("Reverse!")
        #PWM.start(dirOne, -75)
        #PWM.start(dirOne, -75)
        #GPIO.output("P8_18", GPIO.HIGH)
        #GPIO.output("P8_14", GPIO.HIGH)
        #time.sleep(.2)

    template_data = {
        "title" : state,
    }
    return render_template("bobo.html", **template_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
