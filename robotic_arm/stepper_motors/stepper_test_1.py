import RPi.GPIO as GPIO
import time

# Define GPIO pins
DIR_PIN = 20  # Direction pin
STEP_PIN = 21  # Step pin

# Motor settings
step_delay = 0.001  # Delay between steps (in seconds)

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)

def move_stepper(steps, direction):
    # Set motor direction
    GPIO.output(DIR_PIN, direction)
    
    for _ in range(steps):
        # Generate step pulse
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(step_delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(step_delay)

try:
    while True:
        print("Moving Clockwise...")
        move_stepper(1000, GPIO.HIGH)  # Move 1000 steps clockwise
        
        time.sleep(1)  # Pause before changing direction
        
        print("Moving Counterclockwise...")
        move_stepper(1000, GPIO.LOW)  # Move 1000 steps counterclockwise
        
        time.sleep(1)  # Pause before repeating

except KeyboardInterrupt:
    # Clean up GPIO on CTRL+C exit
    GPIO.cleanup()

# Clean up GPIO on normal exit
GPIO.cleanup()
