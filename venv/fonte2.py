#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-2020 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

from __future__ import unicode_literals
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from time import sleep
import sys
import random
from pathlib import Path
from PIL import ImageFont
from demo_opts import get_device
from luma.core.render import canvas
from luma.core.sprite_system import framerate_regulator



def main():
    serial = i2c(port=0, address=0x3C)
    device = ssd1306(serial, rotate=0)
    font = make_font("ChiKareGo.ttf ", device.height - 5)
    texto="francivaldo"

    with canvas(device) as draw:
        w, h = draw.textsize(texto=code, font=font)
        left = (device.width - w) / 2
        top = (device.height - h) / 2
        draw.text((left, top), texto=code, font=font, fill="white")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass