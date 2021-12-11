import time
from machine import Pin
from neopixel import NeoPixel
import json
import time
import network


# Prieeiga prie ID ir slaptazodziu:
with open('secret.json') as f:
    config = json.load(f)

# Prisijungimas prie wifi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
print(wifi.scan())                             # Nuskanuojamos galimo interneto prieeigos
wifi.connect(config["ssid"], config["ssid_password"])       # Prisijungimas

while not wifi.isconnected():
    time.sleep(1)

print("Prisijungta sekmingai")



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
