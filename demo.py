from machine import Pin, PWM
from time import sleep

import macropad
from neopixel import NeoPixel

global display
global np


def pushed(index):
    display.fill_rect(8, 20, 100, 10, 0)
    display.text("Key: {} ".format(index), 8, 20, 1)
    display.show()

    np.fill((160, 0, 0))
    np[index] = (0, 0, 200)
    np.write()


def main():
    led = Pin(macropad.PIN_LED, Pin.OUT)
    led.value(1)

    spkr_sd = Pin(macropad.PIN_SPEAKER_SD, Pin.OUT)
    spkr_sd.value(1)

    speaker = PWM(Pin(macropad.PIN_SPEAKER, Pin.OUT))
    speaker.freq(440)
    speaker.duty_u16(32000)

    global np
    np = NeoPixel(Pin(macropad.PIN_NEOPIXEL, Pin.OUT), 12)
    np.fill((160, 0, 0))
    np.write()

    global display
    display = macropad.make_display()
    display.text("MacroPad Demo", 8, 10, 1)
    display.rect(0, 0, display.width-1, display.height-1, 1)
    display.show()

    sleep(1)
    spkr_sd.value(0)

    keys = [0] * 12
    for i in range(12):
        keys[i] = macropad.Button(Pin(i+1, Pin.IN, Pin.PULL_UP), pushed, arg=i)

    cnt = 0
    while True:
        sleep(0.1)
        # print("loop:", cnt, end="\r")
        led.value(not led.value())
        cnt += 1


main()
