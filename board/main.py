import time
from machine import Pin
from neopixel import NeoPixel

pin = Pin(27, Pin.OUT)  # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 2)  # create NeoPixel driver on GPIO0 for 8 pixels


while True:
    np[0] = (100, 0, 0)
    NeoPixel.fill(np[0], 2)
    time.sleep(1)
    np[1] = (100, 100, 0)
    time.sleep(1)
    np[0] = (100, 0, 100)
    time.sleep(1)
    np[1] = (0, 100, 0)
    time.sleep(1)

    print("puikiai veikia")
