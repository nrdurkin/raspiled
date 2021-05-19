import time
import board, neopixel
from util import rgb, Mode

from modes.crossFade import CrossFadeCtrl
from modes.fairy import FairyCtrl
from modes.stripe import StripeCtrl
from modes.ripple import RippleCtrl

class ColorStrip:

    def __init__(self):
        self._size = 300
        self._strip = neopixel.NeoPixel(board.D18, self._size, auto_write=False)
        self._mode = Mode.BLOCK

        self._CrossFadeCtrl = CrossFadeCtrl(self._fill)
        self._FairyCtrl = FairyCtrl(self._strip)
        self._StripeCtrl = StripeCtrl(self._strip)
        self._RippleCtrl = RippleCtrl(self._strip, self._fill)

        self._startup()

    def _fill(self, color):
        for i in range(self._size):
            self._strip[i] = color
        self._strip.show()

    def _startup(self):
        self._fill((255, 0, 0))
        time.sleep(.3)
        self._fill((0, 255, 0))
        time.sleep(.3)
        self._fill((0, 0, 255))
        time.sleep(.3)
        self._fill((0, 0, 0))

    def loop(self):
        if self._mode == Mode.CROSSFADE:
            self._CrossFadeCtrl.draw()
        elif self._mode == Mode.FAIRY:
            self._FairyCtrl.draw()
        elif self._mode == Mode.STRIPE:
            self._StripeCtrl.draw()
        elif self._mode == Mode.RIPPLE:
            self._RippleCtrl.draw()

    def setMode(self, mode, *arg):
        self._mode = mode
        if mode == Mode.BLOCK:
            self._fill(rgb(arg[0]))
        elif mode == Mode.FAIRY:
            self._FairyCtrl.start(*arg)
        elif mode == Mode.STRIPE:
            self._StripeCtrl.start(*arg)
        elif mode == Mode.RIPPLE:
            self._RippleCtrl.start()

FPS = 60
def main(strip :ColorStrip):
    # strip.setMode(Mode.RIPPLE)
    lastFrameTime = 0
    while True:
        strip.loop()
        currentTime = time.time()
        sleepTime = 1. / FPS - (currentTime - lastFrameTime)
        lastFrameTime = currentTime
        if sleepTime > 0:
            time.sleep(sleepTime)

