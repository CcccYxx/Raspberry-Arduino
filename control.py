from pyfirmata import Arduino, util
from time import sleep

board = Arduino('/dev/ttyACM0')

while True:
    board.digital[12].write(1)
    sleep(0.8)
    board.digital[12].write(0)
    sleep(0.8)


