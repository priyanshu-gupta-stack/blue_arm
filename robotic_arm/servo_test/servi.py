import pigpio import time SERVO_PIN = 14 # GPIO 14 
(physical pin 8 on Raspberry Pi) pi = pigpio.pi() if 
not pi.connected:
    exit() def set_servo_angle(angle):
    # Servo expects a PWM pulse width between 500 (0 
    # degrees) and 2500 (180 degrees) microseconds
    pulse_width = 500 + (angle / 180.0) * 2000 
    pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)
try: while True: angle = input("Enter the desired 
        angle (0-180): ") try:
            angle = float(angle) if 0 <= angle <= 
            180:
                set_servo_angle(angle) print(f"Servo 
                moved to {angle} degrees.")
            else: print("Please enter an angle 
                between 0 and 180.")
        except ValueError: print("Invalid input. 
            Please enter a numeric value.")
except KeyboardInterrupt: pass
# Cleanup
pi.set_servo_pulsewidth(SERVO_PIN, 0) # Turn off 
servo
pi.stop()
