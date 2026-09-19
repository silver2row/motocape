from flask import Flask, render_template, request, redirect, url_for
import gpiod
from gpiod.line import Direction, Value

app = Flask(__name__)

# --- GPIO CONFIGURATION (gpiod v2) ---
# Define your chip and GPIO line offsets (adjust numbers for your hardware/Beagleboard.org Boards...)
CHIP_PATH = "/dev/gpiochip3"  # BeagleY-AI

MOTOR_A_PIN1 = 'GPIO'
MOTOR_A_PIN2 = 'GPIO'
MOTOR_B_PIN1 = 'GPIO'
MOTOR_B_PIN2 = 'GPIO'

# Create the line config mapping pins to Output direction
line_settings = {
    MOTOR_A_PIN1: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
    MOTOR_A_PIN2: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
    MOTOR_B_PIN1: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
    MOTOR_B_PIN2: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
}

# Request the lines from the chip
chip = gpiod.Chip(CHIP_PATH)
motor_request = chip.request_lines(consumer="flask-motor-control", config=line_settings)

def set_motor(motor, direction):
    """Helper to set line values based on motor and desired action."""
    # Determine which pins to change
    if motor == "A":
        pin1, pin2 = MOTOR_A_PIN1, MOTOR_A_PIN2
    elif motor == "B":
        pin1, pin2 = MOTOR_B_PIN1, MOTOR_B_PIN2
    else:
        return

    # Determine high/low state based on direction
    if direction == "forward":
        v1, v2 = Value.ACTIVE, Value.INACTIVE
    elif direction == "backward":
        v1, v2 = Value.INACTIVE, Value.ACTIVE
    else:  # stop
        v1, v2 = Value.INACTIVE, Value.INACTIVE

    # Apply values using gpiod v2 request
    motor_request.set_values({pin1: v1, pin2: v2})

# --- FLASK ROUTES ---
@app.route("/")
def index():
    return render_template("two_DC_motors.html")

@app.route("/control", methods=["POST"])
def control():
    motor = request.form.get("motor")       # 'A' or 'B'
    action = request.form.get("action")     # 'forward', 'backward', 'stop'
    
    if motor in ["A", "B"] and action in ["forward", "backward", "stop"]:
        set_motor(motor, action)
        
    return redirect(url_for("index"))

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    finally:
        # Clean up and release GPIO lines when Flask stops
#        motor_request.release()
#        chip.close()
