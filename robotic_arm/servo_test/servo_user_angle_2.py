import RPi.GPIO as GPIO
import time

# Set up GPIO
servo_pin = 14  # GPIO14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Set up PWM for the servo
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz frequency for servo control
pwm.start(0)  # Start PWM with 0 duty cycle

def set_servo_angle(angle):
    duty = 2 + (angle / 18)  # Map angle (0-180) to duty cycle (2-12)
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

def get_valid_input():
    while True:
        user_input = input("Enter servo angle (0-180 degrees) or 'exit' to quit: ")
        if user_input.lower() == 'exit':
            return None  # If 'exit' is typed, return None to indicate the user wants to quit.
        
        try:
            angle = float(user_input)
            if 0 <= angle <= 180:
                return angle  # Return the valid angle
            else:
                print("Please enter a value between 0 and 180.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit'.")

try:
    while True:
        angle = get_valid_input()  # Get a valid angle from the user or None if they want to exit
        if angle is None:
            print("Exiting program...")
            break  # Exit the loop if user types 'exit'
        
        # Set the servo to the specified angle
        set_servo_angle(angle)
        print(f"Servo moved to {angle} degrees.")

except KeyboardInterrupt:
    print("Program interrupted by user.")

# Clean up
pwm.stop()
GPIO.cleanup()
