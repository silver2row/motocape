#!/usr/bin/python3

# Testing with the BeagleY-AI and Python3
# Testing gpiod v2
# Untested

import os
from flask import Flask, render_template, request, jsonify
import gpiod
from gpiod.line import Direction, Value

app = Flask(__name__)

# --- Linux GPIO Pin Assignment ---
CHIP_PATH = "/dev/gpiochip3"  # With the BeagleY-AI
MOTOR_IN1 = 'GPIO12'
MOTOR_IN2 = 'GPIO6'

line_config = {
    MOTOR_IN1: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
    MOTOR_IN2: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE)
}

# Request lines globally so they persist across HTTP web requests
gpio_request = gpiod.request_lines(
    CHIP_PATH,
    consumer="flask-dc-motor-ajax",
    config=line_config
)

current_status = "Stopped (Coast)"

def set_motor(in1_state, in2_state, status_text):
    global current_status
    gpio_request.set_value(MOTOR_IN1, in1_state)
    gpio_request.set_value(MOTOR_IN2, in2_state)
    current_status = status_text
    print(f"AJAX Command Executed: {status_text}")

@app.route('/')
def home():
    return render_template('index_one.html', status=current_status)

# CHANGED: Accepts JSON POST data and outputs clean JSON telemetry back
@app.route('/control', methods=['POST'])
def control_motor():
    data = request.get_json() or {}
    action = data.get('action')
    
    if action == 'forward':
        set_motor(Value.ACTIVE, Value.INACTIVE, "Moving Forward")
    elif action == 'reverse':
        set_motor(Value.INACTIVE, Value.ACTIVE, "Moving Reverse")
    elif action == 'brake':
        set_motor(Value.ACTIVE, Value.ACTIVE, "Braked (Hard Stop)")
    elif action == 'stop':
        set_motor(Value.INACTIVE, Value.INACTIVE, "Stopped (Coast)")
    else:
        return jsonify({"error": "Unknown action"}), 400
        
    return jsonify({"status": current_status})

import atexit
@atexit.register
def cleanup():
    print("\nShutting down web server. Freeing GPIO hardware locks...")
    gpio_request.set_value(MOTOR_IN1, Value.INACTIVE)
    gpio_request.set_value(MOTOR_IN2, Value.INACTIVE)
    gpio_request.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
