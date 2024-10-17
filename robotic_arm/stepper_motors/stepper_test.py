import time
import gpiozero

step_pin = gpiozero.OutputDevice(21)
direction_pin = gpiozero.OutputDevice(20)

step_pin.off()
direction_pin.off()

steps = 200

while True:

    direction_pin.on()
    for _ in range(steps):
        step_pin.on()
        time.sleep(1)
        step_pin.off()
        time.sleep(1)


    direction_pin.off()
    for _ in range(steps):
        step_pin.on()
        time.sleep(1)
        step_pin.off()
        time.sleep()

