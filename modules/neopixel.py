#
# Copyright (C) 2021 Mark Grosen <mark@grosen.org>
# SPDX-License-Identifier: MIT
#

import array
import rp2


class NeoPixel():
    @staticmethod
    def _ws2812(pull_thresh):
        def _ws2812_inner():
            T1 = 2
            T2 = 5
            T3 = 3
            wrap_target()
            label("bitloop")
            out(x, 1)               .side(0)    [T3 - 1]
            jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
            jmp("bitloop")          .side(1)    [T2 - 1]
            label("do_zero")
            nop()                   .side(0)    [T2 - 1]
            wrap()
        return rp2.asm_pio(
            sideset_init=rp2.PIO.OUT_LOW,
            out_shiftdir=rp2.PIO.SHIFT_LEFT,
            autopull=True,
            pull_thresh=pull_thresh)(_ws2812_inner)

    def __init__(self, pin, num_leds, bpp=3, pio_sm=7):
        if bpp not in {3, 4}:
            raise ValueError("bpp must be 3 or 4")
        self.sm = rp2.StateMachine(pio_sm, self._ws2812(8 * bpp),
                                   freq=8_000_000, sideset_base=pin)
        self.bpp = bpp
        self.shift = 32 - (bpp * 8)
        self.leds = array.array("I", [0 for _ in range(num_leds)])
        self.sm.active(1)

    def __getitem__(self, index):
        val = self.leds[index]
        if self.bpp == 3:
            return ((val >> 8) & 0xff, (val >> 16) & 0xff, val & 0xff)
        else:
            return ((val >> 16) & 0xff, (val >> 24) & 0xff, (val >> 8) & 0xff,
                    val & 0xff)

    def __setitem__(self, index, val):
        grb = (val[1] << 16) | (val[0] << 8) | val[2]
        if self.bpp == 3:
            self.leds[index] = grb
        else:
            self.leds[index] = (grb << 8) | (0 if len(val) == 3 else val[3])

    def __len__(self):
        return len(self.leds)

    def fill(self, val):
        for i in range(len(self.leds)):
            self[i] = val

    def write(self):
        self.sm.put(self.leds, self.shift)
