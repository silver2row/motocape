#!/usr/bin/python3

# w/ help from AI and google in 9/2026
# Changes done by Seth in 2026

from time import sleep
import gpiod
from gpiod.line import Direction, Value

# from flask import Flask, render_template

# --- Linux GPIO Pin Assignment ---
CHIP_PATH = "/dev/gpiochip3"  # For BeagleY-AI
MOTOR_IN1 = 'GPIO12'          # Connects to H-Bridge IN1 pin
MOTOR_IN2 = 'GPIO6'           # Connects to H-Bridge IN2 pin

# Configure outputs in unified v2 structure
line_config = {
    MOTOR_IN1: gpiod.LineSettings(
        direction=Direction.OUTPUT,
        output_value=Value.INACTIVE
    ),
    MOTOR_IN2: gpiod.LineSettings(
        direction=Direction.OUTPUT,
        output_value=Value.INACTIVE
    )
}

# --- Core DC Motor Primitives ---
def motor_forward(request):
    """Drives the motor in a forward direction."""
    print("oving Forward")
    request.set_value(MOTOR_IN1, Value.ACTIVE)
    request.set_value(MOTOR_IN2, Value.INACTIVE)

def motor_reverse(request):
    """Drives the motor in a reverse direction."""
    print("oving Reverse")
    request.set_value(MOTOR_IN1, Value.INACTIVE)
    request.set_value(MOTOR_IN2, Value.ACTIVE)

def motor_brake(request):
    """Actively brakes/stops the motor quickly by shorting both poles."""
    print("Active Brake")
    request.set_value(MOTOR_IN1, Value.ACTIVE)
    request.set_value(MOTOR_IN2, Value.ACTIVE)

def motor_coast(request):
    """Cuts all power to the motor, allowing it to spin down freely."""
    print("Coasting Stop")
    request.set_value(MOTOR_IN1, Value.INACTIVE)
    request.set_value(MOTOR_IN2, Value.INACTIVE)

# --- Operational Sequence ---
try:
    with gpiod.request_lines(
        CHIP_PATH,
        consumer="dc-motor-example",
        config=line_config
    ) as request:
        
        while True:
            # 1. Run forward for 3 seconds
            motor_forward(request)
            time.sleep(3.0)
            
            # 2. Hard brake for 1 second
            motor_brake(request)
            time.sleep(1.0)
            
            # 3. Run in reverse for 3 seconds
            motor_reverse(request)
            time.sleep(3.0)
            
            # 4. Coast to a stop for 2 seconds
            motor_coast(request)
            time.sleep(2.0)

except KeyboardInterrupt:
    print("\nSequence terminated by user.")
    # Safe fallback if script execution breaks: make sure pins are safe
    try:
        with gpiod.request_lines(CHIP_PATH, consumer="safety-stop", config=line_config) as req:
            motor_coast(req)
    except Exception:
        pass
except OSError as e:
    print(f"GPIO Error: {e}")

# Testing without Flask for now
