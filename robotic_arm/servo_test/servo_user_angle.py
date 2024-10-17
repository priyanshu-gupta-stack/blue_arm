import RPi.GPIO as GPIO
import time

# Set up GPIO
servo_pin = 14  # GPIO24
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Set up PWM for the servo
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz frequency for servo control
pwm.start(0)  # Start PWM with 0 duty cycle

def set_servo_angle(angle):
    duty = 2 + (angle / 18)  # Map angle (0-180) to duty cycle (2-12)
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        # Ask for user input
        user_input = input("Enter servo angle (0-180 degrees) or 'exit' to quit: ")

        if user_input.lower() == 'exit':
            break  # Exit the loop if user types 'exit'

        try:
            angle = float(user_input)
            if 0 <= angle <= 180:
                set_servo_angle(angle)  # Set the servo to the input angle
            else:
                print("Please enter a value between 0 and 180.")
        except ValueError:
            print("Invalid input. Please enter a numeric value between 0 and 180.")

except KeyboardInterrupt:
    pass

# Clean up
pwm.stop()
GPIO.cleanup()
