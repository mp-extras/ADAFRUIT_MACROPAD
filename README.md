# MicroPython Board Support for Adafruit MacroPad

This project provides MicroPython board definition and support modules for the Adafruit RP2040-based [MacroPad board](https://learn.adafruit.com/adafruit-macropad-rp2040?view=all).

## Support

* OLED Display - SH1106 driver using FrameBuffer class over SPI
* Neopixel - RP2040 version of the ESP32 NeoPixel class using the PIO SM
* I2C, SPI and Pin definitions for (reasonable) defaults based on schematic
* Half-baked key debouncing

## Missing

* Quadrature Encoding for the rotary encoder switch

## USB HID

Interim USB HID support comes from this RPi [forum post](https://www.raspberrypi.org/forums/viewtopic.php?t=310876)

## Build

Follow the README in the `micropython/ports/rp2` directory to get build fundamentals working.

Once you can build the GENERIC board successfully, you can build the MacroPad version here either from the `ports/rp2` directory or this directory.

You will need to apply a patch to the `ports/rp2/Makefile` to support out-of-tree board definitions (like this one).

``` makefile
 ifdef USER_C_MODULES
 CMAKE_ARGS += -DUSER_C_MODULES=${USER_C_MODULES}
 endif

+ifdef BOARD_DIR
+CMAKE_ARGS += -DMICROPY_BOARD_DIR=${BOARD_DIR} -DPICO_BOARD_HEADER_DIRS=${BOARD_DIR}
+endif
+
```

### `ports/rp2`

`make BOARD=ADAFRUIT-MACROPAD BOARD_DIR=<path/to/this>/ADAFRUIT_MACROPAD`

### This Directory

`make MICROPYTHON=</path/to>/micropython`

## Demo

After flashing the MicroPython UF2 file, you can run a simple demo/example that illustrates basic functionality:

`mpremote run demo.py`
