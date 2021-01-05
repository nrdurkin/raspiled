import time
import board
import neopixel


# LED strip configuration:
LED_COUNT = 200  # Number of LED pixels.


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=25):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip[i] = color
        time.sleep(wait_ms/1000)


def blockColor(strip, color):
    for i in range(strip):
        strip[i] = color

def rgb(hex):
    return tuple(int(r.text[i:i + 2], 16) for i in (0, 2, 4))

if __name__ == '__main__':

    strip = neopixel.NeoPixel(board.D18, LED_COUNT)

    try:
        while True:
            try:
                r = requests.get(url='http://192.168.4.25:3000/color')
                color = r.text
                blockColor(strip, rgb(color))  # Green wipe
            except:
                print("Server down")
                pass
            time.sleep(.5)

    except KeyboardInterrupt:
        colorWipe(strip, (0, 0, 0), 10)