from gpiozero import Button, LED, PWMLED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(0.8)
    led.off()
    sleep(0.8)


