#
# Copyright (C) 2021 Mark Grosen <mark@grosen.org>
# SPDX-License-Identifier: MIT
#

from time import ticks_ms

from micropython import const
from machine import Pin


PIN_OLED_CS = 22
PIN_OLED_DC = 24
PIN_OLED_RST = 23

PIN_LED = 13
PIN_NEOPIXEL = 19

PIN_ROTA = 17
PIN_ROTB = 18

PIN_SPEAKER = 16
PIN_SPEAKER_SD = 14


# https://gist.github.com/jedie/8564e62b0b8349ff9051d7c5a1312ed7
class Button:
    """
    Debounced pin handler
    usage e.g.:
    def button_callback(pin):
        print("Button (%s) changed to: %r" % (pin, pin.value()))
    button_handler = Button(pin=Pin(32, mode=Pin.IN, pull=Pin.PULL_UP), callback=button_callback)
    """

    def __init__(self, pin, callback, arg=None, trigger=Pin.IRQ_FALLING, min_ago=200):
        self.callback = callback
        self.min_ago = min_ago
        self.pin = pin
        self._arg = arg if arg else pin
        self._blocked = False
        self._next_call = ticks_ms() + self.min_ago

        pin.irq(trigger=trigger, handler=self.debounce_handler)

    def call_callback(self, arg):
        self.callback(arg)

    def debounce_handler(self, pin):
        if ticks_ms() > self._next_call:
            self._next_call = ticks_ms() + self.min_ago
            self.call_callback(self._arg)

    def value(self):
        return self.pin.value()


def make_display():
    from machine import SPI, Pin
    from sh1106 import SH1106_SPI

    spi = SPI(1, sck=Pin(26, Pin.OUT), mosi=Pin(27, Pin.OUT),
              polarity=SH1106_SPI.POL, phase=SH1106_SPI.PHA)

    display = SH1106_SPI(128, 64, spi, Pin(PIN_OLED_DC, Pin.OUT),
                         cs=Pin(PIN_OLED_CS, Pin.OUT),
                         res=Pin(PIN_OLED_RST, Pin.OUT))
    display.fill(0)
    display.rotate(True, True)

    return display
