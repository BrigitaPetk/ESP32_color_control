import time
from machine import Pin
from neopixel import NeoPixel
import json
import time
import network
import urequests


# Prieeiga prie ID ir slaptazodziu:
with open('secret.json') as f:
    config = json.load(f)


# Prisijungimas prie wifi
wifi = network.WLAN(network.STA_IF)
    
def prisijungimas():
    wifi.active(True)
    print(wifi.scan())                             # Nuskanuojamos galimo interneto prieeigos
    wifi.connect(config["ssid"], config["ssid_password"])       # Prisijungimas

    while not wifi.isconnected():
        time.sleep(1)

    return "Prisijungta sekmingai"
    # print(wifi.ifconfig())


# Nurodymai neopixeliui:
pin = Pin(14, Pin.OUT)      # 27 jungtis(GPIO0) atitinka T7 jungti ant mikroschemos
np = NeoPixel(pin, 3)        # nurodoma, kuri jungtis ir kiek Neopixeliu prijungta


while True:
    if wifi.isconnected():
        # RGB spalvos gavimas is serverio:
        uzklausos_atsakymas = urequests.get("http://192.168.8.117:5000/spalva")
        print(f"Užklausos statusas: {uzklausos_atsakymas.status_code}")
        r_g_b = uzklausos_atsakymas.json()
        print(r_g_b)
        r = r_g_b["r"]
        g = r_g_b["g"]
        b = r_g_b["b"]

        for index, _  in enumerate(np):
            np[index] = (r, g, b)
            np.write()    

        time.sleep(5)        
    
    else:
        prisijungimas()


