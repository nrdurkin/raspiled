import time
import board
import colorsys
import neopixel


# LED strip configuration:
LED_COUNT = 300  # Number of LED pixels.
strip = neopixel.NeoPixel(board.D18, LED_COUNT, auto_write=False)

mode = 'BLOCK'

def blockColor(color):
    mode = 'BLOCK'
    for i in range(LED_COUNT):
        strip[i] = color
    strip.show()

def rgb(hex):
    if hex[0] == '#':
        hex = hex[1:]
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))

def crossFade():
    mode = 'CROSSFADE'
    frame(0)


def frame(fadeHue=0):
    if mode == 'CROSSFADE':
        fadeHue+=.005
        if fadeHue >1:
            fadeHue = 0
        strip.fill(colorsys.hls_to_rgb(fadeHue,.5,1))
        time.sleep(.05)
        frame(fadeHue)
    else:
        return

                # blockColor(strip, rgb(color))  # Green wipe

    # except KeyboardInterrupt:
    #     colorWipe(strip, (0, 0, 0), 10)
