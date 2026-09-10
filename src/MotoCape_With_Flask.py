#!/usr/bin/python3

import os
from flask import Flask, render_template, request, jsonify
import gpiod
from gpiod.line import Direction, Value

app = Flask(__name__)

# --- Linux GPIO Pin Assignment ---
CHIP_PATH = "/dev/gpiochip3"  # For the BeagleY-AI
MOTOR_IN1 = 'GPIO12'
MOTOR_IN2 = 'GPIO6'

line_config = {
    MOTOR_IN1: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
    MOTOR_IN2: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE)
}

# Request lines globally so they persist across HTTP web requests
# Note: Using an explicit variable instead of a context manager so Flask threads can access it
gpio_request = gpiod.request_lines(
    CHIP_PATH,
    consumer="flask-dc-motor",
    config=line_config
)

# Tracks the current state of the motor for the UI dashboard
current_status = "Stopped (Coast)"

# --- Core Motor Driver Actions ---
def set_motor(in1_state, in2_state, status_text):
    global current_status
    gpio_request.set_value(MOTOR_IN1, in1_state)
    gpio_request.set_value(MOTOR_IN2, in2_state)
    current_status = status_text
    print(f"Web Command Executed: {status_text}")

# --- Flask Web Routes ---
@app.route('/')
def home():
    # Render the UI template and inject the active motor state text
    return render_template('index.html', status=current_status)

@app.route('/control', methods=['POST'])
def control_motor():
    action = request.form.get('action')
    
    if action == 'forward':
        set_motor(Value.ACTIVE, Value.INACTIVE, "Moving Forward")
    elif action == 'reverse':
        set_motor(Value.INACTIVE, Value.ACTIVE, "Moving Reverse")
    elif action == 'brake':
        set_motor(Value.ACTIVE, Value.ACTIVE, "Braked (Hard Stop)")
    elif action == 'stop':
        set_motor(Value.INACTIVE, Value.INACTIVE, "Stopped (Coast)")
        
    return render_template('index.html', status=current_status)

# Clean up GPIO pins when the application closes
import atexit
@atexit.register
def cleanup():
    print("\nShutting down web server. Freeing GPIO hardware locks...")
    gpio_request.set_value(MOTOR_IN1, Value.INACTIVE)
    gpio_request.set_value(MOTOR_IN2, Value.INACTIVE)
    gpio_request.close()

if __name__ == '__main__':
    # Run the app. Debug=False is highly recommended when driving hardware 
    # because Flask's auto-reloader can duplicate background hardware calls.
    app.run(host='0.0.0.0', port=5000, debug=False)
