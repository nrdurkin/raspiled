import time
import board
import neopixel


# LED strip configuration:
LED_COUNT = 200  # Number of LED pixels.
strip = neopixel.NeoPixel(board.D18, LED_COUNT, auto_write=False)


# Define functions which animate LEDs in various ways.
def colorWipe(color, wait_ms=25):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip[i] = color
        time.sleep(wait_ms/1000)


def blockColor(color):
    for i in range(strip):
        strip[i] = color
    strip.show()

def rgb(hex):
    if hex[0] == '#':
        hex = hex[1:]
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))

                # blockColor(strip, rgb(color))  # Green wipe

    # except KeyboardInterrupt:
    #     colorWipe(strip, (0, 0, 0), 10)
