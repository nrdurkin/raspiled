import colorsys, random

def randomPrettyRGB():
    percent = colorsys.hsv_to_rgb(random.uniform(0, 1), 1, 1)
    return (255 * percent[0], 255 * percent[1], 255 * percent[2])

def rgb(hex):
    if hex[0] == '#':
        hex = hex[1:]
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))

from enum import Enum

class Mode(Enum):
    BLOCK = 0
    CROSSFADE = 1
    FAIRY = 2
    STRIPE = 3