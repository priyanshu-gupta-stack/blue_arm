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
        # Move servo to different angles
        set_servo_angle(0)
        time.sleep(2)
        set_servo_angle(90)
        time.sleep(2)
        set_servo_angle(180)
        time.sleep(2)

except KeyboardInterrupt:
    pass

# Clean up
pwm.stop()
GPIO.cleanup()
